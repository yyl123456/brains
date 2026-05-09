# 大脑结构全景（精细版）

> 本文档从微观到宏观全面展示人脑结构，涵盖细胞层次、皮层分区、深部核团、
> 纤维连接、神经化学系统以及功能网络，为 Brains Agent 设计提供完整的生物学参考。

---

## 一、细胞层次基础 Cellular Foundation

### 1.1 神经元 Neurons

神经元是大脑的基本计算单元，全脑约有 **860 亿个神经元**和 **100-500 万亿个突触**。

| 神经元类型 | 英文名 | 特征 | 位置 | 功能 |
|-----------|--------|------|------|------|
| 锥体细胞 | Pyramidal Cell | 三角形胞体，顶树突伸向皮层表面 | 皮层 II/III/V/VI 层 | 兴奋性投射，皮层间及皮层下通信 |
| 星形细胞 | Stellate Cell | 多极，轴突局部分支 | 皮层 IV 层为主 | 接收丘脑输入，局部处理 |
| 篮状细胞 | Basket Cell | 抑制性中间神经元 | 皮层各层 | GABA 能抑制，调控锥体细胞放电 |
| 梭形细胞 | Fusiform Cell | 纺锤形 | 皮层 VI 层 | 皮层-丘脑反馈投射 |
| 马提诺蒂细胞 | Martinotti Cell | 轴突向皮层表层投射 | 皮层深层 | 抑制性调控 |
| 卡哈尔-雷兹乌斯细胞 | Cajal-Retzius Cell | 水平走行 | 皮层 I 层 | 发育期皮层层状结构引导 |
| 普金耶细胞 | Purkinje Cell | 极大扇形树突树 | 小脑皮层 | 小脑唯一输出神经元 |
| 颗粒细胞 | Granule Cell | 全脑最多的神经元类型 | 小脑、海马齿状回 | 兴奋性局部处理 |
| 中型多棘神经元 | Medium Spiny Neuron (MSN) | 密布树突棘 | 纹状体 | 基底神经节主要投射神经元 |

### 1.2 胶质细胞 Glial Cells

| 类型 | 英文名 | 数量比 | 功能 |
|------|--------|--------|------|
| 星形胶质细胞 | Astrocyte | 最多 | 血脑屏障、突触微环境维持、代谢支持、突触可塑性调制 |
| 少突胶质细胞 | Oligodendrocyte | — | 中枢神经系统髓鞘形成，加速信号传导 |
| 小胶质细胞 | Microglia | ~10% | 免疫防御、突触修剪、神经炎症反应 |
| 室管膜细胞 | Ependymal Cell | — | 产生脑脊液、形成脑室内壁 |

### 1.3 突触传递机制

```
突触前神经元                         突触后神经元
  │                                    │
  │  动作电位到达                        │
  │  → Ca²⁺ 通道开放                    │
  │  → 突触囊泡融合                      │
  │  → 神经递质释放                      │
  │       ↓                             │
  │  ─────突触间隙 (~20nm)─────          │
  │       ↓                             │
  │  受体结合 → 离子通道开放/关闭          │
  │       → 兴奋性突触后电位 (EPSP)       │
  │       → 抑制性突触后电位 (IPSP)       │
  │       → 信号整合 → 决定是否发放       │
```

**突触可塑性**：
- **长时程增强 (LTP, Long-Term Potentiation)**：反复刺激增强突触传递效率，是学习与记忆的细胞机制
- **长时程抑制 (LTD, Long-Term Depression)**：降低突触传递效率，用于记忆遗忘和运动学习微调
- **突触标记假说 (Synaptic Tagging)**：弱刺激可设置"标签"，后续强刺激的蛋白合成产物可被捕获

---

## 二、大脑皮层 Cerebral Cortex — 精细解剖

### 2.1 皮层六层结构 (Neocortex Laminar Organization)

| 层 | 名称 | 英文名 | 主要细胞 | 输入/输出 | 功能特点 |
|----|------|--------|----------|----------|----------|
| I | 分子层 | Molecular Layer | 极少细胞体，主要为树突和轴突 | 接收皮层反馈和非特异性丘脑投射 | 调控信号整合 |
| II | 外颗粒层 | External Granular Layer | 小型锥体细胞、星形细胞 | 接收层 IV 输入 | 皮层内局部处理 |
| III | 外锥体层 | External Pyramidal Layer | 中型锥体细胞 | **输出→对侧和同侧皮层** | 皮层-皮层通信（联络纤维/联合纤维） |
| IV | 内颗粒层 | Internal Granular Layer | 星形细胞为主 | **输入←丘脑特异性投射** | 主要感觉输入层，初级感觉皮层最厚 |
| V | 内锥体层 | Internal Pyramidal Layer | 大型锥体细胞（贝兹细胞在运动皮层） | **输出→纹状体、脑干、脊髓** | 皮层主要下行输出 |
| VI | 多形层 | Multiform/Fusiform Layer | 梭形细胞 | **输出→丘脑（反馈投射）** | 丘脑-皮层反馈调节 |

