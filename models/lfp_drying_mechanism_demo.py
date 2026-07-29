#!/usr/bin/env python3
"""One-dimensional mechanism demonstrator for drying-stress evolution.

This script is a research demonstrator, not a calibrated LFP process model.
It couples:

1. an effective mobile-NMP redistribution equation with a surface sink;
2. a solvent-state-dependent mechanical locking function;
3. empirical free shrinkage under in-plane substrate constraint;
4. a local Maxwell stress-evolution law; and
5. a through-thickness channel-crack energy index.

Only NumPy and the Python standard library are required.  The script writes
CSV/JSON results and two self-contained SVG figures.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

import numpy as np


@dataclass(frozen=True)
class ModelParameters:
    """Illustrative parameters; none are calibrated to the user's LFP slurry."""

    d_wet_m2_s: float = 8.0e-11
    d_dry_m2_s: float = 2.0e-12
    diffusivity_exponent: float = 2.5
    lock_nmp_midpoint: float = 0.62
    lock_width: float = 0.045
    e_wet_pa: float = 2.0e4
    e_dry_pa: float = 3.0e7
    modulus_exponent: float = 1.5
    tau_wet_s: float = 3.0
    tau_dry_s: float = 1.08e4
    free_shrinkage_max: float = 0.07
    free_shrinkage_exponent: float = 1.3
    in_plane_constraint: float = 0.90
    channel_geometry_factor: float = 1.50
    fracture_energy_j_m2: float = 4.00


@dataclass(frozen=True)
class Scenario:
    key: str
    label_zh: str
    thickness_m: float
    evaporation_coefficient_m_s: float


SCENARIOS = (
    Scenario("thin_slow", "薄层·温和边界", 80.0e-6, 6.0e-8),
    Scenario("thick_slow", "厚层·温和边界", 160.0e-6, 6.0e-8),
    Scenario("thick_fast", "厚层·强蒸发边界", 160.0e-6, 2.0e-7),
)


@dataclass
class SimulationResult:
    scenario: Scenario
    time_s: np.ndarray
    xi: np.ndarray
    nmp: np.ndarray
    lock: np.ndarray
    stress_pa: np.ndarray
    modulus_pa: np.ndarray
    channel_g_j_m2: np.ndarray
    channel_risk: np.ndarray
    top_flux_m_s: np.ndarray
    mass_balance_relative_error: float


def lock_fraction(w: np.ndarray, p: ModelParameters) -> np.ndarray:
    """Continuous switch from fluid-like (0) to load-bearing (1)."""

    arg = np.clip((w - p.lock_nmp_midpoint) / p.lock_width, -60.0, 60.0)
    return 1.0 / (1.0 + np.exp(arg))


