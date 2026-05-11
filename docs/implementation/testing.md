# Brains Agent 测试指南

## 1. 测试策略
Brains Agent 采用 **分层测试** 策略：
- **单元测试 (Unit Tests)**：验证单个脑区模块（如 Thalamus 的路由逻辑、Hippocampus 的存储接口）。
- **集成测试 (Integration Tests)**：验证跨模块的协作（如 Prefrontal 调用 Basal Ganglia 工具）。
- **端到端测试 (E2E Tests)**：模拟真实用户输入，验证从感知到执行的完整闭环。

## 2. 测试环境准备
1. 确保 `.env` 文件已配置 `OPENAI_API_KEY`。
2. 激活环境：
   ```bash
   source .venv/bin/activate
   ```
   (如果未配置环境，请运行 `bash setup_env.sh`)

## 3. 运行测试
使用以下命令运行集成测试：
```bash
pytest tests/test_agent_flow.py
```

## 4. 重点测试用例：多步动作编排
- **场景**：用户要求列出文件并写入新文件。
- **预期行为**：
    1. `Planner` 识别出需要两步操作。
    2. 第一步调用 `list_directory`。
    3. `Reflector` 发现任务未完成。
    4. 第二步调用 `write_file`。
    5. 最后 `Planner` 决定 `respond` 并结束任务。

## 5. 测试记录
| 日期 | 测试用例 | 状态 | 备注 |
| :--- | :--- | :--- | :--- |
| 2026-05-09 | 基础 API 连通性 | ✅ | / 接口返回 200 |
| 2026-05-09 | 危险词拦截 (杏仁核) | ✅ | 成功拦截 "rm -rf" 等指令 |
| 2026-05-09 | 多步工具调用 (list -> write) | ✅ | 自动编排并生成测试文件 |