### 2.2 皮层分区 — Brodmann 区系统

#### 额叶 Frontal Lobe

| Brodmann 区 | 名称 | 英文名 | 功能 | 联动 |
|-------------|------|--------|------|------|
| BA4 | 初级运动皮层 | Primary Motor Cortex | 随意运动的直接控制（体定位图排列） | → 脊髓（皮质脊髓束）、基底神经节、小脑 |
| BA6 | 前运动区 / 辅助运动区 | Premotor / SMA | 运动计划、运动序列编程 | BA4、基底神经节、顶叶 |
| BA8 | 额叶眼动区 | Frontal Eye Field (FEF) | 自主性眼球运动控制 | 上丘、顶叶 |
| BA9/46 | 背外侧前额叶 | dlPFC | 工作记忆、认知控制、执行功能 | 顶叶、丘脑 MD 核、ACC |
| BA10 | 额极 | Frontopolar Cortex | 多任务协调、前瞻性记忆、元认知 | 海马体、颞叶 |
| BA11/12 | 眶额皮质 | Orbitofrontal Cortex (OFC) | 奖赏评估、决策、情绪调节 | 杏仁核、纹状体、丘脑 |
| BA24/32 | 前扣带皮层 | ACC | 冲突监控、错误检测、疼痛 | dlPFC、杏仁核、岛叶 |
| BA25 | 膝下扣带区 | Subgenual Cingulate | 情绪调节（抑郁症关键靶点） | 杏仁核、下丘脑、海马体 |
| BA44/45 | 布洛卡区 | Broca's Area | 语言产生、语法处理 | 韦尼克区（弓状束）、运动皮层 |
| BA47 | 额下回眶部 | Pars Orbitalis | 语义处理、抑制控制 | 颞叶、OFC |

#### 顶叶 Parietal Lobe

| Brodmann 区 | 名称 | 英文名 | 功能 | 联动 |
|-------------|------|--------|------|------|
| BA1/2/3 | 初级体感皮层 | Primary Somatosensory Cortex (S1) | 触觉、压觉、温度觉（体定位图排列） | 丘脑 VPL → S1 → 顶叶联合区 |
| BA5/7 | 顶叶联合区 | Superior Parietal Lobule (SPL) | 空间认知、本体感觉整合、视觉引导运动 | 额叶（运动计划）、枕叶（视觉） |
| BA39 | 角回 | Angular Gyrus | 阅读、数学运算、语义整合 | 韦尼克区、视觉皮层 |
| BA40 | 缘上回 | Supramarginal Gyrus | 音韵处理、工具使用 | 布洛卡区、体感皮层 |
| BA43 | 味觉皮层 | Gustatory Cortex | 味觉处理 | 岛叶、丘脑 |

#### 颞叶 Temporal Lobe

| Brodmann 区 | 名称 | 英文名 | 功能 | 联动 |
|-------------|------|--------|------|------|
| BA41/42 | 初级听觉皮层 | Primary Auditory Cortex (A1) | 声音频率分析（频率定位图排列） | 丘脑 MGN → A1 → 听觉联合区 |
| BA22 | 韦尼克区（后部） | Wernicke's Area | 语言理解、语音识别 | 布洛卡区（弓状束）、角回 |
| BA20/21 | 颞下回/颞中回 | Inferior/Middle Temporal Gyrus | 视觉物体识别、面孔处理 | 枕叶（腹侧视觉通路） |
| BA37 | 梭状回后部 | Fusiform Face Area (FFA) | 面孔识别 | 杏仁核（情绪面孔）、枕叶 |
| BA38 | 颞极 | Temporal Pole | 语义记忆、社会认知 | OFC（钩束）、杏仁核 |
| BA28/34 | 内嗅皮层 | Entorhinal Cortex | 海马体主要输入门户、空间导航（网格细胞） | 海马体、新皮层 |
| BA35/36 | 海马旁回 | Parahippocampal Gyrus | 场景识别、上下文记忆 | 海马体、视觉联合区 |