def material_state(
    w: np.ndarray, p: ModelParameters
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Return lock fraction, modulus, relaxation time and free strain."""

    lam = lock_fraction(w, p)
    modulus = p.e_wet_pa + (p.e_dry_pa - p.e_wet_pa) * lam**p.modulus_exponent
    log_ratio = math.log(p.tau_dry_s / p.tau_wet_s)
    relaxation = p.tau_wet_s * np.exp(log_ratio * lam)
    free_strain = -p.free_shrinkage_max * np.maximum(1.0 - w, 0.0) ** p.free_shrinkage_exponent
    return lam, modulus, relaxation, free_strain


def effective_diffusivity(w: np.ndarray, p: ModelParameters) -> np.ndarray:
    """Effective internal NMP mobility, not molecular diffusivity."""

    bounded = np.clip(w, 0.0, 1.0)
    return p.d_dry_m2_s + (p.d_wet_m2_s - p.d_dry_m2_s) * bounded**p.diffusivity_exponent


def solve_tridiagonal(
    lower: np.ndarray, diagonal: np.ndarray, upper: np.ndarray, rhs: np.ndarray
) -> np.ndarray:
    """Thomas algorithm for a diagonally dominant tridiagonal system."""

    n = rhs.size
    c_prime = np.empty(n - 1, dtype=float)
    d_prime = np.empty(n, dtype=float)

    c_prime[0] = upper[0] / diagonal[0]
    d_prime[0] = rhs[0] / diagonal[0]
    for i in range(1, n - 1):
        pivot = diagonal[i] - lower[i - 1] * c_prime[i - 1]
        c_prime[i] = upper[i] / pivot
        d_prime[i] = (rhs[i] - lower[i - 1] * d_prime[i - 1]) / pivot

    pivot = diagonal[-1] - lower[-1] * c_prime[-1]
    d_prime[-1] = (rhs[-1] - lower[-1] * d_prime[-2]) / pivot

    solution = np.empty(n, dtype=float)
    solution[-1] = d_prime[-1]
    for i in range(n - 2, -1, -1):
        solution[i] = d_prime[i] - c_prime[i] * solution[i + 1]
    return solution


def simulate(
    scenario: Scenario,
    p: ModelParameters,
    *,
    n_cells: int = 61,
    dt_s: float = 2.0,
    end_time_s: float = 14_400.0,
    save_interval_s: float = 30.0,
) -> SimulationResult:
    """Solve the coupled 1D transport and local stress equations."""

    if n_cells < 5:
        raise ValueError("n_cells must be at least 5")
    if save_interval_s < dt_s:
        raise ValueError("save_interval_s must be greater than or equal to dt_s")

    n_steps = int(round(end_time_s / dt_s))
    save_every = int(round(save_interval_s / dt_s))
    if not math.isclose(save_every * dt_s, save_interval_s, rel_tol=0.0, abs_tol=1e-12):
        raise ValueError("save_interval_s must be an integer multiple of dt_s")

    h = scenario.thickness_m
    dz = h / n_cells
    xi = (np.arange(n_cells, dtype=float) + 0.5) / n_cells
    w = np.ones(n_cells, dtype=float)
    # Evolving the recoverable spring strain, rather than stress directly,
    # preserves the variable-modulus Maxwell identity
    # sigma = E(t) * elastic_strain.  It therefore includes the stress change
    # caused by stiffening without adding an ad-hoc dE/dt term.
    elastic_strain = np.zeros(n_cells, dtype=float)
    stress = np.zeros(n_cells, dtype=float)

    saved_time: list[float] = []
    saved_nmp: list[np.ndarray] = []
    saved_lock: list[np.ndarray] = []
    saved_stress: list[np.ndarray] = []
    saved_modulus: list[np.ndarray] = []
    saved_g: list[float] = []
    saved_risk: list[float] = []
    saved_flux: list[float] = []

    integrated_surface_loss = 0.0

    for step in range(n_steps + 1):
        time_s = step * dt_s
        lam, modulus, _relaxation, _free_strain = material_state(w, p)
        top_flux = scenario.evaporation_coefficient_m_s * w[-1]
        # Tensile part only.  The dimensionless geometry factor is understood
        # to absorb the conventional 1/2 and other channel-crack prefactors.
        # The reference/current thickness stretch is set to one in this first
        # fixed-coordinate demonstrator.
        tensile_stress = np.maximum(stress, 0.0)
        channel_g = (
            p.channel_geometry_factor
            * float(np.sum(tensile_stress * tensile_stress / modulus))
            * dz
        )

        if step % save_every == 0:
            saved_time.append(time_s)
            saved_nmp.append(w.copy())
            saved_lock.append(lam.copy())
            saved_stress.append(stress.copy())
            saved_modulus.append(modulus.copy())
            saved_g.append(channel_g)
            saved_risk.append(channel_g / p.fracture_energy_j_m2)
            saved_flux.append(top_flux)

        if step == n_steps:
            break

        diffusivity = effective_diffusivity(w, p)
        face_diffusivity = (
            2.0
            * diffusivity[:-1]
            * diffusivity[1:]
            / (diffusivity[:-1] + diffusivity[1:] + 1.0e-300)
        )
        face_ratio = dt_s * face_diffusivity / dz**2

        lower = -face_ratio.copy()
        upper = -face_ratio.copy()
        diagonal = np.ones(n_cells, dtype=float)
        diagonal[:-1] += face_ratio
        diagonal[1:] += face_ratio
        # Robin sink at the free surface: j_out = k_e * w_surface.
        diagonal[-1] += dt_s * scenario.evaporation_coefficient_m_s / dz

        w_new = solve_tridiagonal(lower, diagonal, upper, w)
        if float(np.min(w_new)) < -1.0e-10 or float(np.max(w_new)) > 1.0 + 1.0e-10:
            raise RuntimeError("NMP state left physical bounds; reduce dt or inspect the solver")

        w_mid = 0.5 * (w + w_new)
        _lam_mid, modulus_mid, relaxation_mid, _strain_mid = material_state(w_mid, p)
        _lam_old, _modulus_old, _relax_old, strain_old = material_state(w, p)
        _lam_new, _modulus_new, _relax_new, strain_new = material_state(w_new, p)

        # Full in-plane constraint would impose zero total strain.  The scalar
        # factor allows a first-order reduction for foil compliance/slip.
        loading_rate = -p.in_plane_constraint * (strain_new - strain_old) / dt_s
        decay = np.exp(-dt_s / relaxation_mid)
        elastic_strain = (
            elastic_strain * decay
            + loading_rate * relaxation_mid * (1.0 - decay)
        )
        stress = _modulus_new * elastic_strain

        # The backward-Euler transport step uses the new-time surface flux, so
        # the discrete inventory check must integrate that same flux.
        new_top_flux = scenario.evaporation_coefficient_m_s * w_new[-1]
        integrated_surface_loss += new_top_flux * dt_s
        w = w_new

    initial_inventory = h
    final_inventory = h * float(np.mean(w))
    balance_error = abs(initial_inventory - final_inventory - integrated_surface_loss) / initial_inventory

    return SimulationResult(
        scenario=scenario,
        time_s=np.asarray(saved_time),
        xi=xi,
        nmp=np.asarray(saved_nmp),
        lock=np.asarray(saved_lock),
        stress_pa=np.asarray(saved_stress),
        modulus_pa=np.asarray(saved_modulus),
        channel_g_j_m2=np.asarray(saved_g),
        channel_risk=np.asarray(saved_risk),
        top_flux_m_s=np.asarray(saved_flux),
        mass_balance_relative_error=balance_error,
    )


def first_crossing_time(
    time_s: np.ndarray, values: np.ndarray, threshold: float
) -> float | None:
    indices = np.flatnonzero(values >= threshold)
    return None if indices.size == 0 else float(time_s[int(indices[0])])


def scenario_summary(result: SimulationResult) -> dict[str, float | str | None]:
    top = -1
    middle = result.xi.size // 2
    bottom = 0
    max_flat_index = int(np.argmax(result.stress_pa))
    max_time_index, max_height_index = np.unravel_index(
        max_flat_index, result.stress_pa.shape
    )
    risk_peak_index = int(np.argmax(result.channel_risk))
    return {
        "scenario": result.scenario.key,
        "label_zh": result.scenario.label_zh,
        "thickness_um": result.scenario.thickness_m * 1.0e6,
        "evaporation_coefficient_m_s": result.scenario.evaporation_coefficient_m_s,
        "final_mean_nmp": float(np.mean(result.nmp[-1])),
        "top_lock_50_min": _minutes(
            first_crossing_time(result.time_s, result.lock[:, top], 0.5)
        ),
        "middle_lock_50_min": _minutes(
            first_crossing_time(result.time_s, result.lock[:, middle], 0.5)
        ),
        "bottom_lock_50_min": _minutes(
            first_crossing_time(result.time_s, result.lock[:, bottom], 0.5)
        ),
        "peak_stress_mpa": float(result.stress_pa[max_time_index, max_height_index] / 1.0e6),
        "peak_stress_time_min": float(result.time_s[max_time_index] / 60.0),
        "peak_stress_height_fraction": float(result.xi[max_height_index]),
        "peak_channel_g_j_m2": float(np.max(result.channel_g_j_m2)),
        "peak_channel_risk": float(np.max(result.channel_risk)),
        "peak_channel_risk_time_min": float(result.time_s[risk_peak_index] / 60.0),
        "risk_one_crossing_min": _minutes(
            first_crossing_time(result.time_s, result.channel_risk, 1.0)
        ),
        "mass_balance_relative_error": result.mass_balance_relative_error,
    }


def _minutes(value_s: float | None) -> float | None:
    return None if value_s is None else value_s / 60.0


def write_outputs(
    output_dir: Path,
    results: Iterable[SimulationResult],
    parameters: ModelParameters,
) -> list[dict[str, float | str | None]]:
    output_dir.mkdir(parents=True, exist_ok=True)
    result_list = list(results)
    summaries = [scenario_summary(result) for result in result_list]

    with (output_dir / "scenario_summary.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(summaries[0]))
        writer.writeheader()
        writer.writerows(summaries)

    with (output_dir / "scenario_timeseries.csv").open("w", newline="", encoding="utf-8") as handle:
        fieldnames = [
            "scenario",
            "time_min",
            "mean_nmp",
            "bottom_nmp",
            "middle_nmp",
            "top_nmp",
            "bottom_stress_mpa",
            "middle_stress_mpa",
            "top_stress_mpa",
            "max_stress_mpa",
            "channel_g_j_m2",
            "channel_risk",
        ]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for result in result_list:
            middle = result.xi.size // 2
            for i, time_s in enumerate(result.time_s):
                writer.writerow(
                    {
                        "scenario": result.scenario.key,
                        "time_min": f"{time_s / 60.0:.6g}",
                        "mean_nmp": f"{np.mean(result.nmp[i]):.8g}",
                        "bottom_nmp": f"{result.nmp[i, 0]:.8g}",
                        "middle_nmp": f"{result.nmp[i, middle]:.8g}",
                        "top_nmp": f"{result.nmp[i, -1]:.8g}",
                        "bottom_stress_mpa": f"{result.stress_pa[i, 0] / 1.0e6:.8g}",
                        "middle_stress_mpa": f"{result.stress_pa[i, middle] / 1.0e6:.8g}",
                        "top_stress_mpa": f"{result.stress_pa[i, -1] / 1.0e6:.8g}",
                        "max_stress_mpa": f"{np.max(result.stress_pa[i]) / 1.0e6:.8g}",
                        "channel_g_j_m2": f"{result.channel_g_j_m2[i]:.8g}",
                        "channel_risk": f"{result.channel_risk[i]:.8g}",
                    }
                )

    baseline = next(result for result in result_list if result.scenario.key == "thick_fast")
    with (output_dir / "thick_fast_height_profiles.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        fieldnames = [
            "time_min",
            "height_fraction",
            "nmp_state",
            "lock_fraction",
            "stress_mpa",
            "modulus_mpa",
        ]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for i, time_s in enumerate(baseline.time_s):
            for j, xi in enumerate(baseline.xi):
                writer.writerow(
                    {
                        "time_min": f"{time_s / 60.0:.6g}",
                        "height_fraction": f"{xi:.8g}",
                        "nmp_state": f"{baseline.nmp[i, j]:.8g}",
                        "lock_fraction": f"{baseline.lock[i, j]:.8g}",
                        "stress_mpa": f"{baseline.stress_pa[i, j] / 1.0e6:.8g}",
                        "modulus_mpa": f"{baseline.modulus_pa[i, j] / 1.0e6:.8g}",
                    }
                )

    compact = {
        "notice_zh": "机制演示参数，未用 LFP–PVDF/NMP 数据校准，不可作为量产工艺窗口。",
        "parameters": asdict(parameters),
        "summaries": summaries,
        "scenarios": {},
    }
    for result in result_list:
        # Downsample to keep the interactive payload compact.
        t_idx = np.unique(np.linspace(0, result.time_s.size - 1, 121).round().astype(int))
        z_idx = np.unique(np.linspace(0, result.xi.size - 1, 41).round().astype(int))
        compact["scenarios"][result.scenario.key] = {
            "label": result.scenario.label_zh,
            "thickness_um": result.scenario.thickness_m * 1.0e6,
            "time_min": np.round(result.time_s[t_idx] / 60.0, 4).tolist(),
            "height_fraction": np.round(result.xi[z_idx], 5).tolist(),
            "nmp": np.round(result.nmp[np.ix_(t_idx, z_idx)], 5).tolist(),
            "lock": np.round(result.lock[np.ix_(t_idx, z_idx)], 5).tolist(),
            "stress_mpa": np.round(
                result.stress_pa[np.ix_(t_idx, z_idx)] / 1.0e6, 5
            ).tolist(),
            "risk": np.round(result.channel_risk[t_idx], 5).tolist(),
        }
    with (output_dir / "interactive_payload.json").open("w", encoding="utf-8") as handle:
        json.dump(compact, handle, ensure_ascii=False, separators=(",", ":"))

    return summaries


def hex_to_rgb(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    return int(value[0:2], 16), int(value[2:4], 16), int(value[4:6], 16)


def blend_hex(low: str, high: str, fraction: float) -> str:
    a = hex_to_rgb(low)
    b = hex_to_rgb(high)
    x = min(max(fraction, 0.0), 1.0)
    return "#" + "".join(f"{round(v0 + (v1 - v0) * x):02x}" for v0, v1 in zip(a, b))


def svg_text(x: float, y: float, text: str, css_class: str = "label", anchor: str = "start") -> str:
    escaped = (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )
    return f'<text x="{x:.1f}" y="{y:.1f}" class="{css_class}" text-anchor="{anchor}">{escaped}</text>'


def polyline(points: list[tuple[float, float]], color: str, css_class: str = "series") -> str:
    encoded = " ".join(f"{x:.2f},{y:.2f}" for x, y in points)
    return f'<polyline points="{encoded}" class="{css_class}" stroke="{color}" />'


def heatmap_panel(
    values: np.ndarray,
    time_min: np.ndarray,
    xi: np.ndarray,
    *,
    x: float,
    y: float,
    width: float,
    height: float,
    low_color: str,
    high_color: str,
    vmin: float,
    vmax: float,
    title: str,
    legend_min: str,
    legend_max: str,
    marker_time_min: float | None = None,
    marker_label: str | None = None,
) -> str:
    t_idx = np.unique(np.linspace(0, values.shape[0] - 1, 101).round().astype(int))
    z_idx = np.unique(np.linspace(0, values.shape[1] - 1, 41).round().astype(int))
    data = values[np.ix_(t_idx, z_idx)]
    cell_w = width / data.shape[0]
    cell_h = height / data.shape[1]
    parts = [svg_text(x, y - 18, title, "panel-title")]
    for ti in range(data.shape[0]):
        for zi in range(data.shape[1]):
            fraction = (float(data[ti, zi]) - vmin) / max(vmax - vmin, 1.0e-30)
            fill = blend_hex(low_color, high_color, fraction)
            # z=1 is the top and is drawn at the top of the panel.
            draw_y = y + height - (zi + 1) * cell_h
            parts.append(
                f'<rect x="{x + ti * cell_w:.2f}" y="{draw_y:.2f}" '
                f'width="{cell_w + 0.25:.2f}" height="{cell_h + 0.25:.2f}" fill="{fill}" />'
            )
    parts.append(f'<rect x="{x}" y="{y}" width="{width}" height="{height}" class="frame" />')
    if marker_time_min is not None:
        marker_x = x + marker_time_min / float(time_min[-1]) * width
        parts.append(
            f'<line x1="{marker_x:.2f}" y1="{y}" x2="{marker_x:.2f}" '
            f'y2="{y + height}" stroke="#5e2530" stroke-width="2.2" stroke-dasharray="10 7" />'
        )
        if marker_label:
            parts.append(svg_text(marker_x + 8, y + 24, marker_label, "tick"))
    for fraction, tick in ((0.0, "0"), (0.5, f"{time_min[-1] / 2:.0f}"), (1.0, f"{time_min[-1]:.0f}")):
        tx = x + fraction * width
        parts.append(f'<line x1="{tx}" y1="{y + height}" x2="{tx}" y2="{y + height + 8}" class="axis" />')
        parts.append(svg_text(tx, y + height + 30, tick, "tick", "middle"))
    parts.append(svg_text(x + width / 2, y + height + 58, "时间 / min", "axis-label", "middle"))
    for fraction, label in ((0.0, "箔侧 0"), (0.5, "中层"), (1.0, "表面 1")):
        ty = y + height - fraction * height
        parts.append(f'<line x1="{x - 8}" y1="{ty}" x2="{x}" y2="{ty}" class="axis" />')
        parts.append(svg_text(x - 14, ty + 5, label, "tick", "end"))
    legend_y = y + height + 92
    steps = 60
    for i in range(steps):
        fill = blend_hex(low_color, high_color, i / (steps - 1))
        parts.append(
            f'<rect x="{x + i * width / steps:.2f}" y="{legend_y:.2f}" '
            f'width="{width / steps + 0.25:.2f}" height="12" fill="{fill}" />'
        )
    parts.append(svg_text(x, legend_y + 32, legend_min, "tick"))
    parts.append(svg_text(x + width, legend_y + 32, legend_max, "tick", "end"))
    return "\n".join(parts)


def make_mechanism_svg(result: SimulationResult, output_path: Path) -> None:
    width, height = 1800, 1480
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<title>一维厚向 NMP 输运、锁定与干燥应力机制演示</title>',
        '<desc>以未校准示意参数计算厚层强蒸发边界下的 NMP 状态、机械锁定比例、面内拉应力和选定时刻的高度剖面。</desc>',
        """<style>
        .bg { fill:#f7f8fa; }
        .title { font:700 34px Arial,'PingFang SC','Microsoft YaHei',sans-serif; fill:#172033; }
        .subtitle { font:400 20px Arial,'PingFang SC','Microsoft YaHei',sans-serif; fill:#5c667a; }
        .panel-title { font:700 23px Arial,'PingFang SC','Microsoft YaHei',sans-serif; fill:#172033; }
        .label,.axis-label { font:400 18px Arial,'PingFang SC','Microsoft YaHei',sans-serif; fill:#26334a; }
        .tick { font:400 15px Arial,'PingFang SC','Microsoft YaHei',sans-serif; fill:#5c667a; }
        .small { font:400 16px Arial,'PingFang SC','Microsoft YaHei',sans-serif; fill:#5c667a; }
        .strong { font:700 18px Arial,'PingFang SC','Microsoft YaHei',sans-serif; fill:#172033; }
        .frame { fill:none; stroke:#8e98aa; stroke-width:1.2; }
        .axis { stroke:#7d8798; stroke-width:1.2; }
        .grid { stroke:#d9dee8; stroke-width:1; }
        .series { fill:none; stroke-width:4; stroke-linejoin:round; stroke-linecap:round; }
        .dash { fill:none; stroke-width:4; stroke-dasharray:12 9; stroke-linejoin:round; }
        .chain { fill:#ffffff; stroke:#cbd2df; stroke-width:1.5; rx:12; }
        .arrow { stroke:#6f7a8e; stroke-width:2.2; fill:none; marker-end:url(#arrow); }
        </style>""",
        '<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#6f7a8e" /></marker></defs>',
        f'<rect width="{width}" height="{height}" class="bg" />',
        svg_text(80, 70, "NMP 输运受限如何形成厚向应力：1D 机制演示", "title"),
        svg_text(80, 108, "厚层·强蒸发边界；全部参数为示意值，未用 LFP–PVDF/NMP 数据校准", "subtitle"),
    ]

    chain_labels = ["NMP 状态梯度", "锁定时间不同", "自由收缩不同步", "面内拉应力分层", "G/Γ 上升"]
    chain_x = [80, 410, 740, 1070, 1400]
    for i, (cx, label) in enumerate(zip(chain_x, chain_labels)):
        parts.append(f'<rect x="{cx}" y="145" width="280" height="64" class="chain" />')
        parts.append(svg_text(cx + 140, 184, label, "strong", "middle"))
        if i < len(chain_x) - 1:
            parts.append(f'<path d="M {cx + 280} 177 L {chain_x[i + 1] - 20} 177" class="arrow" />')

    time_min = result.time_s / 60.0
    heat_width, heat_height = 690, 330
    risk_crossing_s = first_crossing_time(result.time_s, result.channel_risk, 1.0)
    risk_crossing_min = None if risk_crossing_s is None else risk_crossing_s / 60.0
    parts.append(
        heatmap_panel(
            result.nmp,
            time_min,
            result.xi,
            x=120,
            y=285,
            width=heat_width,
            height=heat_height,
            low_color="#f7fbff",
            high_color="#1769aa",
            vmin=0.0,
            vmax=1.0,
            title="A  归一化移动 NMP 状态 w(z,t)",
            legend_min="0：局部 NMP 已低",
            legend_max="1：初始湿态",
            marker_time_min=risk_crossing_min,
        )
    )
    parts.append(
        heatmap_panel(
            result.lock,
            time_min,
            result.xi,
            x=990,
            y=285,
            width=heat_width,
            height=heat_height,
            low_color="#fff9ee",
            high_color="#d97904",
            vmin=0.0,
            vmax=1.0,
            title="B  机械锁定比例 λ(z,t)",
            legend_min="0：可快速松弛",
            legend_max="1：可持续承载",
            marker_time_min=risk_crossing_min,
        )
    )

    stress_mpa = result.stress_pa / 1.0e6
    stress_vmax = max(1.05, float(np.max(stress_mpa)))
    parts.append(
        heatmap_panel(
            stress_mpa,
            time_min,
            result.xi,
            x=120,
            y=835,
            width=heat_width,
            height=heat_height,
            low_color="#fff8f5",
            high_color="#b42318",
            vmin=0.0,
            vmax=stress_vmax,
            title="C  面内拉应力 σ∥(z,t) / MPa",
            legend_min="0 MPa",
            legend_max=f"{stress_vmax:.2f} MPa（示意）",
            marker_time_min=risk_crossing_min,
            marker_label=(
                None
                if risk_crossing_min is None
                else f"Rch=1，{risk_crossing_min:.0f} min"
            ),
        )
    )

    # Height profiles at representative process times.
    plot_x, plot_y, plot_w, plot_h = 990, 835, 690, 330
    parts.append(svg_text(plot_x, plot_y - 18, "D  不同时刻的厚向拉应力剖面", "panel-title"))
    for gy in np.linspace(0, 1, 5):
        yy = plot_y + plot_h - gy * plot_h
        parts.append(f'<line x1="{plot_x}" y1="{yy}" x2="{plot_x + plot_w}" y2="{yy}" class="grid" />')
        parts.append(svg_text(plot_x - 14, yy + 5, f"{gy:.2g}", "tick", "end"))
    for gx in np.linspace(0, stress_vmax, 5):
        xx = plot_x + gx / stress_vmax * plot_w
        parts.append(f'<line x1="{xx}" y1="{plot_y}" x2="{xx}" y2="{plot_y + plot_h}" class="grid" />')
        parts.append(svg_text(xx, plot_y + plot_h + 30, f"{gx:.2f}", "tick", "middle"))
    parts.append(f'<rect x="{plot_x}" y="{plot_y}" width="{plot_w}" height="{plot_h}" class="frame" />')
    parts.append(svg_text(plot_x + plot_w / 2, plot_y + plot_h + 58, "σ∥ / MPa", "axis-label", "middle"))
    parts.append(svg_text(plot_x - 72, plot_y + plot_h / 2, "参考高度 ξ", "axis-label", "middle"))

    target_times = (20.0, 45.0, 75.0, 120.0)
    colors = ("#2f6db3", "#d97904", "#b42318", "#7137a8")
    for target, color in zip(target_times, colors):
        idx = int(np.argmin(np.abs(time_min - target)))
        points = [
            (
                plot_x + stress_mpa[idx, j] / stress_vmax * plot_w,
                plot_y + plot_h - result.xi[j] * plot_h,
            )
            for j in range(result.xi.size)
        ]
        parts.append(polyline(points, color))
    legend_y = 1265
    for i, (target, color) in enumerate(zip(target_times, colors)):
        lx = plot_x + i * 170
        parts.append(f'<line x1="{lx}" y1="{legend_y}" x2="{lx + 48}" y2="{legend_y}" stroke="{color}" stroke-width="4" />')
        parts.append(svg_text(lx + 58, legend_y + 6, f"{target:.0f} min", "small"))

    summary = scenario_summary(result)
    parts.extend(
        [
            svg_text(120, 1335, "读图：", "strong"),
            svg_text(190, 1335, "表面先失去 NMP 并锁定；高应力带随后向中层和箔侧推进。", "label"),
            svg_text(
                120,
                1375,
                f"本次示意计算：表面/中层/箔侧 λ=0.5 分别约在 {summary['top_lock_50_min']:.1f} / {summary['middle_lock_50_min']:.1f} / {summary['bottom_lock_50_min']:.1f} min；峰值应力约 {summary['peak_stress_mpa']:.2f} MPa。",
                "label",
            ),
            svg_text(120, 1415, "限制：虚线以后是假定涂层保持完整的反事实轨迹；模型无裂后卸载，也不给层间剪应力。", "small"),
        ]
    )
    parts.append("</svg>")
    output_path.write_text("\n".join(parts), encoding="utf-8")


def make_comparison_svg(results: list[SimulationResult], output_path: Path) -> None:
    width, height = 1800, 980
    colors = {"thin_slow": "#2f6db3", "thick_slow": "#d97904", "thick_fast": "#b42318"}
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<title>厚度与蒸发边界对 NMP、应力和断裂能指标的影响</title>',
        '<desc>比较薄层温和、厚层温和与厚层强蒸发三个未校准示意工况。</desc>',
        """<style>
        .bg { fill:#f7f8fa; }
        .title { font:700 34px Arial,'PingFang SC','Microsoft YaHei',sans-serif; fill:#172033; }
        .subtitle { font:400 20px Arial,'PingFang SC','Microsoft YaHei',sans-serif; fill:#5c667a; }
        .panel-title { font:700 22px Arial,'PingFang SC','Microsoft YaHei',sans-serif; fill:#172033; }
        .label,.axis-label { font:400 17px Arial,'PingFang SC','Microsoft YaHei',sans-serif; fill:#26334a; }
        .tick,.small { font:400 15px Arial,'PingFang SC','Microsoft YaHei',sans-serif; fill:#5c667a; }
        .frame { fill:none; stroke:#8e98aa; stroke-width:1.2; }
        .grid { stroke:#d9dee8; stroke-width:1; }
        .series { fill:none; stroke-width:4; stroke-linejoin:round; stroke-linecap:round; }
        .threshold { stroke:#606b7d; stroke-width:2; stroke-dasharray:10 8; }
        </style>""",
        f'<rect width="{width}" height="{height}" class="bg" />',
        svg_text(80, 70, "厚度 × 蒸发边界：三个机制演示工况", "title"),
        svg_text(80, 108, "比较的是模型内部因果响应，不是量产窗口；Γ 与全部物性均为示意值", "subtitle"),
    ]

    panel_specs = (
        ("A  平均移动 NMP 状态", lambda r: np.mean(r.nmp, axis=1), 0.0, 1.0, "平均 w"),
        ("B  厚度内最大面内拉应力", lambda r: np.max(r.stress_pa, axis=1) / 1.0e6, 0.0, 1.2, "最大 σ∥ / MPa"),
        ("C  通道裂纹结构代理 Rch", lambda r: r.channel_risk, 0.0, 1.4, "Rch = Gproxy / Γref"),
    )
    panel_xs = (90, 650, 1210)
    plot_y, plot_w, plot_h = 230, 470, 460
    max_time = max(float(result.time_s[-1] / 60.0) for result in results)

    for p_idx, ((title, getter, ymin, ymax, y_label), px) in enumerate(zip(panel_specs, panel_xs)):
        parts.append(svg_text(px, plot_y - 28, title, "panel-title"))
        for gy in np.linspace(ymin, ymax, 5):
            yy = plot_y + plot_h - (gy - ymin) / (ymax - ymin) * plot_h
            parts.append(f'<line x1="{px}" y1="{yy}" x2="{px + plot_w}" y2="{yy}" class="grid" />')
            parts.append(svg_text(px - 12, yy + 5, f"{gy:.2g}", "tick", "end"))
        for gx in np.linspace(0.0, max_time, 5):
            xx = px + gx / max_time * plot_w
            parts.append(f'<line x1="{xx}" y1="{plot_y}" x2="{xx}" y2="{plot_y + plot_h}" class="grid" />')
            parts.append(svg_text(xx, plot_y + plot_h + 30, f"{gx:.0f}", "tick", "middle"))
        if p_idx == 2:
            threshold_y = plot_y + plot_h - (1.0 - ymin) / (ymax - ymin) * plot_h
            parts.append(f'<line x1="{px}" y1="{threshold_y}" x2="{px + plot_w}" y2="{threshold_y}" class="threshold" />')
            parts.append(svg_text(px + plot_w - 6, threshold_y - 8, "示意阈值 Rch=1", "small", "end"))
        parts.append(f'<rect x="{px}" y="{plot_y}" width="{plot_w}" height="{plot_h}" class="frame" />')
        parts.append(svg_text(px + plot_w / 2, plot_y + plot_h + 62, "时间 / min", "axis-label", "middle"))
        parts.append(svg_text(px + 8, plot_y + 26, y_label, "small"))
        for result in results:
            values = getter(result)
            points = [
                (
                    px + float(t / 60.0) / max_time * plot_w,
                    plot_y + plot_h - (float(v) - ymin) / (ymax - ymin) * plot_h,
                )
                for t, v in zip(result.time_s, values)
            ]
            parts.append(polyline(points, colors[result.scenario.key]))

    legend_y = 790
    for i, result in enumerate(results):
        lx = 150 + i * 500
        color = colors[result.scenario.key]
        summary = scenario_summary(result)
        parts.append(f'<line x1="{lx}" y1="{legend_y}" x2="{lx + 60}" y2="{legend_y}" stroke="{color}" stroke-width="5" />')
        parts.append(svg_text(lx + 75, legend_y + 6, result.scenario.label_zh, "label"))
        parts.append(
            svg_text(
                lx,
                legend_y + 42,
                f"Hr={summary['thickness_um']:.0f} μm；峰值 σ={summary['peak_stress_mpa']:.2f} MPa；max Rch={summary['peak_channel_risk']:.2f}",
                "small",
            )
        )
    parts.append(svg_text(90, 895, "读图边界：Rch=1 仅因本演示把 Γ 固定为 4.00 J/m²；在目标 LFP 中，Γ、E、τ、D、约束和缺陷均须独立标定。", "label"))
    parts.append(svg_text(90, 930, "红线跨过 Rch=1 后仍继续计算的是“假定不开裂”的完整膜反事实；真实裂纹会释放应力，需损伤反馈模型。", "small"))
    parts.append("</svg>")
    output_path.write_text("\n".join(parts), encoding="utf-8")


def convergence_check(
    scenario: Scenario, p: ModelParameters, end_time_s: float
) -> dict[str, float]:
    coarse = simulate(
        scenario,
        p,
        n_cells=41,
        dt_s=4.0,
        end_time_s=end_time_s,
        save_interval_s=60.0,
    )
    fine = simulate(
        scenario,
        p,
        n_cells=81,
        dt_s=1.0,
        end_time_s=end_time_s,
        save_interval_s=60.0,
    )
    return {
        "coarse_peak_stress_mpa": float(np.max(coarse.stress_pa) / 1.0e6),
        "fine_peak_stress_mpa": float(np.max(fine.stress_pa) / 1.0e6),
        "peak_stress_relative_difference": float(
            abs(np.max(coarse.stress_pa) - np.max(fine.stress_pa))
            / np.max(fine.stress_pa)
        ),
        "coarse_peak_risk": float(np.max(coarse.channel_risk)),
        "fine_peak_risk": float(np.max(fine.channel_risk)),
        "peak_risk_relative_difference": float(
            abs(np.max(coarse.channel_risk) - np.max(fine.channel_risk))
            / np.max(fine.channel_risk)
        ),
        "coarse_mass_balance_error": coarse.mass_balance_relative_error,
        "fine_mass_balance_error": fine.mass_balance_relative_error,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    project_root = Path(__file__).resolve().parents[1]
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=project_root / "models" / "outputs" / "lfp_drying_mechanism_demo",
    )
    parser.add_argument(
        "--image-dir",
        type=Path,
        default=project_root / "findings" / "lfp_pvdf_nmp_drying" / "images",
    )
    parser.add_argument("--end-time-min", type=float, default=240.0)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    parameters = ModelParameters()
    end_time_s = args.end_time_min * 60.0
    results = [
        simulate(
            scenario,
            parameters,
            n_cells=61,
            dt_s=2.0,
            end_time_s=end_time_s,
            save_interval_s=30.0,
        )
        for scenario in SCENARIOS
    ]
    summaries = write_outputs(args.output_dir, results, parameters)
    args.image_dir.mkdir(parents=True, exist_ok=True)
    make_mechanism_svg(
        next(result for result in results if result.scenario.key == "thick_fast"),
        args.image_dir / "11_lfp_thickness_stress_evolution.svg",
    )
    make_comparison_svg(
        results,
        args.image_dir / "12_lfp_stress_scenario_comparison.svg",
    )
    convergence = convergence_check(SCENARIOS[-1], parameters, end_time_s)
    with (args.output_dir / "numerical_checks.json").open("w", encoding="utf-8") as handle:
        json.dump(convergence, handle, ensure_ascii=False, indent=2)

    print(json.dumps({"summaries": summaries, "numerical_checks": convergence}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
