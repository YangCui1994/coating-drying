# papers_Yang 文献逐篇解读与证据审计

> 审阅日期：2026-07-23。  
> 审阅范围：本地 [papers_Yang](../papers_Yang/) 中 17 个 PDF；逐页文本抽取并对关键公式、图表和结论页做视觉复核。  
> Dawson 学位论文及关联论文的深入解释见[单独报告](12_dawson_thesis_deep_read.md)；公式变量、单位和适用边界见[公式手册](13_formula_and_symbol_guide.md)。  
> 引用方式：每项实质性结论同时给出本地 PDF 页码与 DOI/官方入口。页码均指 PDF 阅读器页码，而非期刊印刷页；需要印刷页对照时另行说明。

## 1. 语料清点：17 个文件不等于 17 项独立证据

| 本地文件 | 文献身份 | 去重/纳入判定 |
|---|---|---|
| [Dawson_Thesis.pdf](../papers_Yang/Dawson_Thesis.pdf) | Dawson 2025 UCL 博士论文 | 独立来源；重点深读 |
| [d5eb00201j.pdf](../papers_Yang/d5eb00201j.pdf) | Dawson et al. 2026，带 White Rose 封面的版本 | 与下一文件同一论文，只登记一次 |
| [d5eb00201j (1).pdf](<../papers_Yang/d5eb00201j (1).pdf>) | Dawson et al. 2026，期刊排版版 | 同一 DOI 的首选阅读版本 |
| [d6eb00017g.pdf](../papers_Yang/d6eb00017g.pdf) | Morrison et al. 2026，Dawson 合著 | 独立来源；裂后局部输运 |
| [Energy Tech…Kumberg.pdf](<../papers_Yang/Energy Tech - 2019 - Kumberg - Drying of Lithium‐Ion Battery Anodes for Use in High‐Energy Cells  Influence of Electrode.pdf>) | Kumberg et al. 2019 | 独立来源 |
| [jaiser2017.pdf](../papers_Yang/jaiser2017.pdf) | Jaiser et al. 2017 | 独立来源 |
| [processes-11-03236.pdf](../papers_Yang/processes-11-03236.pdf) | Zhao et al. 2023 | 独立来源；公式需纠错 |
| [Li-ion Electrode…pdf](<../papers_Yang/Li-ion Electrode Microstructure Evolution during Drying and Calen.pdf>) | Nikpour et al. 2022 | 独立来源 |
| [1605.00599v3.pdf](../papers_Yang/1605.00599v3.pdf) | Bertrand et al. 2016 | 独立来源 |
| [Arai 2012…pdf](<../papers_Yang/Arai 2012, Skin formation and bubble growth during drying processof polymer solution.pdf>) | Arai & Doi 2012 | 独立来源 |
| [Moorhead 2024.pdf](<../papers_Yang/Journal of the American Ceramic Society - 2024 - Moorhead - Characterizing stress development and cracking of ceramic.pdf>) | Moorhead & Francis 2024 | 独立来源 |
| [Moorhead 2024 (1).pdf](<../papers_Yang/Journal of the American Ceramic Society - 2024 - Moorhead - Characterizing stress development and cracking of ceramic (1).pdf>) | 同上 | 与上一文件 SHA-256 完全相同，不重复计证据 |
| [cardinal2010.pdf](../papers_Yang/cardinal2010.pdf) | Cardinal et al. 2010 | 独立来源 |
| [tirumkudulu2005.pdf](../papers_Yang/tirumkudulu2005.pdf) | Tirumkudulu & Russel 2005 | 独立来源 |
| [tang2021.pdf](../papers_Yang/tang2021.pdf) | Tang et al. 2021 | 独立来源；综述 |
| [zeng2019.pdf](../papers_Yang/zeng2019.pdf) | Zeng et al. 2019 | 独立来源 |
| [s41560-026-02087-6.pdf](../papers_Yang/s41560-026-02087-6.pdf) | Wang et al. 2026 | 排除：循环期颗粒破裂，不是涂布干燥开裂 |

因此，本文件夹对应 14 项与当前问题有关的独立文献来源，加 1 项因“cracking”同词异义而排除的文献；两个重复组不能重复增加证据权重。