#### 枕叶 Occipital Lobe

| Brodmann 区 | 名称 | 英文名 | 功能 | 联动 |
|-------------|------|--------|------|------|
| BA17 | 初级视觉皮层 (V1) | Primary Visual Cortex / Striate Cortex | 基础视觉特征提取（朝向、边缘、对比度） | 丘脑 LGN → V1 → V2 |
| BA18 | V2 | Secondary Visual Cortex | 轮廓整合、立体视觉 | V1 → V2 → V3/V4/V5 |
| BA19 | V3/V4/V5 | Visual Association Areas | V3:动态形状 / V4:颜色 / V5(MT):运动 | 顶叶（背侧通路）、颞叶（腹侧通路） |

#### 岛叶 Insular Cortex（隐藏的第五叶）

| 子区 | 功能 | 联动 |
|------|------|------|
| 前岛叶 (Anterior Insula) | 内感受觉知、主观情感体验、共情、时间感知 | ACC、杏仁核、前额叶 |
| 后岛叶 (Posterior Insula) | 躯体感觉整合、疼痛处理 | 体感皮层、丘脑 |

---

## 三、间脑 Diencephalon — 精细结构

### 3.1 丘脑 Thalamus 全部核团

丘脑包含约 50-60 个核团，按功能分为三大类：

#### 特异性中继核

| 核团 | 英文名 | 输入 | 输出 | 功能 |
|------|--------|------|------|------|
| 外侧膝状体 | LGN | 视网膜神经节细胞 | V1 (BA17) | 视觉中继，6 层结构分处大/小细胞通路 |
| 内侧膝状体 | MGN | 下丘 (IC) | A1 (BA41) | 听觉中继 |
| 腹后外侧核 | VPL | 脊髓丘脑束、内侧丘系 | S1 (BA1/2/3) | 躯干和四肢体感中继 |
| 腹后内侧核 | VPM | 三叉丘系 | S1（面部区域） | 面部体感中继 |
| 腹外侧核 | VL | 小脑深部核团 | BA4/6 | 运动协调中继 |
| 腹前核 | VA | 苍白球内侧部 | 前运动区、SMA | 运动计划中继 |

#### 联合核

| 核团 | 英文名 | 连接 | 功能 |
|------|--------|------|------|
| 背内侧核 | MD | 杏仁核、前额叶 | 情绪、执行功能 |
| 前核群 | AN | 乳头体、扣带回 | 记忆（Papez 环路） |
| 丘脑枕 | Pulvinar | 顶叶、颞叶、枕叶 | 注意力调制、视觉认知 |
| 外侧后核 | LP | 顶叶联合区 | 空间认知 |

#### 非特异性核

| 核团 | 英文名 | 功能 |
|------|--------|------|
| 板内核群 | Intralaminar Nuclei (CM/PF) | 觉醒、意识、疼痛 |
| 网状核 | Reticular Nucleus (TRN) | 丘脑门控，调制信息通过，选择性注意 |

### 3.2 下丘脑 Hypothalamus 全部核团

| 区域 | 核团 | 英文名 | 功能 | 联动 |
|------|------|--------|------|------|
| **前区** | 视交叉上核 | Suprachiasmatic Nucleus (SCN) | 昼夜节律主时钟 | 视网膜（光输入）、松果体 |
| | 视上核 | Supraoptic Nucleus | 分泌 ADH（抗利尿） | 垂体后叶 |
| | 室旁核 | Paraventricular Nucleus (PVN) | 分泌 CRH（应激）、催产素 | 垂体、自主神经系统 |
| | 视前区 | Preoptic Area | 体温调节、性行为 | 自主神经系统 |
| **中区** | 弓状核 | Arcuate Nucleus | 食欲调节（NPY/POMC） | 垂体门脉系统 |
| | 腹内侧核 | Ventromedial Nucleus (VMN) | 饱感中枢、防御行为 | 杏仁核、脑干 |
| | 背内侧核 | Dorsomedial Nucleus | 情绪行为、体重调节 | 边缘系统 |
| **后区** | 乳头体 | Mammillary Body | 记忆回路（Papez 环路） | 海马体（穹窿）→ 丘脑前核 |
| | 后核 | Posterior Nucleus | 体温升高、交感兴奋 | 自主神经系统 |
| | 外侧下丘脑 | Lateral Hypothalamus | 摄食中枢、觉醒（含食欲素神经元 Orexin） | 全脑（觉醒网络） |

### 3.3 上丘脑 Epithalamus

