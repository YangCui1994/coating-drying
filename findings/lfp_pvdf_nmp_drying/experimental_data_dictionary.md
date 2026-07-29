# 首轮实验数据字典与事件编码

> 配套文件：[`experimental_data_template.csv`](experimental_data_template.csv)。这是项目内部数据规范，不是文献结论。

## 1. 一行数据代表什么

一行对应“一个独立可追溯样品 × 一个横幅位置 × 一个过程/中断时刻”。同一完整干燥 run 在多个横幅位置或多个中断点取样时，应使用不同的 `run_id` 或 `sample_role/process_time_s` 组合，不能把多位置平均后只留一行。

- `batch_id`：生产/涂布批次。
- `independent_slurry_batch_id`：真正独立配制的浆料批次；用于区分生物学意义上的独立重复与同一卷上的相邻技术重复。
- `replicate_id`：同一实验条件下的重复编号。
- `sample_role`：建议限定为 `preoven`、`full_dry`、`interrupted`、`hot_exit`、`cooled`、`post_rest`、`post_calender` 或 `section_control`。
- `transverse_y_mm`：横幅共定位坐标；必须保留边缘、四分之一处和中心的真实位置，而不是只写 `edge/center`。

## 2. 缺失值规则

- 未测量写空值或 `NA`，不能写 `0`。
- 低于检出限写 `below_LOD`，并在 `measurement_uncertainty_note` 记录 LOD。
- 事件未发生、未分辨和未测量是三种不同状态，分别写 `not_observed`、`unresolved`、`not_measured`。
- 时间统一相对 E0，以秒记录；入炉前已存在的缺陷记为 `left_censored_pre_E0`。

## 3. E0–E6 事件字段

| 字段 | 写入条件 | 不能用什么替代 |
|---|---|---|
| `event_e0_s` | 受控烘箱边界接通，通常为 0 | 颗粒锁定 |
| `event_e1_s` + `event_e1_status` | 首次局部机械锁定可被独立分辨 | PVDF 富集、表面变哑、低渗层 |
| `event_e2_s` | 跨厚度承载骨架形成，宏观收缩进入分辨率平台 | 完全干燥 |
| `event_e3_s` + `event_e3_evidence` | 外界连通气相首次进入孔网 | 单独的失重拐点 |
| `event_e4_s` + `event_e4_evidence` | 到表面的连续供液路径失去贯通 | NMP 清零；气侧变化造成的降速 |
| `event_e5_s` + `event_e5_code` | 首次不可逆 D1–D5 失效 | 出炉后第一次看到缺陷 |
| `event_e6_s` | 按预定义空间统计和取样方法达到残余 NMP 规格 | 零溶剂或结构不再变化 |

E5 是横切事件，不应因为编号而强制排在 E4 后。多类缺陷同时出现时，`event_e5_code` 可用分号分隔，例如 `D3;D5`，并在 `notes` 写清哪个先被识别。

Dawson 的 CT/DVC 结果说明“局部位移异常、气体逸出/永久变形、可见裂纹和脱层”可能不是同一时刻。因此 E5 还需要以下字段：

| 字段 | 物理/观测含义 | 记录要求 |
|---|---|---|
| `event_e5_detection_method` | 首次 E5 由哪种方法判定，例如 DIC、DVC、表面相机、CT 或截面 | 方法变更时不能直接比较阈值 |
| `event_e5_threshold` | 预注册的位移、开口、持续时间或分割阈值 | 同时写空间窗口和连续帧数；不能事后按结果调阈值 |
| `event_e5_interval_lower_s`、`event_e5_interval_upper_s` | 真实事件所在的帧间区间 | 若 38 min 尚无、40 min 首见，应写 $(2280,2400]$ s，而不是虚构 2340 s 的精确真值 |
| `first_visible_defect_s` | 肉眼/原始图像首次可见的缺陷时刻 | 与 DIC/DVC 的早期信号分开 |
| `dic_dvc_peak_displacement_um` | 刚体运动校正后、预定义窗口内的局部峰值位移 | 保存方向分量、算法参数和空间分辨率到轨迹元数据 |
| `dic_dvc_background_um` | 同帧无缺陷参照区或全场伪影的位移水平 | 早期信号必须相对背景解释，不能只报峰值 |

这些字段不把 Dawson 报告的 1–2 µm 设为 LFP 通用门槛；它们只是让目标实验能估计自己的信噪比、误报率和事件时间区间。

## 4. `Skin+` 编码

`skin_plus_status` 建议使用：

- `supported`：重复测得表层相对内部持续的低渗、低扩散、高模量、高屈服或固定状态对比；
- `not_supported`：在方法分辨率内未发现持续对比；
- `unresolved`：证据相互冲突或分辨率不足；
- `not_measured`：未进行能够判断的厚向测量。

`skin_plus_evidence` 必须写具体测量，如 `permeability_profile`、`wet_modulus_profile`、`composition_plus_mechanics`；“表面完整”不是有效证据。

## 5. 残余 NMP 的空间口径

- `residual_nmp_method`：GC、热脱附、TGA 或其他经校准方法。
- `residual_nmp_sampling_basis`：面积平均、顶/中/底分层、横幅最坏位置或规定产品抽样法。
- `residual_nmp_mean_ppm` 与 `residual_nmp_worst_ppm` 必须分开；若只测平均值，最坏值留空。
- `residual_nmp_top_ppm/mid_ppm/bottom_ppm` 只有在分层方法的交叉污染与回收率已评估时填写。

## 6. D1–D5 与中层空洞判别字段

| 代码 | 质量表型 | 最少需要额外记录 |
|---|---|---|
| D1 | 表面通道/泥裂 | 深度、宽度、面积、是否到达基底 |
| D2 | 真正层内内聚裂纹 | 裂尖、面状三维连通、形成时序 |
| D3 | 气泡/异常空洞/空化候选 | 球形度、连通性、入炉前基线、脱气响应 |
| D4 | 界面脱粘 | 脱粘起点、与 D1 触底的先后、剥离强度 |
| D5 | 表面起伏/鼓包/塌陷 | $S_a$、振幅、主波长、下方是否有腔体 |

`crack_tip_present`、`void_connectivity` 和 `void_preexisting_status` 是区分 D2/D3 的关键字段。`sectioning_artifact_risk` 必须记录 cryo、真空、离子束或机械切片过程可能造成的拔出和弱面张开。

## 7. 轨迹与不确定度

`film_temp_trace_id`、`evaporation_flux_trace_id`、`mass_loss_trace_id`、`thickness_trace_id` 与 `surface_topography_trace_id` 应指向原始数据文件，而不是把整条曲线塞进 CSV。每条轨迹需在元数据中保存采样频率、校准日期、坐标基准和时间同步误差。

`measurement_uncertainty_note` 至少记录：传感器精度、事件时间分辨率、残余 NMP 检出限、截面抽样体积和缺陷分割阈值。模型拟合时应把这些量作为观测误差，而不是把所有偏差吸收到材料参数中。
