# LFP–PVDF/NMP 厚涂极片干燥失效：研究文档库

本目录收录结构化范围综述、分领域专题报告、证据矩阵、模型卡、变量字典和目标体系综合机制图。

## 研究项目状态

| 阶段 | 研究决策 | 状态 |
|---|---|---|
| 0. 问题界定 | 定义 D1–D5 开裂类缺陷、因果时间窗和 H0–H10 竞争假设 | 已完成 |
| 1. 证据地形 | 追踪电池、胶体、陶瓷、聚合物、凝胶、岩土、设备与烘焙类比的证据、反例和迁移边界 | 首轮完成；各领域完整物理过程已做首轮深挖 |
| 2. 目标体系判别 | 用 27 个主样+中断样+脱气对照定位锁定–侵气–失效时序 | 待执行 |
| 3. 参数辨识 | 按设备、状态、迁移、孔结构、力学、失效的顺序校准 | 等待阶段 2 数据 |
| 4. 工艺窗口 | 外部验证、不确定度量化和跨批次/跨设备检验 | 未开始 |

因此，当前交付的是“已经证据审计的机制架构+可证伪实验计划”，而不是未经校准的数值工艺窗口。

## 文件导航

- [`00_basic_knowledge_framework.md`](00_basic_knowledge_framework.md)：从零建立“设备边界—材料状态—应力—失效”的基础知识体系与学习路径。
- [`00_main_report.md`](00_main_report.md)：综合结论、证据边界和研究决策。
- [`10_physical_process_learning_guide.md`](10_physical_process_learning_guide.md)：用费曼式白话、苏格拉底追问和反证问题学习完整干燥过程；建议新读者从这里开始。
- [`01_battery_electrode.md`](01_battery_electrode.md)：沿 E0–E6 深入锂电电极的热质、迁移、锁定、侵气、应力和 D1–D5 竞争失效。
- [`11_baking_analogy.md`](11_baking_analogy.md)：面包外壳、饼干延迟 checking 与未糊化淀粉浆的类比故事、严格证据和禁用边界。
- [`02_geotechnical_desiccation.md`](02_geotechnical_desiccation.md)：岩土非饱和输运与干缩断裂。
- [`03_gel_poroelastic_fracture.md`](03_gel_poroelastic_fracture.md)：凝胶孔弹性、空化与断裂。
- [`04_colloidal_films.md`](04_colloidal_films.md)：胶体膜、毛细应力与临界厚度。
- [`05_ceramic_tape_casting.md`](05_ceramic_tape_casting.md)：陶瓷流延与同步干燥应力。
- [`06_polymer_coatings.md`](06_polymer_coatings.md)：结皮、气泡、宏孔和表面起伏。
- [`07_roll_to_roll_drying.md`](07_roll_to_roll_drying.md)：宽幅连续干燥和设备映射。
- [`08_cross_domain_synthesis.md`](08_cross_domain_synthesis.md)：缺陷本体、迁移矩阵和竞争假设。
- [`09_modeling_framework_and_experimental_program.md`](09_modeling_framework_and_experimental_program.md)：方程层级、参数辨识和第一轮实验。
- [`12_dawson_thesis_deep_read.md`](12_dawson_thesis_deep_read.md)：Dawson 学位论文、第 5 章后续期刊版和裂后局部 XRD 的页码级深读。
- [`13_formula_and_symbol_guide.md`](13_formula_and_symbol_guide.md)：全库原有 66 个行间公式的变量、单位、测量方法、量纲和适用边界，以及 Dawson 专属公式。
- [`14_papers_yang_reading_notes.md`](14_papers_yang_reading_notes.md)：papers_Yang 中 17 个 PDF 的去重、逐篇解读、公式纠错和证据审计。
- [`15_1d_thickness_stress_demonstrator.md`](15_1d_thickness_stress_demonstrator.md)：把 NMP 输运、连续锁定、受限自由收缩、变模量 Maxwell 应力和通道裂纹结构代理耦合成可复现的一维厚向机制演示。
- [`16_kumberg_2019_full_translation_zh.md`](16_kumberg_2019_full_translation_zh.md)：Kumberg 2019 的完整中文翻译，保留公式、表格、图注、参考文献和逐页来源，并显式标出原文排印/量纲问题。
- [`17_kumberg_2019_terminology.md`](17_kumberg_2019_terminology.md)：该文专有名词、易误译概念和公式符号中英对照；重点区分蒸发通量与线速度、CCT 与裂纹深度、粘附力与断裂能。
- [`18_kumberg_2019_deep_read.md`](18_kumberg_2019_deep_read.md)：逐图、逐表、逐公式证据审计，含实验重建、原文内部矛盾、右删失、LFP/PVDF–NMP 迁移边界和当前模型参数可辨识性。
- [`19_schabel_thick_coating_cracking_map.md`](19_schabel_thick_coating_cracking_map.md)：将 Schabel 2011–2026 年锂电干燥工作按“直接开裂证据—失效前状态—候选干预—设备放大”分级，另将三项燃料电池催化层直接开裂研究单列为跨体系旁证，并映射到本项目 E0–E6、D1–D5、H1/H5/H6/H9/H10 与实验计划。
- [`20_capillary_gradient_constraint_and_interfacial_shear.md`](20_capillary_gradient_constraint_and_interfacial_shear.md)：以六面板机制图呈现毛细加载—自由收缩—约束应力—载荷传递—裂纹储能主线，把详细推导放入正文；并用“自由膜 100→97、约束膜保持近 100”的反事实严格解释应力符号、涂层–铝箔受力平衡，以及厚向梯度、弯曲倾向与界面剪切的区别。
- [`21_dawson_thesis_chapter5_full_translation_zh.md`](21_dawson_thesis_chapter5_full_translation_zh.md)：Dawson 2025 博士论文第 5 章完整中文翻译，覆盖 PDF pp.117–141 的全部正文、方法、结果、结论、贡献说明、表 5.4、图 5.33–5.41 图注及图内文字对照，并保留逐页来源与原引用编号。
- [`22_fixed_thickness_cracking_reduction_parameter_map.md`](22_fixed_thickness_cracking_reduction_parameter_map.md)：在固定目标干厚度/面密度下，用同一块厚极片的四阶段剖面图说明“湿膜—受约束收缩—厚向状态不同步—D1–D5 竞争失效”，再将设备轨迹、横幅均匀性、气泡/团聚、固含–流变–孔网、PVDF/CBD 湿态力学及界面参数映射到加载、松弛和断裂抗力；原参数流程图保留为内部技术补充。
- [`23_staged_experimental_program_for_cracking_model_identification.md`](23_staged_experimental_program_for_cracking_model_identification.md)：从临界厚度概率曲线、蒸发与气泡支路筛选、中断样时序定位到材料参数标定的分阶段验证方案。
- [`24_external_report_cracking_control_model_and_validation.md`](24_external_report_cracking_control_model_and_validation.md)：面向外部技术讨论的厚极片开裂控制、模型结构和验证路径综合报告。
- [`25_1d_drying_stress_model_independent_output_report.md`](25_1d_drying_stress_model_independent_output_report.md)：一维 NMP 输运—机械锁定—自由收缩—Maxwell 应力—通道裂纹风险计算的独立输出版；完整定义每个物理量、代码变量和 CSV 字段，说明直接测量、专门测试与联合反演边界，并逐场景、逐时间点解释最终计算结果。
- [`images/README.md`](images/README.md)：多孔介质示意图、E0–E6 状态时间轴、缺陷判别图和烘焙类比图索引。
- [`literature/README.md`](literature/README.md)：各报告核心文献原文入口、离线 PDF 与中文导读说明。
- [`evidence_matrix.csv`](evidence_matrix.csv)：以机制主张为行的证据矩阵。
- [`source_registry.csv`](source_registry.csv)：来源元数据与 DOI 登记表。
- [`experimental_data_template.csv`](experimental_data_template.csv)：后续实验数据字段模板。
- [`experimental_data_dictionary.md`](experimental_data_dictionary.md)：一行数据的粒度、E0–E6、`Skin+`、D1–D5、残余 NMP 与缺失值编码规则。
- [`search_log.md`](search_log.md)：实际检索与饱和度记录。

## 引用标记

正文使用“作者年 + DOI 或稳定链接”紧邻引用。重要主张同时标注证据性质与证据等级；项目自身的综合判断使用“本项目推论”标签。当前登记 100 个来源、82 条主张级证据；papers_Yang 的重复 PDF 不重复计证据，循环期颗粒破裂论文因同词异义而排除；食品/烘焙及燃料电池催化层来源仅用于迁移问题、方程/因果结构与实验逻辑，不用于 LFP 参数赋值。