| 结构 | 英文名 | 功能 |
|------|--------|------|
| 松果体 | Pineal Gland | 分泌褪黑素 (Melatonin)，调节昼夜节律 |
| 缰核 | Habenula | 奖赏预期误差、厌恶学习、抑制多巴胺释放 |

---

## 四、边缘系统 Limbic System — 精细解剖

### 4.1 海马体 Hippocampus

#### 内部结构

```
海马体 (Hippocampus) 横截面 — 三突触回路
   
   内嗅皮层 (EC)
       │
       │ 穿通纤维 (Perforant Path)
       ▼
   齿状回 (DG) — 颗粒细胞层
       │
       │ 苔藓纤维 (Mossy Fibers)
       ▼
   CA3 区 — 锥体细胞层（循环连接丰富）
       │
       │ 谢弗侧支 (Schaffer Collaterals)
       ▼
   CA1 区 — 锥体细胞层
       │
       │ 输出
       ▼
   下托 (Subiculum) → 穹窿 → 乳头体 / 隔区
```

#### 功能分区

| 子区 | 英文名 | 特点 | 功能 |
|------|--------|------|------|
| 齿状回 | Dentate Gyrus (DG) | 成年神经发生持续区 | 模式分离（区分相似记忆） |
| CA3 | Cornu Ammonis 3 | 丰富的循环兴奋连接 | 模式完成（从部分线索恢复完整记忆）、快速编码 |
| CA1 | Cornu Ammonis 1 | 主要输出区 | 时序记忆、比较新旧信息 |
| 下托 | Subiculum | 海马体输出枢纽 | 空间导航、记忆整合 |

#### 特殊细胞类型

| 细胞 | 英文名 | 位置 | 功能 |
|------|--------|------|------|
| 位置细胞 | Place Cell | CA1/CA3 | 编码空间位置（认知地图） |
| 网格细胞 | Grid Cell | 内嗅皮层 | 形成空间度量（六角网格） |
| 头方向细胞 | Head Direction Cell | 海马旁回/丘脑 | 编码头部朝向 |
| 边界细胞 | Border Cell | 内嗅皮层 | 编码环境边界 |
| 时间细胞 | Time Cell | CA1 | 编码事件时间间隔 |

### 4.2 杏仁核 Amygdala

| 核群 | 英文名 | 输入 | 输出 | 功能 |
|------|--------|------|------|------|
| 基外侧核群 | Basolateral (BLA) | 感觉皮层、丘脑、海马体 | 中央核、前额叶 | 刺激-情绪关联学习，情绪记忆编码 |
| 中央核 | Central Nucleus (CeA) | BLA | 下丘脑、脑干 | 恐惧反应输出（冻结、心率加速等） |
| 内侧核 | Medial Nucleus | 嗅球 | 下丘脑 | 社会行为、费洛蒙处理 |
| 皮层核 | Cortical Nucleus | 嗅觉系统 | 内嗅皮层 | 嗅觉情绪处理 |

**关键通路**：
- **低通路**（快速、粗略）：丘脑 → 杏仁核（绕过皮层，约 12ms）
- **高通路**（慢速、精确）：丘脑 → 感觉皮层 → 杏仁核（约 30-40ms）

### 4.3 扣带回 Cingulate Gyrus

| 分区 | 英文名 | 功能 | 联动 |
|------|--------|------|------|
| 前扣带回膝前部 | Pregenual ACC (pgACC) | 情绪调节 | vmPFC、杏仁核 |
| 前扣带回背侧部 | Dorsal ACC (dACC) | 认知控制、冲突监控 | dlPFC、岛叶 |
| 膝下扣带回 | Subgenual ACC (sgACC) | 悲伤、抑郁（深部脑刺激靶点） | 杏仁核、下丘脑 |
| 中扣带回 | Midcingulate Cortex (MCC) | 疼痛感知、运动选择 | 运动皮层、岛叶 |
| 后扣带回 | Posterior Cingulate Cortex (PCC) | 内省、自我参照、默认模式网络核心 | 海马体、角回 |
| 压后皮层 | Retrosplenial Cortex (RSC) | 空间记忆、导航 | 海马体、顶叶 |

---

## 五、基底神经节 Basal Ganglia — 精细解剖

### 5.1 组成结构

