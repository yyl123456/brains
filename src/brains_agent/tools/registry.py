import asyncio
from typing import Dict, Any, Callable, List
from pydantic import BaseModel, Field

class ToolMetadata(BaseModel):
    name: str
    description: str
    parameters: Dict[str, Any]

class ToolRegistry:
    """
    基底神经节 (Basal Ganglia) - 工具注册与执行引擎
    负责管理 Agent 可用的技能与工具。
    """
    def __init__(self):
        self._tools: Dict[str, Callable] = {}
        self._metadata: Dict[str, ToolMetadata] = {}

    def register_tool(self, metadata: ToolMetadata):
        def decorator(func: Callable):
            self._tools[metadata.name] = func
            self._metadata[metadata.name] = metadata
            return func
        return decorator

    def get_tool_schemas(self) -> List[Dict[str, Any]]:
        return [m.dict() for m in self._metadata.values()]

    async def execute(self, name: str, **kwargs) -> Any:
        if name not in self._tools:
            raise ValueError(f"Tool '{name}' not found in registry.")
        
        func = self._tools[name]
        if hasattr(func, "__call__"):
             # Simple execution for now
             return await func(**kwargs) if asyncio.iscoroutinefunction(func) else func(**kwargs)
        return None

# Global Registry
registry = ToolRegistry()
