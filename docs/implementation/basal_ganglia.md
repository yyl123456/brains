# 模块实现：基底神经节 (Basal Ganglia)

## 1. 定位
基底神经节是 Agent 的 **技能与动作系统**。

## 2. 核心功能
- **工具注册 (Tool Registry)**：管理可用的外部函数和 API。
- **动作选择 (Action Selection)**：根据前额叶的计划选择最佳工具。
- **自动化策略 (Habitual Actions)**：针对高频任务形成执行习惯。

## 3. 当前实现状态
- **模块路径**：`src/brains_agent/tools/`
- **主要文件**：
    - `registry.py`：工具注册引擎。
    - `definitions.py`：具体工具实现。
- **已上线的技能**：
    - `get_current_time`：获取系统时间。
    - `list_directory`：列出文件目录。
    - `read_file`：读取文件内容。
    - `write_file`：写入/覆盖文件。

## 4. 下一步计划
- [ ] **代码即技能 (Voyager 模式)**：支持 Agent 动态编写并注册 Python 脚本作为新技能。
- [ ] **沙箱执行**：为文件系统和 Shell 动作提供隔离的执行环境。
- [ ] **多步骤习惯**：将常用的工具组合固化为单一动作。
