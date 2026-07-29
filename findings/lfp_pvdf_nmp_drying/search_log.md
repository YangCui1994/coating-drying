# 检索与引用审计日志

> 检索截止：2026-07-23（Asia/Shanghai）。  
> 执行方式：结构化范围综述，以机理饱和而不是文献数量为停止条件。  
> 协议：[`search_protocol.md`](../../research_briefs/lfp_pvdf_nmp_drying/search_protocol.md)。

## 1. 实际使用的数据通道

- 普通网络检索：用于发现种子论文、开放全文、机构存储页及出版商页面。
- Crossref API 与 DOI 解析：逐条核对 DOI–作者–题名–期刊–年份。
- 出版商/期刊原始页面：RSC、Wiley、Elsevier、APS、Springer、MDPI、Taylor & Francis 等。
- 机构元数据：仅在书章页码或 Crossref 粒度不足时补充；不用来代替核心原始证据。

本轮没有直接导出 Web of Science/Scopus 的授权索引结果，因此不声称 PRISMA 式全面穷尽。结论的边界是“在本轮可核验公开文献中”，而不是“全球不存在其他研究”。

## 2. 分模块执行记录

### M1：LFP–PVDF/NMP 目标体系

- 核心查询：`LFP PVDF NMP electrode drying crack`; `LiFePO4 thick electrode drying residence time cracking`; `LFP cathode drying internal void blister skin`; 加入 `commercial`, `roll-to-roll`, `20 cm`, `multi-zone`, `in situ CT` 的组合变体。
- 直接命中：Zhao et al. (2023) 是 LFP–PVDF/NMP 热质模型，但不含迁移、力学、空洞或断裂；Liu & Deng (2026) 讨论 LFP 厚度/温度/停留时间，本轮仅获得摘要。
- 近邻直接证据：Dawson et al. (2026) 的 NMC622–PVDF/NMP 原位 CT；Kumano et al. (2024)、Zhang et al. (2022)、Klemens et al. (2022) 的 PVDF/NMP 正极迁移/微结构。
- 纳排结果：没有找到同时满足“商用型 LFP 配方 + PVDF/NMP + 约 20 cm 宽幅 + 厚涂 + 分区强制对流 + 内裂/空洞原位”的公开来源。
- 饱和判断：**未饱和**。这是需要由目标体系实验填补的核心缺口。

### M2–M3：电极热质传递、固结、孔隙排空与组分迁移

- 核心查询：`battery electrode drying pore emptying falling rate`; `binder migration drying rate switch`; `PVDF conductive agent migration cathode drying`; `electrode dryer heat transfer coefficient IR gravimetry`; `multi-zone electrode solvent removal model` 。
- 种子引文网：Jaiser 2016 → Jaiser 2017 Cryo-BIB-SEM/表面液体 → Kumberg 2019 厚度/裂纹 → Kumberg 2020/2021 干燥边界；Font 2018 作为迁移模型锚点；Susarla 2018 作为热质与多区锚点。
- 冲突专门保留：Jaiser/Kumano 支持高干燥强度下粘结剂表面富集；Zhang 2022 对 F 富集梯度的温度敏感性给出反例。
- 饱和判断：一般“收缩—锁定—毛细供液—侵气/断连”状态主干接近**机理饱和**；LFP 中 PVDF/炭黑迁移的方向与强度**未饱和**。

### M4：胶体膜、颗粒涂层与临界开裂厚度

- 核心查询：`drying colloidal film critical cracking thickness capillary stress`; `direct critical stress colloid film`; `particle size fracture toughness drying film`; `ceramic particulate coating simultaneous stress cracking saturation` 。
- 种子引文网：Tirumkudulu & Russel 2005、Singh & Tirumkudulu 2007、Man & Russel 2008、Goehring et al. 2013、Birk-Braun et al. 2017；陶瓷线以 Chiu et al. 1993 系列、Lewis et al. 1996、Martinez & Lewis 2002、Moorhead & Francis 2024 为锚点。
- 修正性证据：纯弹性 CCT 不足以包含缺陷、塑性/黏弹耗散和界面滑移；颗粒尺度对开裂应力与对断裂韧度的影响不能合并为一个普适符号。
- 饱和判断：CCT/能量标度与实验方法达到第一阶段**机理饱和**；目标 LFP 的 $E'(c),\tau_r(c),\Gamma_c(c)$ 与缺陷分布仍未知。

