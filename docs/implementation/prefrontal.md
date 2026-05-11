# 模块实现：前额叶 (Prefrontal Cortex)

## 1. 定位
前额叶是 Brains Agent 的 **中央执行机构**。它负责逻辑推理、任务拆解、决策制定以及跨模块的协调。

## 2. 核心功能
- **目标设定 (Goal Setting)**：解析原始意图，确立最终目标。
- **动态计划 (Dynamic Planning)**：将目标分解为可执行的子任务序列。
- **工作记忆管理 (Working Memory)**：在任务执行期间，维护临时的上下文状态。
- **反思与调整 (Reflection)**：根据执行结果实时修正计划。

## 3. 当前实现状态
- **模块路径**：`src/brains_agent/executive/coordinator.py`
- **当前版本**：v0.2 (LLM 驱动的 JSON 计划)
- **技术栈**：Python, LangGraph, LangChain, GPT-4o

## 4. 逻辑流程
1. **Context Loading (loader)**：从海马体检索相关原子事实。
2. **Strategy Formulation (planner)**：
    - 调用 LLM，传入 **Tool Registry** 的 Schema、上下文和当前任务。
    - LLM 输出结构化的 JSON 计划，包含 `thought` (推理)、`next_step` (下一步动作) 和 `parameters` (工具参数)。
3. **Execution (executor)**：
    - 如果 `next_step` 为 `respond`，则生成最终回复。
    - 如果为工具名称，则通过基底神经节执行对应工具。
4. **Reflection (reflector)**：评估执行结果，决定是继续下一步计划还是结束任务。
5. **Memory Consolidation**：任务完成后，将全过程固化回海马体。

## 5. 待优化项
- [x] 集成 LangGraph 实现状态机控制的任务流。
- [ ] 引入更复杂的自省 (Self-Introspection) 逻辑，减少幻觉。
- [ ] 支持长程任务的分层计划 (Hierarchical Planning)。