## 2. 这些论文合起来真正告诉了我们什么

### 2.1 目标和近邻电池体系

1. **厚度与干燥强度共同决定风险，而不是只由烘箱温度决定。** Kumberg 的水系石墨楔形厚膜显示，在其体系中低通量样品即使较厚也不裂，而较高通量下才出现临界厚度和裂纹面积变化；这是“厚度×实际蒸发通量”的直接电池证据，不是 LFP 数值阈值。[本地 PDF pp.7–8](<../papers_Yang/Energy Tech - 2019 - Kumberg - Drying of Lithium‐Ion Battery Anodes for Use in High‐Energy Cells  Influence of Electrode.pdf#page=7>)；[DOI 10.1002/ente.201900722](https://doi.org/10.1002/ente.201900722)

2. **宏观收缩结束之后，液体迁移和孔排空仍在继续。** Jaiser 的冷冻截面直接看到大孔先排空、小孔及表面孔继续含液，并观察到孤立液簇和颗粒接触处的 pendular rings；这比仅凭失重曲线推断更强。[本地 PDF pp.7–9](../papers_Yang/jaiser2017.pdf#page=7)；[DOI 10.1016/j.jpowsour.2017.01.117](https://doi.org/10.1016/j.jpowsour.2017.01.117)

3. **PVDF“必然上浮”不成立。** Jaiser 观察到特定石墨负极中的 PVDF 梯度早于明显孔排空和宏观收缩终止；Nikpour 则在 NMC532/PVDF/NMP 中发现明显厚向非均匀主要出现在 150 °C 以上，而面内异质在全部条件都存在。材料、温度、检测方法和面内位置都会改变结论。[Jaiser 本地 PDF p.8](../papers_Yang/jaiser2017.pdf#page=8)；[Nikpour 本地 PDF pp.13–16](<../papers_Yang/Li-ion Electrode Microstructure Evolution during Drying and Calen.pdf#page=13>)；[DOI 10.3390/batteries8090107](https://doi.org/10.3390/batteries8090107)

4. **Dawson 证明了事件链，但没有给出商用 LFP 工艺窗口。** NMC622/PVDF/NMP 小圆柱 CT 样品显示固结、气泡逸出、主裂纹和脱层可以先后发生；DVC 还发现可见裂纹前的局部位移异常。配方、钢柱、常温慢干和毫米级样品使任何具体时间或厚度数值都不可直接迁移。[本地期刊 PDF pp.3–12](<../papers_Yang/d5eb00201j (1).pdf#page=3>)；[DOI 10.1039/D5EB00201J](https://doi.org/10.1039/D5EB00201J)

5. **裂纹形成后的功能也不是简单“高速通道”。** Morrison 的局部 operando XRD 显示，裂纹附近的嵌锂差异具有倍率和深度窗口，厚向梯度通常比横向近裂/远裂差异更强；该结果回答裂后传输，不回答起裂。[本地 PDF pp.7–11](../papers_Yang/d6eb00017g.pdf#page=7)；[DOI 10.1039/D6EB00017G](https://doi.org/10.1039/D6EB00017G)

### 2.2 跨领域文献提供的不是 LFP 常数，而是判别结构

- 胶体/陶瓷论文提供“干燥应力随状态演化、厚度增加能量释放、峰值应力与裂纹不一一对应”的框架。
- 聚合物论文提供“结皮—皮下负压—已有气泡扩散增长”的候选分支，但气体组成并未直接测得。
- 凝胶孔弹性提供“外层先干、内部压力均化时间随长度平方增长”的模型结构；内部应力多为模型预测。
- 岩土研究提醒：缺陷、底面约束、厚度、收缩和界面脱离必须分开统计；某些土体可以在仍近饱和时开裂，因此“先侵气后开裂”不是跨材料普适顺序。

这些论文最重要的共同结论是：同一个最终表面形貌可以由不同状态路径产生，必须保存时间顺序和内部证据。

## 3. 电池论文逐篇解读

### 3.1 Kumberg et al. 2019：厚度、蒸发通量、黏附与裂纹

文献：J. Kumberg et al., *Energy Technology* 7, 1900722，[DOI 10.1002/ente.201900722](https://doi.org/10.1002/ente.201900722)。

本论文已经拆分为三个可独立阅读的交付件：[完整中文翻译](16_kumberg_2019_full_translation_zh.md)、[专有名词与符号中英对照](17_kumberg_2019_terminology.md)和[逐图逐公式深度解读](18_kumberg_2019_deep_read.md)。本节只保留跨论文证据矩阵所需的摘要。

体系为 43 wt% 固含的石墨–导电炭–CMC/SBR 水系负极；干膜楔形厚度约 89–512 µm，涂层宽约 100 mm。它是本文件夹中最接近“厚度×干燥速率×裂纹”的电池实验，但溶剂、粘结剂、活性物和集流体界面均不同。

关键观察：

- 厚样在宏观收缩停止后仍保持较长恒速段；末期偏离气侧动力学被作者解释为连续液路断开后的孤立液簇，但该文没有直接成像液簇。[本地 PDF pp.3–4、9](<../papers_Yang/Energy Tech - 2019 - Kumberg - Drying of Lithium‐Ion Battery Anodes for Use in High‐Energy Cells  Influence of Electrode.pdf#page=3>)
- 在其蒸发通量不高于约 $3~\mathrm{g\,m^{-2}\,s^{-1}}$ 的实验条件下，楔形膜至 512 µm 未见裂纹；6、10、15 的条件出现裂纹。约 6 的条件中裂纹主要出现在干厚约 325 µm 以上。所有这些数值只属于该水系负极。[本地 PDF pp.7–8](<../papers_Yang/Energy Tech - 2019 - Kumberg - Drying of Lithium‐Ion Battery Anodes for Use in High‐Energy Cells  Influence of Electrode.pdf#page=7>)
- 厚度和干燥强度增加都降低黏附；快干样品的 CMC 顶/底信号差异增大。[本地 PDF pp.4–7](<../papers_Yang/Energy Tech - 2019 - Kumberg - Drying of Lithium‐Ion Battery Anodes for Use in High‐Energy Cells  Influence of Electrode.pdf#page=4>)
- 图像分析排除了小于 $0.3~\mathrm{mm^2}$ 的区域，微小起裂可能被漏计。[本地 PDF p.10](<../papers_Yang/Energy Tech - 2019 - Kumberg - Drying of Lithium‐Ion Battery Anodes for Use in High‐Energy Cells  Influence of Electrode.pdf#page=10>)

气侧蒸发式为：

$$
\dot m_S=
\widetilde M_S\widetilde\rho_G\beta_{S,G}
\ln\frac{1-\widetilde y_{S,\infty}}
{1-\widetilde y_{S,Ph}}.
$$

$\dot m_S$ 是面积蒸发质量通量，$\widetilde M_S$ 是溶剂摩尔质量，$\widetilde\rho_G$ 是气体摩尔密度，$\beta_{S,G}$ 是气侧传质系数，两个 $\widetilde y$ 分别是主气流和界面处溶剂摩尔分数。它只适用于界面连续润湿、主要由气侧控制的阶段；进入侵气和液路断连后不能单独闭合内部过程。[本地 PDF p.1](<../papers_Yang/Energy Tech - 2019 - Kumberg - Drying of Lithium‐Ion Battery Anodes for Use in High‐Energy Cells  Influence of Electrode.pdf#page=1>)

**本项目用法：** 把烘箱设定温度改写为实测 $T_s(t)$ 与 $J(t)$；实验因子使用湿厚/面密度×前段通量，而不是照搬 325 µm。

### 3.2 Jaiser et al. 2017：宏观均匀收缩下仍有微观异质孔排空

文献：S. Jaiser et al., *Journal of Power Sources* 345, 97–107，[DOI 10.1016/j.jpowsour.2017.01.117](https://doi.org/10.1016/j.jpowsour.2017.01.117)。

体系为石墨/CB/PVDF/NMP，47.5 wt% 固含，约 114 µm 湿厚、61 µm 干厚，60 mm 宽，约 76.5 °C。

- Cryo-BIB-SEM 没有看到锐利的自上而下颗粒压实前沿；颗粒整体较均匀地接近和压实。[本地 PDF pp.6–7](../papers_Yang/jaiser2017.pdf#page=6)
- 孔排空并不均匀：大孔先空，小孔和表面孔继续含液；还观察到与连续液路断开的孤立液簇和颗粒接触处液桥。[本地 PDF pp.7–9](../papers_Yang/jaiser2017.pdf#page=7)
- EDS 显示 PVDF 液相浓度梯度在明显孔排空及收缩终止前已经形成。梯度是直接观察；“溶剂扩散拖曳自由 PVDF”是作者解释。[本地 PDF p.8](../papers_Yang/jaiser2017.pdf#page=8)

论文把截面状态换算为时间的式子是实验账本：

$$
d_{film}=d_0-\frac{t_{calc}}{t_{EoFS}}(d_0-d_{dry}),
\qquad
t_{calc}=\frac{(X_{NMP,0}-X_{NMP})M_S}{\dot m}.
$$

$d_0$ 和 $d_{dry}$ 为初始湿厚和干厚，$t_{EoFS}$ 为宏观收缩终止时间，$X_{NMP}$ 为 NMP/干固体质量比，$M_S$ 为干面密度，$\dot m$ 为蒸发通量。第一式假设收缩阶段厚度线性变化；它不是通用本构。[本地 PDF p.5](../papers_Yang/jaiser2017.pdf#page=5)

**本项目用法：** 把 E2“宏观收缩平台”、E3“侵气”和 E4“连续液路断开”分别测量；不能用一个失重拐点代替三者。

### 3.3 Zhao et al. 2023：目标化学体系直接，但方程不可原样复制

文献：C. Zhao et al., *Processes* 11, 3236，[DOI 10.3390/pr11113236](https://doi.org/10.3390/pr11113236)。

优点是研究对象直接为 LFP/PVDF/NMP，并建立固–液–气非稳态热质模型；不足是忽略聚合物迁移和力学，且验证主要停留在表面温度。[本地 PDF pp.2–14](../papers_Yang/processes-11-03236.pdf#page=2)

审阅发现四项需要在复用前纠正：

1. 有效导热率式 (23) 把气相项写成 $\lambda_gS_l\varepsilon$；按相体积分数，气相项应依赖气相饱和度 $1-S_l$。原式会让液相和气相同时按 $S_l$ 加权。[本地 PDF p.6](../papers_Yang/processes-11-03236.pdf#page=6)
2. 绝热/对流边界式 (26)、(27) 写成 $\lambda\,\partial T/\partial t$；热通量必须由空间法向梯度 $-\lambda\nabla T\cdot\mathbf n$ 给出，原式量纲不成立。[本地 PDF p.6](../papers_Yang/processes-11-03236.pdf#page=6)
3. 对 $k_g$ 与 $\mu_g$ 的文字定义互换，应分别是气相渗透率与气体动力黏度。[本地 PDF p.5](../papers_Yang/processes-11-03236.pdf#page=5)
4. 体相相变源 $\dot m$ 没有给出足够闭合关系；若直接求解，内部蒸发位置和速率仍不确定。

论文的液相结构可写为：

$$
\frac{\partial(\rho_l\varepsilon S_l)}{\partial t}
+\frac{\partial c_l}{\partial x}
=-\dot m,
$$

$$
c_l=-\rho_l\frac{k_l}{\mu_l}\frac{\partial P_g}{\partial x}
+\rho_l\frac{k_l}{\mu_l}\frac{\partial P_c}{\partial x}.
$$

这里 $\rho_l$ 为液体密度，$\varepsilon$ 为孔隙率，$S_l$ 为液相饱和度，$c_l$ 为液相质量通量，$P_g$、$P_c$ 为气压和毛细压，$k_l$ 为液相渗透率，$\mu_l$ 为液体黏度，$\dot m$ 为体积相变源。方程结构可作起点，但必须重新推导符号、边界和闭合，并再耦合 PVDF/CB 迁移、收缩、应力与失效。

实验验证包括三个样品的表面温度历史，以及单一条件的表面 SEM 和定性划格粘附；没有验证内部 NMP、饱和度、孔压、迁移或裂纹。[本地 PDF pp.11–14](../papers_Yang/processes-11-03236.pdf#page=11)

**本项目用法：** 将其列为“热质模型结构/趋势证据”，证据等级不能因目标材料匹配就自动升高；裂纹窗口必须由新增力学和目标实验验证。

### 3.4 Nikpour et al. 2022：迁移反例与二维取样必要性

文献：M. Nikpour et al., *Batteries* 8, 107，[DOI 10.3390/batteries8090107](https://doi.org/10.3390/batteries8090107)。

NMC532/CB/PVDF 配比 90/5/5，石墨/CB/PVDF 92/2/6，NMP/固体质量比为 1；80 µm 刮刀间隙，NMC 面载约 13 mg cm$^{-2}$；比较 24 °C 长时干燥与 80、150、232 °C 约 10 min 干燥。[本地 PDF pp.9–10](<../papers_Yang/Li-ion Electrode Microstructure Evolution during Drying and Calen.pdf#page=9>)

- 全部条件都有面内 F/PVDF 信号异质；明显厚向梯度主要在 150 °C 以上出现。[本地 PDF pp.13–16](<../papers_Yang/Li-ion Electrode Microstructure Evolution during Drying and Calen.pdf#page=13>)
- 80 °C 样品电子电导最高；高温样品接触电阻和 MacMullin 数增加，辊压降低部分电阻但没有抹去全部干燥历史。[本地 PDF pp.16–24](<../papers_Yang/Li-ion Electrode Microstructure Evolution during Drying and Calen.pdf#page=16>)
- EDS 氟信号受孔隙率、吸收和荧光影响，适合相近样品间的相对比较，不宜直接当 PVDF 绝对浓度。[本地 PDF pp.15–16](<../papers_Yang/Li-ion Electrode Microstructure Evolution during Drying and Calen.pdf#page=15>)
- 论文没有系统裂纹指标；可见裂纹只是高温电导下降的多个候选解释之一。[本地 PDF p.16](<../papers_Yang/Li-ion Electrode Microstructure Evolution during Drying and Calen.pdf#page=16>)

**本项目用法：** 宽 20 cm 极片不能只做中心线顶/底 EDS；至少需要横幅位置×厚度位置二维分层取样。

### 3.5 Morrison et al. 2026：裂纹的功能具有倍率和深度窗口

文献：A. R. T. Morrison et al., *EES Batteries* 2, 911–923，[DOI 10.1039/D6EB00017G](https://doi.org/10.1039/D6EB00017G)。

研究使用 87:8:5 的 NMC622/CB/PVDF、40 wt% 固含、80 °C 热板制得预先开裂的厚电极。主样约 195 µm 干厚、55% 孔隙率、32 mg cm$^{-2}$，目标裂纹约 1.3 mm 长、50 µm 宽。[本地 PDF pp.3–5](../papers_Yang/d6eb00017g.pdf#page=3)

operando MCC-XRD 的直接量是 NMC 晶胞参数及据此估算的局部嵌锂状态，不是电解液 $[\mathrm{Li}^+]$。中层和集流体附近，裂纹附近区域放电时嵌锂更快；顶部横向差异较小。0.8C、0.5C 的底层近裂/体相 SoL 差约 4.5%、7.3%，而厚向约 110 µm 的差可达约 27.3%。[本地 PDF pp.7–10](../papers_Yang/d6eb00017g.pdf#page=7)

只有两片被挑选的电极，重点展示一条长而直的孤立裂纹；测量体积沿光束方向还会平均约毫米尺度。因此该研究支持机制存在性，不给裂纹几何的总体效应量。

**本项目用法：** 单独建立“裂纹形成模型”和“裂后功能模型”；不要因为裂纹有时改善离子通路，就把干燥开裂视为可接受的结构设计。

## 4. 胶体、陶瓷、聚合物和凝胶论文逐篇解读

### 4.1 Cardinal et al. 2010：$Pe$–沉降竞争图

文献：C. M. Cardinal et al., *AIChE Journal*，[DOI 10.1002/aic.12190](https://doi.org/10.1002/aic.12190)。

$$
Pe=\frac{EH_0}{D_0},
\qquad
D_0=\frac{k_BT}{6\pi\eta R},
$$

$$
N_s=\frac{U_0}{E},
\qquad
U_0=\frac{2R^2g(\rho_p-\rho_l)}{9\eta}.
$$

$E$ 是自由表面下降速度，$H_0$ 是初始湿厚，$D_0$ 是稀释极限 Brownian 扩散率，$R$ 是单分散颗粒半径，$\eta$ 是液体黏度，$U_0$ 是 Stokes 沉降速度。[本地 PDF pp.2–3](../papers_Yang/cardinal2010.pdf#page=2)

高 $Pe$ 倾向表面富集，低 $Pe$ 倾向扩散均化，高 $N_s$ 倾向底部沉降；表面富集和底部沉降可以同时发生，cryo-SEM 提供了源体系验证。[本地 PDF pp.8–10](../papers_Yang/cardinal2010.pdf#page=8)

关键术语边界：论文中的 “skin” 只是超过浓度阈值的表面颗粒富集层；模型没有加入其对蒸发率、渗透率或流变的反馈。[本地 PDF p.6](../papers_Yang/cardinal2010.pdf#page=6) 因此它不等于本项目要求有持续低渗/高模量证据的 **Skin+**。

### 4.2 Tirumkudulu & Russel 2005：一般能量结构与特殊 $H^{-2/3}$ 指数

文献：M. S. Tirumkudulu and W. B. Russel, *Langmuir*，[DOI 10.1021/la048298k](https://doi.org/10.1021/la048298k)。

$$
G_I=\frac12\frac{\sigma_0^2h}{\bar E_f}\pi g(\alpha,\beta).
$$

$G_I$ 是 I 型能量释放率，$\sigma_0$ 是受限收缩应力，$h$ 是膜厚，$\bar E_f$ 是膜的平面应变模量，$g(\alpha,\beta)$ 是由膜–基底弹性失配决定的无量纲函数。[本地 PDF p.6](../papers_Yang/tirumkudulu2005.pdf#page=6)

该一般结构与本项目 $G=C\sigma^2H/E'$ 一致。论文后续得到的 $\sigma_c\propto H^{-2/3}$、裂纹间距和数值系数来自特定湿乳胶颗粒的非线性本构；实测临界应力绝对值约为模型的三倍，只有趋势较一致。[本地 PDF pp.9–11](../papers_Yang/tirumkudulu2005.pdf#page=9)

**本项目用法：** 迁移能量结构，不迁移 $-2/3$ 指数、系数或水–空气界面能。

### 4.3 Moorhead & Francis 2024：同步测应力比只看最终裂纹更有信息

文献：S. Moorhead and L. F. Francis, *Journal of the American Ceramic Society*，[DOI 10.1111/jace.19644](https://doi.org/10.1111/jace.19644)。

陶瓷涂层经历无应力悬浮期、颗粒锁定后应力上升、峰值、随后孔内弯月面退缩和应力下降；ZnO 源体系的 CCT 约 53 µm。较厚样在峰值附近开裂，先快速卸载，再出现较慢的排液相关下降。[本地 PDF pp.5–6、9–11](<../papers_Yang/Journal of the American Ceramic Society - 2024 - Moorhead - Characterizing stress development and cracking of ceramic.pdf#page=5>)；[DOI 10.1111/jace.19644](https://doi.org/10.1111/jace.19644)

最重要的修正是：悬臂梁曲率反演假定涂层连续。起裂后的快速应力下降本身是裂纹指纹和比较量，不能继续当成“完整连续膜的绝对应力”。相近峰值应力也不保证相同开裂结果，因为厚度改变可释放能量。

**本项目用法：** 若做铝箔曲率/应力实验，将峰值前数据用于应力反演，峰值后数据用于事件识别；同时用成像确认裂纹何时破坏连续膜假设。

### 4.4 Arai & Doi 2012：皮层、压力与已有气泡增长

文献：M. Arai and M. Doi, *European Physical Journal E*，[DOI 10.1140/epje/i2012-12057-2](https://doi.org/10.1140/epje/i2012-12057-2)。

降低蒸发速度时，源体系未观察到结皮或气泡；有结皮也不保证一定产生气泡。结皮受容器壁约束并下凹，可降低皮下液体压力。[本地 PDF pp.3–6](<../papers_Yang/Arai 2012, Skin formation and bubble growth during drying processof polymer solution.pdf#page=3>)

论文的皮层降压尺度为：

$$
\Delta P\simeq E\frac{h}{L}
\left(\frac dL\right)^2\sin\theta,
$$

其中 $E$ 是皮层模量，$h$ 是皮层厚度，$L$ 是容器半径，$d$ 是下凹量，$\theta$ 是边缘角。已有气泡的扩散控制增长式为：

$$
R=
\left[
\frac{2(c_0-c_R)D_p}{\rho_g}(t-\tau)
\right]^{1/2}.
$$

$R$ 为泡半径，$c_0$ 与 $c_R$ 为远场和泡界面溶解气浓度，$D_p$ 为有效扩散系数，$\rho_g$ 为泡内气体密度，$\tau$ 为诱导时间。[本地 PDF pp.5–7](<../papers_Yang/Arai 2012, Skin formation and bubble growth during drying processof polymer solution.pdf#page=5>)

必须纠正两种常见误读：

- 泡内“丙酮蒸气+溶解空气”是测压、Henry 定律和模型拟合的一致性推断，论文没有直接分析泡内气体成分，并把成分测量列为未来工作。[本地 PDF p.7](<../papers_Yang/Arai 2012, Skin formation and bubble growth during drying processof polymer solution.pdf#page=7>)
- 正文式和数据支持 $R\propto\sqrt{t-\tau}$；结论段“半径随时间平方增长”的表述与式 (8) 不一致，不能沿用。

**本项目用法：** 将它视为 D3/D5 的候选机制和实验设计启发；不把丙酮–聚合物的压力、模量、时间或气体组成搬到 NMP/PVDF。

### 4.5 Bertrand et al. 2016：孔弹性压力均化与外层先干

文献：T. Bertrand et al., *Physical Review Applied* 6, 064010，[DOI 10.1103/PhysRevApplied.6.064010](https://doi.org/10.1103/PhysRevApplied.6.064010)。

球形凝胶模型预测外层先失水、外壳环向受拉、湿核心受压；提高外部蒸发能力会增加含液梯度和最大环向有效应力。[本地 PDF pp.8–11](../papers_Yang/1605.00599v3.pdf#page=8)

$$
\sigma_i=\sigma_i'-p,
\qquad
\phi_f(v_f-v_s)
=-\frac{k(\phi_f)}{\eta}
\nabla\left(\frac{\mu_f}{\Omega_f}\right),
$$

$$
\tau=\frac{\eta a_d^2\Omega_p}{k_0k_BT}.
$$

前两式分别表示总应力分解和化学势驱动的液–骨架相对运动；$\tau$ 是随干燥尺度 $a_d^2$ 增长的孔弹性时间。[本地 PDF pp.2–4](../papers_Yang/1605.00599v3.pdf#page=2)

论文直接测的是球体宏观半径等量，内部压力、孔隙率和应力主要来自模型预测。自由球形、交联水凝胶、大可逆形变和水体系参数不能迁移到受铝箔约束的 LFP。

## 5. 岩土论文逐篇解读

### 5.1 Tang et al. 2021：三类裂纹判据应并列，而非强行合一

文献：C. S. Tang et al., *Earth-Science Reviews* 216, 103586，[DOI 10.1016/j.earscirev.2021.103586](https://doi.org/10.1016/j.earscirev.2021.103586)。

该综述把模型分成能量、应力/强度和体积收缩三类：

$$
\delta U\ge\delta U_{SE},
\qquad
\sigma_h\ge\sigma_t,
$$

$$
dU=dw_{el}+dw_{pl}+d\Gamma.
$$

$w_{el}$ 是可恢复弹性能，$w_{pl}$ 是塑性耗散，$\Gamma$ 是新增裂面能。[本地 PDF pp.12–15](../papers_Yang/tang2021.pdf#page=12)

综述还归纳出：某些土体可在仍接近饱和时开裂，空气侵入不是所有材料起裂的必要前提；缺陷、边界约束和吸力共同决定位置。[本地 PDF pp.19–21](../papers_Yang/tang2021.pdf#page=19) 这是综述级证据，若要用具体阈值必须回溯其原始论文。

**本项目用法：** 同时保留局部强度、能量传播和塑性/黏弹耗散；不把土体吸力阈值赋给电极。

### 5.2 Zeng et al. 2019：厚度与底面摩擦耦合

文献：H. Zeng et al., *Engineering Geology* 265, 105220，[DOI 10.1016/j.enggeo.2019.105220](https://doi.org/10.1016/j.enggeo.2019.105220)。

Xiashu 黏土实验组合 0.5、1.0、1.5 cm 厚度与三种底面摩擦。粗糙底面通常产生更多裂段和节点；厚层裂纹数量较少，但单条更长、更宽。界面影响与厚度耦合，而非简单相加。[本地 PDF pp.12–16、20–24](../papers_Yang/zeng2019.pdf#page=12)

简化受力关系：

$$
\sigma=\frac{f(\mu)L}{d},
\qquad
\sigma_{cr}=\frac{f(\mu)L_{cr}}d,
$$

$f(\mu)$ 为界面剪应力，$L$ 为土块接触长度，$d$ 为层厚。[本地 PDF pp.20–21](../papers_Yang/zeng2019.pdf#page=20)

该论文的裂隙面积指标会把边缘整体脱离计入裂隙；某些光滑底面样品内部没有裂纹，却因边缘收缩得到较大指标。这直接支持本项目将内部裂纹、边缘收缩和界面脱层分开统计。

## 6. 排除文献：Wang et al. 2026

Wang et al., *Nature Energy*，[DOI 10.1038/s41560-026-02087-6](https://doi.org/10.1038/s41560-026-02087-6)，研究的是 NMC811/石墨软包在数百次循环中的堆叠压力、活性颗粒破裂、析锂和寿命。[本地 PDF](../papers_Yang/s41560-026-02087-6.pdf)

其 “cathode cracking” 是运行期一次/二次活性颗粒机械破裂，不是涂布干燥阶段的 D1 通道裂纹、D2 层内开裂、D3 空洞或 D4 脱层。因此不进入当前核心证据矩阵，只在排除日志中保留，防止关键词检索造成同词异义污染。

## 7. 由本批文献产生的模型决策

### 7.1 可以保留

- 以实测膜温与蒸发通量驱动热质模型；
- 以 E2 收缩平台、E3 侵气、E4 液路断连、多个 E5 失效事件描述状态序列；
- 用 $Pe$ 和沉降比做迁移的第一层排序；
- 用 Darcy/孔弹性处理液体–骨架相对运动；
- 用 $G=C\sigma^2H/E'$ 与强度门槛并列处理失效；
- 为预存气泡、皮层下空洞、表面通道裂纹和脱层建立竞争分支；
- 把横幅位置与厚度位置同时作为采样坐标。

### 7.2 必须删去或降级

- 不把 Zhao 2023 的原始边界条件和有效导热式直接复制进模型；
- 不把 Cardinal 的表面浓度层自动称为低渗/高模量 **Skin+**；
- 不把 Arai 的泡内气体组成写成直接测量；
- 不把 Tirumkudulu 的 $H^{-2/3}$ 当普适指数；
- 不把 Moorhead 起裂后的曲率继续反演成连续膜绝对应力；
- 不把 Dawson/Kumberg 的临界厚度、时间或蒸发通量数值转给 LFP；
- 不用 CIF 单值混合通道裂纹、气泡和脱层；
- 不用运行期颗粒裂纹文献解释干燥开裂。

## 8. 推荐阅读顺序

如果只读五项：

1. Dawson 学位论文第 5 章：形成事件链；
2. Dawson et al. 2026：DVC 与气泡事件修正；
3. Jaiser et al. 2017：孔排空和液路断连的真实截面；
4. Kumberg et al. 2019：厚度×通量×裂纹的电池实验；
5. Moorhead & Francis 2024：同步应力–干燥–起裂。

第二层再读：Arai & Doi 用于内部空洞候选机制，Cardinal 用于迁移竞争，Tirumkudulu 用于断裂能结构，Bertrand 用于孔压均化，Tang/Zeng 用于约束与机制分类，Nikpour 用于“PVDF 必然上浮”的反例。Zhao 适合在重新推导方程时作为对照，而不适合当模板。