### M5–M6：结皮、表面凹凸、气泡、空化与层内断裂

- 核心查询：`polymer coating skin formation bubble growth pressure`; `dissolved gas supersaturation drying polymer film degassing`; `solvent blister drying film model`; `drying-induced cavitation constrained gel`; `Marangoni corrugation drying polymer solution`; `skin wrinkling drying coating` 。
- 种子引文网：Arai & Doi 2012、Pourdarvish et al. 2008/2009、Punati & Tirumkudulu 2022、Price & Cairncross 1999、Yiantsios et al. 2015；空化线以 Scherer & Smith 1995 和 Wang & Cai 2015 为锚点。
- 纳排判断：三元聚合物液–液相分离仅作低优先级候选，除非 LFP 体系实测到水/非溶剂污染或 PVDF 相边界。
- 饱和判断：跨领域“可能的机制集合”接近**饱和**；各路径在 LFP 中的存在性、占比和阈值**未饱和**。

### M7：凝胶孔弹性与岩土干缩断裂

- 核心查询：`gel drying poroelastic pressure fracture cavitation`; `soil desiccation cracking hydro mechanical review`; `basal friction layer thickness soil cracking`; `unsaturated flow cohesive fracture desiccation`; `phase field heterogeneous clay drying` 。
- 凝胶引文网：Scherer 1988/1989/1990 干燥系列 → Scherer & Smith 1995 空化 → Bertrand et al. 2016 有限变形孔弹性 → Noselli et al. 2016 裂尖孔弹韧化。
- 岩土引文网：Tang et al. 2021 综述 → Péron et al. 2009 收缩/脱饱和 → Zeng et al. 2019/2020 底摩擦–厚度 → Vo et al. 2017 内聚区 → Hün et al. 2021 异质相场。
- 饱和判断：输运–收缩–约束–断裂耦合的模型族达到第一阶段**架构饱和**；土/凝胶的数值参数全部排除直接移植。

### M8：连续卷对卷、多区烘箱与横幅均匀性

- 核心查询：`roll-to-roll battery electrode drying scale-up heat transfer coefficient`; `impingement nozzle heat transfer uniformity drying`; `pilot cathode coating drying DOE`; `NMP cathode drying solvent recovery mass balance` 。
- 直接命中：Román-Ramírez et al. 2021/2022 中试 DOE 及开放数据；von Horstig et al. 2026 跨设备放大；Kumberg et al. 2020/2021 局部传热系数与 IR/称重；Nienke et al. 2023/2024 喷嘴强度–均匀性。
- 饱和判断：“设定值→膜温/通量/气相溶剂边界”方法学接近**饱和**；20 cm LFP 线上的 $h(y),\beta(y),p_{NMP,g}(y)$ 实测数据**不存在于公开证据集**。

### M9：时间分辨电极“烘干电影”补充检索（2026-07-23）

- 核心查询：`in situ battery electrode coating drying X-ray radiography`; `operando ultrasound electrode drying`; `thick cathode real-time gravimetry film temperature NMP`; `roll-to-roll NMP cathode film temperature drying transition`; `dynamic gradient resistivity drying electrode`。
- 新增直接/近直接证据：Higa et al. (2024) 的硬 X 射线原位涂层动态；Kukay et al. (2024) 的厚 NMC/PVDF/NMP 同步质量–膜温；von Horstig et al. (2025) 的中试卷对卷膜温与局部边缘风险；Xiong et al. (2026) 的在线超声反馈；另登记 Baburoglu et al. (2025) 的深度敏感电阻代理和 Zhu et al. (2021) 的干燥应力模型。
- 证据纪律：超声拐点同时受厚度、密度、模量、饱和度和孔隙影响，不把它唯一命名为锁定；膜温回升可作为蒸发冷却减弱代理，不单独证明液相断连；模型应力不写成直接测量。
- 仍然缺失：同一块 LFP–PVDF/NMP 样品中同步 $m(t)$、$H(t)$、$T_s(t)$、内部 NMP 连通、湿态应力与首次裂纹/空洞的研究。
- 饱和判断：可观测代理和仪器组合已足够支持第一轮事件实验设计；目标 LFP 的事件共定位**未饱和**。

