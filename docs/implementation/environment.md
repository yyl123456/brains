# 环境配置记录 (Environment)

## 1. Python 运行环境
项目使用软链接形式关联全局/共享的虚拟环境：
- **软链接路径**：`.venv` -> `/home/yyl/.venv`
- **Python 版本**：`3.12.3`

## 2. 依赖管理
环境应包含以下核心依赖（记录于 `requirements.txt`）：
- `fastapi`, `uvicorn` (API 服务)
- `langchain`, `langchain-openai`, `langgraph` (认知引擎)
- `mem0ai` (海马体存储)
- `loguru` (系统日志)

## 3. 环境变量
项目依赖以下环境变量（配置于 `.env`）：
- `OPENAI_API_KEY`: LLM 调用凭证。
- `MEM0_API_KEY`: Mem0 服务凭证。

## 4. 激活方式
```bash
source .venv/bin/activate
```