| 结构 | 英文名 | 细胞类型 | 功能 |
|------|--------|----------|------|
| 尾状核 | Caudate Nucleus | MSN (D1/D2 型) | 认知控制、目标导向行为 |
| 壳核 | Putamen | MSN (D1/D2 型) | 习惯性运动控制 |
| 伏隔核 | Nucleus Accumbens (NAc) | MSN | 奖赏预测、动机驱动 |
| 苍白球外侧部 | Globus Pallidus externa (GPe) | GABA 能 | 间接通路中继 |
| 苍白球内侧部 | Globus Pallidus interna (GPi) | GABA 能 | 基底神经节主要输出 |
| 黑质致密部 | Substantia Nigra pars compacta (SNc) | 多巴胺能 | 多巴胺释放，调制纹状体 |
| 黑质网状部 | Substantia Nigra pars reticulata (SNr) | GABA 能 | 基底神经节输出（眼动、头动） |
| 丘脑底核 | Subthalamic Nucleus (STN) | 谷氨酸能 | 超直接通路，运动抑制 |

### 5.2 三大通路

```
                    皮层 (Cortex)
                    │          │           │
           直接通路  │   间接通路 │  超直接通路 │
                    ▼          ▼           ▼
               纹状体D1    纹状体D2       STN
               (抑制)      (抑制)       (兴奋)
                    │          │           │
                    ▼          ▼           ▼
                  GPi/SNr    GPe        GPi/SNr
                    │          │           
                    │          ▼           
                    │        STN→GPi/SNr   
                    │          │           
                    ▼          ▼           
               丘脑 (抑制减弱→促进运动)   丘脑 (抑制增强→抑制运动)
                    │
                    ▼
                  皮层

直接通路 (Direct)：促进期望运动 — "Go" 信号
间接通路 (Indirect)：抑制非期望运动 — "No-Go" 信号  
超直接通路 (Hyperdirect)：全局快速制动 — "Stop" 信号
```

### 5.3 多巴胺调制

| 受体 | 位置 | 效应 | 功能意义 |
|------|------|------|----------|
| D1 受体 | 直接通路 MSN | 兴奋 → 促进运动 | 正强化信号、奖赏学习 |
| D2 受体 | 间接通路 MSN | 抑制 → 减少制动 | 风险评估、厌恶学习 |

**奖赏预测误差 (Reward Prediction Error, RPE)**：
- 实际奖赏 > 预期 → 多巴胺 burst 放电 → 正向学习
- 实际奖赏 = 预期 → 基线放电 → 不更新
- 实际奖赏 < 预期 → 多巴胺 pause → 负向学习（extinction）

---

## 六、小脑 Cerebellum — 精细解剖

### 6.1 小脑皮层三层结构

| 层 | 英文名 | 主要细胞 | 功能 |
|----|--------|----------|------|
| 分子层 | Molecular Layer | 平行纤维、星形细胞、篮状细胞 | 信号整合、抑制调控 |
| 普金耶细胞层 | Purkinje Cell Layer | 普金耶细胞 | 小脑皮层唯一输出 (GABA 能) |
| 颗粒层 | Granular Layer | 颗粒细胞、高尔基细胞 | 苔藓纤维输入处理、模式扩展 |

### 6.2 输入-处理-输出

```
输入系统:
  苔藓纤维 (Mossy Fiber) ← 脑桥核 ← 大脑皮层
       ↓
  颗粒细胞 → 平行纤维 → 普金耶细胞

  攀爬纤维 (Climbing Fiber) ← 下橄榄核 ← 误差信号
       ↓
  直接激活普金耶细胞 → 触发复杂棘波 → 修改突触权重（学习）

输出系统:
  普金耶细胞 (抑制) → 深部核团 → 丘脑VL → 运动皮层
                              → 红核 → 脊髓
```

### 6.3 功能分区

| 分区 | 英文名 | 解剖位置 | 输入 | 输出 | 功能 |
|------|--------|----------|------|------|------|
| 前庭小脑 | Vestibulocerebellum | 绒球小结叶 | 前庭核 | 前庭核 | 平衡、眼动（VOR） |
| 脊髓小脑 | Spinocerebellum | 蚓部 + 中间带 | 脊髓 | 红核、网状结构 | 姿势、步态、肢体协调 |
| 大脑小脑 | Cerebrocerebellum | 外侧半球 | 大脑皮层（经脑桥） | 丘脑VL → 皮层 | 运动计划、认知、语言 |

---

## 七、脑干 Brainstem — 精细解剖

### 7.1 中脑 Midbrain

