# 核心文献原文与中文导读说明

本目录为研究报告配套的核心文献入口。专题报告及 [`基础知识体系`](../00_basic_knowledge_framework.md) 末尾列出 2–3 篇最值得优先阅读的论文，并提供简短中文导读。导读按照 `paper-translation` 工作规范编写，但**不是全文翻译**；它保留论文对象、方法、主要结论和迁移边界，帮助决定下一步应全文翻译哪几篇。

## 原文状态标记

- **本地 PDF**：已保存开放版本、作者接受稿或预印本，并检查页数及抽样渲染；可离线阅读。
- **开放原文**：链接到出版社、作者主页或机构仓储的合法全文；是否能直接下载取决于网站策略。
- **DOI / 出版社原文**：稳定的正式版本入口，可能需要机构订阅。没有把非授权副本当作本地原文保存。

## 已离线保存并检查的原文

| 文献 | 文件 | 版本与检查结果 |
|---|---|---|
| Font et al. (2018), binder migration model | [`BAT06_Font_2018_binder_migration_model_preprint.pdf`](originals/BAT06_Font_2018_binder_migration_model_preprint.pdf) | arXiv 预印本，25 页；标题页和模型正文已抽样渲染 |
| Susarla et al. (2018), solvent removal model | [`BAT12_Susarla_2018_solvent_removal_author_manuscript.pdf`](originals/BAT12_Susarla_2018_solvent_removal_author_manuscript.pdf) | OSTI 作者稿，36 页；摘要和模型背景已抽样渲染 |
| Román-Ramírez et al. (2021), pilot coating–drying DOE | [`BAT13_Roman_Ramirez_2021_pilot_coating_drying_accepted.pdf`](originals/BAT13_Roman_Ramirez_2021_pilot_coating_drying_accepted.pdf) | Warwick 作者接受稿，43 页，CC BY-NC-ND 4.0；封面和正文已抽样渲染 |
| Goehring et al. (2013), plasticity and fracture | [`COL07_Goehring_2013_plasticity_fracture_repository.pdf`](originals/COL07_Goehring_2013_plasticity_fracture_repository.pdf) | NTU 机构仓储版，5 页；标题页、裂纹图像和能量方程页已抽样渲染 |

全部 26 篇核心文献的报告归属、DOI、原文入口、离线文件和访问状态见 [`core_literature_manifest.csv`](core_literature_manifest.csv)；其中报告代码 `K00` 表示 [`基础知识体系`](../00_basic_knowledge_framework.md)。

## papers_Yang 本地文献包

用户补充的 17 个原始 PDF 保存在本地工作区 [`papers_Yang`](../../papers_Yang/)，但按发布约束不上传 GitHub。解读文档中的相对 PDF 链接和 `#page=` 页码锚点继续作为本地证据定位；GitHub 读者可使用相邻 DOI、出版社或机构仓储链接获取可公开访问的原文。该文献包对应 15 项文献身份：两份 Dawson D5EB00201J 是同一论文的不同封装，两份 Moorhead 2024 是 SHA-256 完全相同的副本。文件原样保留在本地以避免破坏用户资料目录，来源登记和证据计数均去重。

- [`Dawson 学位论文及关联论文深读`](../12_dawson_thesis_deep_read.md)：形成、性能、模型负结果和后续局部 XRD 的证据链。
- [`papers_Yang 逐篇解读`](../14_papers_yang_reading_notes.md)：其余电池、胶体、陶瓷、聚合物、凝胶和岩土论文的页码级核验。
- [`公式与物理量详解`](../13_formula_and_symbol_guide.md)：所有原有公式的变量、单位、测量方式和适用边界。

其中 Wang et al. 2026 研究循环期活性颗粒破裂，因 “cracking” 同词异义而不进入干燥开裂核心证据矩阵。

## 本项目统一术语

| English | 本项目译法 |
|---|---|
| binder / binder migration | 粘结剂 / 粘结剂迁移 |
| current collector | 集流体 |
| wet film / coating | 湿膜 / 涂层；工艺动作译为涂布 |
| solid content | 固含量 |
| surface evaporation | 表面蒸发 |
| capillary pressure / capillary pumping | 毛细压力 / 毛细泵吸 |
| skin / crusting | 表面皮层 / 结皮 |
| delamination | 脱层或界面脱粘 |
| critical cracking thickness, CCT | 临界开裂厚度，CCT |
| drying stress / stress relaxation | 干燥应力 / 应力松弛 |

## 阅读原则

1. 先读论文研究的具体材料、厚度、溶剂和边界条件，再读结论。
2. 把直接观察、作者模型和本项目跨领域迁移分开。
3. 公式结构可以迁移，经验参数和临界阈值原则上不能直接迁移到商用 LFP–PVDF/NMP。
4. 如果后续做全文翻译，应优先选择目标体系最接近、对模型方程或实验判别最关键的论文，而不是单纯按引用量排序。