### M10：烘焙、饼干 checking 与未糊化淀粉浆（2026-07-23）

- 核心查询：`bread baking moving evaporation front crust crumb`; `bread local moisture core increase evaporation condensation NMR`; `biscuit checking moisture gradient cooling fracture`; `starch slurry drying cracking liquid vapor transport`。
- 面包线：Zanoni 1993/1994 的现象学与移动边界模型；Purlis & Salvadori 2009 的移动边界验证；Ureta et al. 2019 的局部温湿测量；Lucas et al. 2024 的空间 NMR；Sun et al. 2023 的入炉前/烘焙中气泡演化综述；Zhang et al. 2007 的人工表层约束；冷却/再分配用 Ben Aissa 2010 与 Baik 2000。
- 饼干线：Kim & Okos 1999 的输运/松弛物性；Saleem et al. 2005 的全场应变–有限元；Bedas et al. 2019 的 Karl Fischer/NIR 与 15 天裂损；Ahmad et al. 2001 的相近总含水、不同均匀性干预。
- 颗粒桥梁：Goehring 2009 的未糊化淀粉浆双孔隙与液相/蒸气两区；Crostack et al. 2012 的原位 X 射线裂纹前沿；Akiba et al. 2017 的淀粉类型/厚度反例。
- 迁移规则：只迁移移动转变区、表层状态定义、平均挥发物不充分、出炉后演化、双储库开关和同步实验逻辑；不迁移水物性、食品相变、面包壳厚、饼干湿度阈值、淀粉孔隙参数或裂纹百分比。
- 饱和判断：作为教学与假设生成的三条主线已达到本阶段**概念饱和**；它们不填补 LFP 参数缺口。

### M11：Schabel 署名工作与厚涂开裂相关性复核（2026-07-29）

- 检索边界：2011-01-01 至 2026-07-29；以 KIT-TFT 官方出版物列表、Schabel 作者元数据、KITopen 与 DOI 出版商页交叉核验。严格核心口径为“Schabel 署名 + 锂电湿电极主干燥或真空后干燥”，核得 39 项；本模块再只保留与 LFP 厚涂主干燥开裂相关的子集。
- 直接开裂命中：Kumberg et al. 2019 仍是该工作群中唯一系统测量厚度、蒸发通量、表面裂纹、裂纹严重度和粘附的核心实验；现有 E005/E006 和 Kumberg 专篇不重复登记。
- 相邻体系旁证：另登记 Schabel 署名的三项 Pt/C–Nafion 催化层研究（Quarz 2024；Zimmerer 2026 原位识别；Zimmerer 2026 参数解耦）为 FC01–FC03/E080–E082。它们直接约束“膜温—气侧传质—材料抗力—裂纹”的因果结构，但不计入上述 39 项锂电核心集，任何微米厚度、换热系数、CNT 比例和裂纹阈值均不向 LFP 移植。
- 开裂前状态命中：Jaiser 2016/2017 的 PVDF-NMP 石墨固化、孔排空与迁移；Kumberg 2021 的层厚–内部传质模型；Kumberg 2021 的在线称重/膜温边界标定。
- 工艺与设备命中：Jaiser/Altvater 的阶段选择性干燥、NIR 膜温–通量解耦、Mohacsi 在线孔排空代理，以及 von Horstig 2026 的跨设备 drivers 匹配。多层、Laponite 和 primer 只登记为二阶段候选干预，因为其主要终点不是裂纹。
- 排除：Schabel 的 post-drying、痕量水分、露点与 CO2 工作不进入湿涂层 NMP 开裂因果链；2026 孔尺度 binder 迁移预印本不进入已验证主张。
- 纠错：Jaiser 2016 与 2017 Cryo-BIB-SEM 为石墨/CB/PVDF-NMP，而非原文档误写的水系石墨；已同步修正教程、来源登记和 E007。其溶剂/粘结剂更接近目标体系，但活性物、正负极和几何仍不同。
- 饱和判断：Schabel 署名工作的“与开裂相关性分级”已达到本阶段饱和；其工作没有填补商用 LFP/PVDF-NMP 宽幅厚涂中湿态应力、内部裂纹或数值 CCT 的直接证据缺口。完整结果见 [`19_schabel_thick_coating_cracking_map.md`](19_schabel_thick_coating_cracking_map.md)。