| 结构 | 英文名 | 功能 | 联动 |
|------|--------|------|------|
| 上丘 | Superior Colliculus | 视觉定向反射、眼球跳跃运动 | FEF、V1、脊髓 |
| 下丘 | Inferior Colliculus | 听觉中继与整合 | MGN → 听觉皮层 |
| 红核 | Red Nucleus | 运动协调（红核脊髓束） | 小脑、运动皮层 |
| 黑质 | Substantia Nigra | 运动启动（致密部）、运动输出（网状部） | 纹状体、丘脑 |
| 腹侧被盖区 | VTA | 奖赏、动机（多巴胺释放） | 伏隔核、前额叶 |
| 中脑导水管周围灰质 | PAG | 疼痛调控、防御行为 | 脊髓、杏仁核 |
| 中脑网状结构 | Midbrain Reticular Formation | 觉醒调节 | 丘脑板内核 |

### 7.2 脑桥 Pons

| 结构 | 英文名 | 功能 | 联动 |
|------|--------|------|------|
| 脑桥核 | Pontine Nuclei | 皮层-小脑信息中继 | 大脑皮层 → 脑桥核 → 小脑 |
| 蓝斑 | Locus Coeruleus (LC) | 去甲肾上腺素释放、警觉、注意力 | 全脑弥散投射 |
| 中缝背核 | Dorsal Raphe Nucleus | 5-HT 释放、情绪调节 | 全脑弥散投射 |
| 臂旁核 | Parabrachial Nucleus | 味觉、内脏感觉、呼吸 | 丘脑、下丘脑 |
| 脑桥呼吸中枢 | Pontine Respiratory Group | 呼吸节律精细调节 | 延髓呼吸中枢 |

### 7.3 延髓 Medulla Oblongata

| 结构 | 英文名 | 功能 |
|------|--------|------|
| 孤束核 | Nucleus Tractus Solitarius (NTS) | 内脏感觉整合（味觉、血压、消化） |
| 疑核 | Nucleus Ambiguus | 吞咽、发声、心率调节 |
| 迷走神经背运动核 | Dorsal Motor Nucleus of Vagus | 副交感输出（心、肺、消化道） |
| 下橄榄核 | Inferior Olivary Nucleus | 小脑攀爬纤维来源，运动学习误差信号 |
| 薄束核/楔束核 | Gracile/Cuneate Nucleus | 精细触觉和本体感觉中继 |
| 延髓呼吸中枢 | Medullary Respiratory Center | 基础呼吸节律发生 |
| 延髓心血管中枢 | Medullary Cardiovascular Center | 心率和血压调节 |

---

## 八、神经递质系统 — 精细解剖

### 8.1 主要神经递质通路

#### 多巴胺 (Dopamine) 系统

| 通路 | 英文名 | 起源 → 靶区 | 功能 | 相关疾病 |
|------|--------|-------------|------|----------|
| 中脑边缘通路 | Mesolimbic | VTA → NAc | 奖赏、动机、成瘾 | 成瘾、精神分裂（阳性症状） |
| 中脑皮层通路 | Mesocortical | VTA → PFC | 认知、工作记忆、注意力 | 精神分裂（阴性症状）、ADHD |
| 黑质纹状体通路 | Nigrostriatal | SNc → 尾状核/壳核 | 运动启动与控制 | 帕金森病 |
| 结节漏斗通路 | Tuberoinfundibular | 弓状核 → 正中隆起 | 抑制催乳素分泌 | 高催乳素血症 |

#### 5-羟色胺 (Serotonin, 5-HT) 系统

| 核团 | 投射区域 | 功能 |
|------|----------|------|
| 中缝背核 (B7) | 大脑皮层、基底神经节、边缘系统 | 情绪、焦虑、强迫 |
| 中缝正中核 (B8) | 海马体、隔区 | 记忆、空间认知 |
| 中缝大核 (B3) | 脊髓 | 疼痛调控 |

#### 去甲肾上腺素 (Norepinephrine, NE) 系统

- **来源**：蓝斑 (Locus Coeruleus, LC)，仅约 15,000 个神经元
- **投射**：几乎投射到全脑所有区域
- **功能**：觉醒-注意力调制（倒U曲线）、应激反应、记忆巩固
- **模式**：
  - 紧张(Tonic)模式 → 高警觉、扫描环境
  - 相位(Phasic)模式 → 集中注意力于特定刺激

#### 乙酰胆碱 (Acetylcholine, ACh) 系统

| 来源 | 英文名 | 投射 | 功能 |
|------|--------|------|------|
| 基底核 (Meynert) | Nucleus Basalis of Meynert (NBM) | 新皮层 | 注意力、记忆编码 |
| 内侧隔核 | Medial Septal Nucleus | 海马体 | θ 节律驱动、记忆 |
| 脑干胆碱能核 | Pedunculopontine/Laterodorsal Tegmental | 丘脑 | 觉醒、REM 睡眠 |

