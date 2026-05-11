# Brains Agent Architecture Design

## 1. Introduction

Brains Agent 旨在构建一个模拟人类认知过程的高度结构化智能体。本方案结合了当前最前沿的 Agent 框架（如 Claude Code）和记忆系统（如 Mem0），并深度借鉴脑科学中的功能分区，设计出一套可解释、可演化的认知架构。

## 2. Overall Architecture (脑启发映射)

我们将 Agent 的功能模块与脑区进行 1:1 映射，形成以下层次结构：

| 模块名称 (Agent Module) | 模拟脑区 (Brain Region) | 核心职责 (Responsibilities) | 参考技术/项目 |
| :--- | :--- | :--- | :--- |
| **Sense & Router** | 丘脑 (Thalamus) | 输入过滤、多模态分发、注意力权重分配 | LLM Router, Message Filtering |
| **Working Memory** | 海马体 (短期) | 最近对话上下文、实时任务状态 | Context Window, LRU Cache |
| **Long-term Memory** | 海马体 (长期) | 原子事实提取、个性化偏好、关联检索 | **Mem0**, Vector DB, Graph Store |
| **Cognitive Engine** | 大脑皮层 (Cortex) | 语言理解、逻辑推理、知识储备 | Claude 3.5/4, GPT-4, Llama 3 |
| **Executive Function** | 前额叶 (Prefrontal) | 目标分解、计划生成、反思与调整 | Task Coordinator, ReAct |
| **Action Selector** | 基底神经节 | 工具调用选择、策略执行、习惯性行为 | Tool Use, Function Calling |
| **Safety & Risk** | 杏仁核 (Amygdala) | 风险评估、安全过滤、情绪响应倾向 | Guardrails, Sentiment Analysis |
| **Refiner & Monitor** | 小脑 (Cerebellum) | 输出校准、自我纠错、响应优化 | Self-Correction Loops, Evaluators |
| **System State** | 下丘脑 & 脑干 | 令牌消耗监控、运行心跳、基础 I/O | Telemetry, Rate Limiting |

---

## 3. Core Components Detail

### 3.1 记忆系统 (Hippocampus / Memory System)
借鉴 **Mem0** 的核心思想，我们的记忆系统采用“原子事实”存储模式，而非简单的聊天记录堆叠：
- **Hierarchical Storage (分层存储)**:
    - **User Level**: 用户的长期偏好、性格特征、职业背景。
    - **Session Level**: 当前任务的特定知识（如：“正在处理 repo-A 的重构”）。
    - **Agent Level**: Agent 自身学到的操作经验（如：“处理这类错误时，先检查环境变量”）。
- **Fact Extraction & Consolidation (事实提取与整合)**:
    - **Atomic Extraction**: 使用 LLM 将对话流实时转化为独立的、不可分割的事实单元。
    - **Conflict Resolution**: 当新输入与既有记忆矛盾时（如：用户之前说喜欢 Python，现在说改用 Go），系统通过 LLM 进行判断，决定是更新记忆还是保留冲突作为不同阶段的偏好。
    - **Entity Linking**: 对关键实体（项目名、变量、人名）进行关联映射，提高检索的精准度。
- **Hybrid Retrieval (混合检索)**:
    - 结合 **Vector Search** (语义相关性) 和 **Keyword/Entity Matching** (精确匹配)。

### 3.2 决策与计划 (Prefrontal Cortex / Executive Function)
借鉴 **Claude Code** 的 `Coordinator` 模式：
- **Goal Decomposition**: 将复杂指令分解为 `Sub-tasks`。
- **Plan, Act, Observe Loop**: 标准的循环机制，但增加了“反思”步骤。
- **Priority Management**: 根据任务紧急程度和资源消耗动态调整处理顺序。

### 3.3 执行与工具 (Basal Ganglia / Action System)
- **Tool Registry**: 类似于脑区的“技能存储”。
- **Execution Engine**: 负责具体的工具调用（File system, Shell, API）。
- **Feedback Loop**: 工具执行结果反馈给“小脑”进行评估。

### 3.4 评估与修正 (Cerebellum / Refinement)
- **Self-Critique**: 在输出前进行自我检查。
- **Consistency Check**: 确保输出与长期记忆中的事实不冲突。

---

## 4. Data Flow (信息流转过程)

1. **Sensory Input**: 用户输入（文本/代码）进入系统。
2. **Thalamic Routing**: 丘脑识别意图，过滤噪声，确定处理优先级。
3. **Hippocampal Retrieval**: 同时从持久记忆（Mem0 风格）检索相关背景，注入上下文。
4. **Cortical Reasoning**: 大脑皮层（LLM）结合上下文进行推理。
5. **Prefrontal Planning**: 前额叶生成初步计划。
6. **Basal Ganglia Execution**: 选定工具并执行。
7. **Cerebellar Refinement**: 对执行结果或生成文本进行校准。
8. **Hippocampal Encoding**: 任务完成后，将新学到的事实或偏好“固化”到长期记忆中。

---

## 5. Implementation Roadmap (实施路线图)

- **Phase 1 (Infrastructure)**: 构建基础的 LLM 调用接口与工具执行框架（基底神经节）。
- **Phase 2 (Memory)**: 集成 Mem0 风格的记忆提取与检索机制（海马体）。
- **Phase 3 (Executive)**: 实现任务编排与复杂计划能力（前额叶）。
- **Phase 4 (Refinement)**: 引入自我纠错与安全风控模块（小脑 & 杏仁核）。

---

## 6. References

- [Mem0: The memory layer for AI Agents](https://github.com/mem0ai/mem0)
- [Claude Code Source Analysis (Internal Research)](~/workspace/llmss/agent/claude-code-source-code)
- [Brains Agent Documentation](docs/brain-structure-detailed.md)