## 3. 显式冲突与未决问题

| 编号 | 冲突/未决问题 | 本轮处理 |
|---|---|---|
| C01 | 自上而下的锐利颗粒固结前沿 vs 近似均匀收缩 | 保留 Jaiser 2017 的修正；将“表面富集/低渗层”与“宏观硬壳前沿”分开。 |
| C02 | 高温/高通量是否必然导致 PVDF 表面富集 | 将 Kumano/Jaiser 与 Zhang 反例同时保留；改用实际 $J,T_s,H$ 和材料/检测方法作条件。 |
| C03 | 颗粒越小是否必然更易裂 | 不给单调结论；分解为孔喉毛细压、网络模量/屈服、扩散/沉降与断裂能。 |
| C04 | 表面完整+中层空洞是否证明结皮 | 否。并列夹气、溶解气/蒸气、空化和真内裂，等待时序/三维/脱气鉴别。 |
| C05 | 更高干燥速率是否持续降低 CCT | 区分“起裂边界”和“裂纹严重度”；两者可对通量呈现不同响应。 |
| C06 | 负孔压是否一定降低断裂抵抗 | 否。整层孔压加载与裂尖局部溶剂流动耗散分开处理。 |

## 4. 引用与元数据审计

- 2026-07-22 首轮快照：59 个唯一核心来源、42 条主张级证据。
- 2026-07-23 电极时间分辨、烘焙专题与独立引用审计后：首轮登记 83 个来源、63 条证据；papers_Yang 页码级审计后为 87 个来源、73 条证据；2026-07-29 Schabel 开裂相关性复核及相邻催化层开裂旁证登记后为 **100 个来源**、**82 条主张级证据**，见 [`source_registry.csv`](source_registry.csv) 与 [`evidence_matrix.csv`](evidence_matrix.csv)。
- Crossref 逐条核验发现并修正：
  - `10.1016/j.compgeo.2016.12.010` 的第一作者是 **Vo**，不是 Sánchez；
  - `10.1016/j.ijheatmasstransfer.2015.06.015` 的第一作者是 **Yiantsios**；
  - `10.1002/polb.23590` 应引为 **Chen et al.**；
  - Kodikara & Costa 书章改用章节 DOI `10.1007/978-3-642-32492-5_2`，并保留页码 21–32。
- 在来源登记表中区分 `full text inspected`、`abstract only` 和 `abstract and metadata inspected`；仅摘要来源不用于方程细节或定量阈值。
- 食品来源的实验数值只说明其源体系中的因果或反例；凡涉及 LFP 均写明“本项目推论”和迁移边界。
- 2026-07-23 对用户提供的 17 个 papers_Yang PDF 做页码级核验：两份 D5EB00201J 为同一论文的不同封装，两份 Moorhead 2024 字节级相同；来源和证据均去重，原始文件仍全部保留。
- Dawson 学位论文使用 UCL 官方记录核对身份；与 D5EB00201J 重叠的形成结论优先采用后续同行评审版本，并把 thesis 的模型失败保留为负证据。
- 发现 Zhao et al. 2023 的有效导热、热边界、气相参数文字与相变闭合存在疑点，因此只保留热质结构/趋势，不把原方程直接移入项目模型。
- 纠正 Arai & Doi 2012 的证据措辞：气泡轨迹和压力是直接测量，泡内组成与扩散控制是推断；增长按正文 $R\propto\sqrt{t-\tau}$，不沿用结论段冲突表述。
- Wang et al. 2026 的 cracking 指循环期活性颗粒破裂，按预设缺陷定义排除出干燥开裂核心证据。

## 5. 停止与后续追踪

本轮在各模块的种子论文、综述模型谱系和修正性证据均已覆盖后停止。停止的是“继续堆积邻近材料论文”，不是声称目标体系已完全饱和。后续优先级为：

1. 获得 Liu & Deng (2026) 全文并做前后向引文更新；
2. 定期更新 `LFP + PVDF/NMP + thick coating + crack/void` 的目标检索；
3. 第一轮实验确定空洞/裂纹分支后，只对被数据支持的模型族做第二轮深检索；
4. 在取得内部生产数据前，不声称任何数值化的安全涂布量或通用温度–线速窗口。
