# LFP–PVDF/NMP 厚涂极片干燥失效：结构化范围综述协议

## 1. 研究问题

本综述回答以下问题：

1. LFP–PVDF/NMP 湿膜从入炉到出炉及短时冷却期间，经历哪些热、质、组分、结构与力学过程？
2. 表面泥裂、内部裂纹、异常宏孔、界面脱粘、表面致密层及表面起伏分别可由哪些竞争机制产生？
3. 厚度/涂布量、固含量、粒径/团聚尺度、线速度和烘箱条件通过哪些中间物理量改变失效风险？
4. 锂电电极、胶体膜、陶瓷流延、聚合物涂层、凝胶、岩土干缩及烘焙/淀粉颗粒体的哪些模型或实验逻辑可以迁移，需要修改哪些假设？

## 2. 因果时间窗口与缺陷边界

- 主时间窗口：入炉、分区干燥、出炉及短时冷却。
- 混料、脱气、涂布和流平仅作为初始条件与非干燥零假设。
- 牵引、收卷和辊压作为替代解释，不进入主模型。
- 纳入：表面连通泥裂、非表面连通内裂、涂层–铝箔脱粘、明显大于背景孔隙的异常宏孔、表面致密/凝胶/富集层、表面粗糙/皱缩/鼓泡。
- 排除：正常微孔与 LFP 颗粒原生内孔。

## 3. 数据源

学术来源优先：Web of Science/Scopus 等索引的同行评议论文，通过 Crossref/DOI 和出版商页面核对元数据。网络搜索用于发现开放全文、机构存储库副本和前后向引文。专利、厂商和工业资料仅用于补充设备结构、量产边界与术语，不用来单独证明核心机理。

## 4. 检索模块

| 编号 | 主题 | 核心检索块（按数据库语法调整） |
|---|---|---|
| M1 | 目标/邻近电极 | `(LFP OR LiFePO4 OR cathode) AND (PVDF AND NMP) AND drying AND (crack* OR void* OR blister* OR skin* OR rough*)` |
| M2 | 热质传递 | `battery electrode drying AND (heat mass transfer OR evaporation flux OR falling-rate OR multi-zone OR web speed) AND model` |
| M3 | 组分迁移 | `battery electrode AND (binder migration OR carbon-binder migration OR sedimentation OR solidification OR pore emptying)` |
| M4 | 泥裂/临界厚度 | `(battery electrode OR colloidal film OR ceramic tape) AND (critical cracking thickness OR channel crack OR capillary stress OR constrained shrinkage)` |
| M5 | 结皮/表面形貌 | `drying film AND (skin formation OR gel front OR Marangoni OR wrinkling OR buckling OR surface roughness)` |
| M6 | 宏孔/内裂 | `drying film AND (internal void OR cavity OR cavitation OR trapped solvent OR bubble growth OR solvent popping OR blister)` |
| M7 | 岩土/凝胶 | `desiccation crack AND (Richards OR poroelastic OR cohesive OR phase field)`; `gel drying AND (Darcy OR pressure gradient OR fracture OR cavitation)` |
| M8 | 工业尺度 | `roll-to-roll electrode drying AND (cross-web uniformity OR impingement nozzle OR scale-up OR solvent load)` |
| M9 | 时间分辨观测 | `battery electrode drying AND (in situ OR operando OR radiography OR ultrasound OR gravimetry OR film temperature) AND (locking OR pore emptying OR crack*)` |
| M10 | 烘焙/颗粒食品类比 | `(bread crust crumb moving evaporation front) OR (biscuit checking moisture gradient) OR (starch slurry drying crack liquid vapor transport)` |

## 5. 纳入、排除与停止规则

### 纳入

- 直接研究电极干燥、颗粒/聚合物湿膜干燥、非饱和多孔介质干缩或凝胶脱溶剂断裂。
- 提供直接观察、定量关系、模型方程、尺度判据或权威分类。
- 可明确识别材料、边界条件和研究尺度。

### 排除

- 只讨论循环中活性颗粒破裂，与制造干燥无关。
- 无法核验的营销性内容、无出处二手图表或抄录文。
- 仅有最终形貌但无法识别干燥阶段或初始条件，且不能提供机制判别价值。

### 停止

一个模块在完成代表性综述的前后向追踪，并连续两轮定向检索未出现新模型族、新状态转换或新竞争机制时停止。

## 6. 证据等级与引用规则

| 等级 | 含义 |
|---|---|
| A | LFP–PVDF/NMP 直接证据 |
| B | 其他 PVDF/NMP 正极 |
| C | 其他锂电电极 |
| D1 | 陶瓷流延/颗粒涂层 |
| D2 | 胶体膜/聚合物涂层 |
| D3 | 凝胶/孔弹性材料 |
| D4 | 岩土干缩 |
| I | 专利/工业资料 |
| T | 纯理论 |

每个外部主张必须在紧邻位置给出引用键与 DOI/稳定链接，并标注证据性质：直接观察、实验相关、模型反演、理论推导、作者推测或本项目推论。无法获得全文的文献标记为“仅摘要”，不用于支撑方程细节。

## 7. 数据提取与质量审计

- 证据矩阵以“单条机制主张”为行，而不是以论文为行。
- 方程必须记录原始文献、方程号/页码（可获得时）、符号定义和原始假设。
- 关键模型至少追溯一篇原始论文；综述用于定位、分类和发现引文。
- 评审时逐条核对 DOI–题名–作者、引用覆盖、推论标记和跨领域外推。
- 对烘焙类比，来源中的食品数值只证明其源体系现象；所有面向 LFP 的结论必须标为迁移假设，并显式列出禁止迁移的物性、相变、几何和时间尺度。
- 对 E0–E6 事件，E5“首次不可逆失效”作为横切事件记录，并带 D1–D5 缺陷代码；不把编号误写为必然发生顺序。
