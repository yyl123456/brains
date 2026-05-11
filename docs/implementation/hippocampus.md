# 模块实现：海马体 (Hippocampus)

## 1. 定位
海马体负责 Agent 的 **多层级存储系统**。

## 2. 核心功能
- **原子事实提取 (Fact Extraction)**：利用 Mem0 将非结构化对话转化为离散事实。
- **关联检索 (Associative Retrieval)**：基于向量相似度召回背景信息。
- **记忆固化 (Consolidation)**：将短期交互经验转化为长期知识。

## 3. 当前实现状态
- **模块路径**：`src/brains_agent/memory/hippocampus.py`
- **集成工具**：Mem0
- **当前功能**：支持基础的 `add` 和 `search` 操作。

## 4. 路线图
- [ ] 集成 Zep 以实现基于知识图谱的深度记忆检索。
- [ ] 增加“记忆遗忘”机制，处理过时或错误的信息。