### 8.2 主要受体类型

| 递质 | 受体类型 | 效应 | 临床意义 |
|------|----------|------|----------|
| 谷氨酸 | AMPA | 快速兴奋 | 基础突触传递 |
| 谷氨酸 | NMDA | 慢速兴奋，电压/配体双门控 | LTP（学习与记忆关键） |
| 谷氨酸 | mGluR | 代谢型调控 | 突触可塑性精细调节 |
| GABA | GABA_A | 快速抑制（Cl⁻通道） | 抗焦虑药物靶点 |
| GABA | GABA_B | 慢速抑制（G蛋白偶联） | 肌肉松弛、止痛 |
| ACh | 烟碱型 (nAChR) | 快速兴奋 | 注意力增强 |
| ACh | 毒蕈碱型 (mAChR) | 调制性 | 记忆（阿尔茨海默病相关） |

---

## 九、白质纤维束 White Matter Tracts — 完整分类

### 9.1 联合纤维 (Commissural Fibers) — 连接两半球

| 纤维束 | 英文名 | 连接 | 功能 |
|--------|--------|------|------|
| 胼胝体 | Corpus Callosum | 左右半球同源区域 | 半球间信息整合 |
| ├─ 嘴部 | Rostrum | 眶额叶 | |
| ├─ 膝部 | Genu（→小钳） | 前额叶 | 执行功能协调 |
| ├─ 体部 | Body | 运动/体感皮层 | 感觉运动协调 |
| └─ 压部 | Splenium（→大钳） | 枕叶/颞叶 | 视觉信息整合 |
| 前连合 | Anterior Commissure | 双侧颞叶、杏仁核 | 嗅觉和情绪信息交换 |
| 海马连合 | Hippocampal Commissure | 双侧海马体 | 记忆信息交换 |

### 9.2 联络纤维 (Association Fibers) — 连接同侧半球不同区域

| 纤维束 | 英文名 | 连接 | 功能 |
|--------|--------|------|------|
| 弓状束 | Arcuate Fasciculus (AF) | 布洛卡区 ↔ 韦尼克区 | 语言产生与理解的桥梁 |
| 上纵束 | Superior Longitudinal Fasciculus (SLF) | 额叶 ↔ 顶叶/颞叶 | 注意力、空间认知 |
| 下纵束 | Inferior Longitudinal Fasciculus (ILF) | 枕叶 ↔ 颞叶 | 视觉识别（腹侧通路） |
| 下额枕束 | Inferior Fronto-Occipital Fasciculus (IFOF) | 额叶 ↔ 枕叶 | 语义处理、视觉注意 |
| 钩束 | Uncinate Fasciculus (UF) | 前颞叶 ↔ 眶额叶 | 情绪调节、社会认知 |
| 扣带束 | Cingulum | 沿扣带回全程 | 情绪、记忆、注意力 |
| 穹窿 | Fornix | 海马体 → 乳头体/隔区 | 记忆回路核心通路 |

### 9.3 投射纤维 (Projection Fibers) — 连接皮层与皮层下

| 纤维束 | 英文名 | 连接 | 功能 |
|--------|--------|------|------|
| 内囊 | Internal Capsule | 皮层 ↔ 丘脑/脑干/脊髓 | 运动和感觉信号传导的关键瓶颈 |
| 皮质脊髓束 | Corticospinal Tract | 运动皮层 → 脊髓 | 随意运动控制 |
| 丘脑辐射 | Thalamic Radiations | 丘脑 → 皮层各区 | 感觉信息分发 |
| 视辐射 | Optic Radiation | LGN → V1 | 视觉信号传导 |
| 听辐射 | Auditory Radiation | MGN → A1 | 听觉信号传导 |

---

## 十、大尺度功能网络 Large-Scale Brain Networks

现代神经科学认为大脑功能并非由单一区域独立完成，而是由分布式网络协同实现。

