# Brains Agent Architecture Design (v2 - 增强认知版)

## 1. 核心设计理念

Brains Agent v2 旨在将“大模型作为 CPU”的理念演进为“大模型作为大脑核心”。通过整合 MemGPT 的 OS 级管理、Zep 的时态图谱、Stanford 的反思机制以及 Voyager 的技能库，我们构建了一个多维度的认知系统。

## 2. 增强型脑区映射架构

| 生物脑区 | Agent 模块名称 | 核心职责 | 借鉴项目 | 关键技术实现 |
| :--- | :--- | :--- | :--- | :--- |
| **丘脑 (Thalamus)** | **Sensory Gateway** | 信号过滤、意图路由、多模态预处理 | Claude Code, Cognee | Message Router, Input Filtering |
| **海马体 (Hippocampus)** | **Multilayer Memory** | 短期/长期记忆编码、检索与合并 | **Mem0, Zep, MemGPT** | Atomic Fact Extraction, Vector-Graph Hybrid, Paging |
| **大脑皮层 (Cortex)** | **Semantic Engine** | 抽象建模、跨领域推理、世界模型构建 | **Cognee, Zep** | Semantic Knowledge Graph, Ontology Grounding |
| **前额叶 (Prefrontal)** | **Executive & Reflect** | 目标设定、分层计划、高层反思 (Metacognition) | **Stanford Agents, Letta** | Reflection Loops, Hierarchical Planning, Dream-time Compute |
| **基底神经节 (Basal Ganglia)** | **Procedural Library** | 技能习得、工具链自动化、习惯化策略 | **Voyager** | Executable Skill Library (Code-as-Memory) |
| **杏仁核 (Amygdala)** | **Emotional & Risk** | 情绪标记 (Salience)、安全边界、优先级管理 | **MemoryBank** | Importance Scoring, Risk Guardrails |
| **小脑 (Cerebellum)** | **Refinement Loop** | 输出校准、行为纠错、持续在线学习 | **Voyager, Cognee** | Self-Correction, `.improve()` API |

---

## 3. 核心子系统详解

### 3.1 混合记忆层次结构 (Hybrid Memory Tiering)
受 **MemGPT/Letta** 和 **Zep/Graphiti** 启发：
- **Level 0: Core Memory (L1 Cache)**: 直接在 Context Window 中，由 Agent 自主管理的实体与偏好（MemGPT 风格的 `self_edit`）。
- **Level 1: Episodic Stream (L2 Cache)**: 原始交互序列，带有时标和重要度分数（Stanford 风格的 Memory Stream）。
- **Level 2: Semantic Graph (Storage)**: 经由 **Cognee/Zep** 提取的实体、关系、社区（Communities）。支持双时态（Event Time vs. Ingestion Time）。
- **Level 3: Procedural Skills (ROM)**: **Voyager** 风格的技能库。当 Agent 发现某个复杂任务可重复时，将其固化为一段经过验证的代码/工具，下次直接调用。

### 3.2 认知闭环：感知-反思-行动 (The Cognitive Loop)
受 **Stanford Generative Agents** 启发：
1.  **Perceive (感知)**: 外部输入进入 `Sensory Gateway`。
2.  **Retrieve (检索)**: 基于 **Recency (新近度)**, **Importance (重要度)**, **Relevance (相关性)** 的三位一体检索。
3.  **Reflect (反思)**: 当累积的记忆重要度超过阈值，触发“梦境”或“后台计算”进行知识固化和冲突检测。
4.  **Plan (计划)**: 前额叶将大目标分解为细粒度行动。
5.  **Act (行动)**: 基底神经节选择最佳工具或技能执行。
6.  **Learn (学习)**: 小脑评估结果，更新记忆重要度或修正技能库。

### 3.3 技能习得系统 (Skill Acquisition)
参考 **Voyager**：
- Agent 具备“元编程”能力。
- 成功的工具链组合会被重构为 `Skill` 类。
- `Skill` 包含：描述（语义检索）、代码实现（直接执行）、测试用例（验证可靠性）。

---

## 4. 关键流程：记忆的“固化” (Memory Consolidation)

1.  **Raw Interaction**: 存入 Episodic Stream。
2.  **Cognification (Cognee 风格)**: 后台任务提取实体关系，存入 Semantic Graph。
3.  **Conflict Resolution (Mem0 风格)**: 检测新事实是否与旧知识冲突。
4.  **Reflection (Stanford 风格)**: 产生高层洞察（例如：“用户经常在深夜编写 Python 代码，可能更喜欢异步处理”）。
5.  **Skill-fication (Voyager 风格)**: 将常用的操作序列固化。

---

## 5. 建议的技术选型

- **Orchestration**: LangGraph (状态机管理) / Letta (Agent 状态管理)。
- **Memory Store**: 
    - **Vector**: LanceDB / Qdrant。
    - **Graph**: Neo4j / Kuzu (用于 Graphiti)。
    - **Relational**: PostgreSQL (带 pgvector)。
- **Cognitive Logic**: 自定义反射循环 (Reflexion) + 背景任务调度。

---

## 6. 参考文献与项目

- **MemGPT/Letta**: [GitHub](https://github.com/letta-ai/letta) - 虚拟上下文管理。
- **Zep/Graphiti**: [GitHub](https://github.com/getzep/graphiti) - 动态图谱记忆。
- **Mem0**: [GitHub](https://github.com/mem0ai/mem0) - 原子事实提取。
- **Cognee**: [GitHub](https://github.com/topoteretes/cognee) - 认知控制面。
- **Voyager**: [GitHub](https://github.com/MineDojo/Voyager) - 技能库学习。
- **Stanford Generative Agents**: [Paper](https://arxiv.org/abs/2304.03442) - 记忆流与反思。