| 网络 | 英文名 | 核心节点 | 功能 | 对立/协作网络 |
|------|--------|----------|------|---------------|
| **默认模式网络** | Default Mode Network (DMN) | vmPFC、PCC、角回、海马体 | 内省、自传体记忆、心理理论、走神 | 与 TPN 反相关 |
| **任务正网络** | Task-Positive Network (TPN) / Central Executive | dlPFC、后顶叶、FEF | 目标导向注意力、工作记忆 | 与 DMN 反相关 |
| **突显网络** | Salience Network (SN) | 前岛叶、dACC | 检测重要刺激、切换 DMN/TPN | 调制 DMN↔TPN 切换 |
| **感觉运动网络** | Sensorimotor Network | 运动皮层、S1、SMA | 运动执行与体感处理 | 小脑、基底神经节 |
| **视觉网络** | Visual Network | V1-V5、梭状回 | 视觉处理层级 | 顶叶（背侧）、颞叶（腹侧） |
| **听觉网络** | Auditory Network | A1、颞上沟 | 听觉处理、语音 | 布洛卡区（语言） |
| **边缘网络** | Limbic Network | 杏仁核、海马体、OFC | 情绪处理、记忆 | SN（触发）、PFC（调节） |
| **背侧注意网络** | Dorsal Attention Network (DAN) | FEF、后顶叶 (IPS) | 自上而下注意力导向 | 与 VAN 互补 |
| **腹侧注意网络** | Ventral Attention Network (VAN) | 颞顶联合区 (TPJ)、腹侧额叶 | 自下而上注意力捕获 | 与 DAN 互补 |

---

## 十一、记忆系统全景 Memory Systems

### 11.1 记忆分类与神经基础

```
记忆 (Memory)
├── 感觉记忆 (Sensory Memory) — 数百毫秒
│   ├── 图标记忆 (Iconic) — V1/V2
│   └── 回声记忆 (Echoic) — A1
│
├── 工作记忆 (Working Memory) — 秒级
│   ├── 语音环 (Phonological Loop) — 布洛卡区、韦尼克区
│   ├── 视空间画板 (Visuospatial Sketchpad) — 后顶叶、枕叶
│   ├── 情景缓冲 (Episodic Buffer) — 额叶
│   └── 中央执行 (Central Executive) — dlPFC
│
└── 长时记忆 (Long-Term Memory)
    ├── 陈述性/外显记忆 (Declarative/Explicit)
    │   ├── 情景记忆 (Episodic) — 海马体、前额叶
    │   └── 语义记忆 (Semantic) — 前颞叶、广泛皮层
    │
    └── 非陈述性/内隐记忆 (Non-declarative/Implicit)
        ├── 程序记忆 (Procedural) — 基底神经节、小脑
        ├── 启动效应 (Priming) — 感觉皮层
        ├── 条件反射 (Conditioning)
        │   ├── 情绪性 — 杏仁核
        │   └── 骨骼肌 — 小脑
        └── 非联合学习 (Habituation/Sensitization) — 反射弧
```

### 11.2 记忆巩固过程

```
编码 (Encoding):
  感觉皮层 → 海马体（快速编码、突触可塑性）

巩固 (Consolidation):
  1. 突触巩固 (分钟-小时): LTP → 蛋白质合成 → 结构性突触改变
  2. 系统巩固 (天-年): 海马体 ⇄ 新皮层 反复重激活（尤其慢波睡眠期间）
     → 记忆逐渐从海马体依赖转为皮层依赖

提取 (Retrieval):
  前额叶（策略性搜索） + 海马体（模式完成） → 皮层存储区（激活表征）

遗忘 (Forgetting):
  1. 衰减 (Decay): 突触连接弱化
  2. 干扰 (Interference): 新旧记忆竞争
  3. 主动遗忘: 前额叶驱动的海马体活动抑制
```

---

## 十二、对 Agent 设计的映射提示

| 大脑系统 | 功能本质 | Agent 类比 |
|----------|----------|-----------|
| 感觉皮层 | 多模态输入编码 | 输入解析器（文本/图像/音频处理） |
| 丘脑 | 信息过滤与路由 | 注意力/路由机制 |
| 海马体 | 快速编码、情景记忆、模式分离/完成 | 短期向量存储、RAG 检索 |
| 新皮层 | 长期知识、语义表征 | 长期知识库、嵌入空间 |
| 前额叶 | 工作记忆、计划、决策 | 推理引擎、上下文窗口管理 |
| 杏仁核 | 情绪标记、优先级 | 重要性评分、紧急度标记 |
| 基底神经节 | 行动选择、习惯 | 工具调用路由、策略缓存 |
| 小脑 | 误差修正、精细调节 | 自我评估、输出校准 |
| 默认模式网络 | 内省、联想 | 后台联想/重整理进程 |
| 突显网络 | 关键信号检测 | 中断/优先级切换机制 |
| 睡眠巩固 | 记忆整理与压缩 | 离线索引重建、知识蒸馏 |

---

*本文档为 Brains Agent 项目参考资料 — 精细版*
