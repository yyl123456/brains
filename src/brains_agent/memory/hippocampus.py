import os
from typing import List, Dict, Any
from mem0 import Memory
from loguru import logger

class Hippocampus:
    """
    海马体 (Hippocampus) - 多层记忆系统
    集成了 Mem0 用于长期事实记忆，并预留了 Zep/Graphiti 的集成接口。
    """
    def __init__(self, user_id: str = "default_user"):
        self.user_id = user_id
        # 初始化 Mem0
        try:
            self.memory = Memory()
            logger.info("Hippocampus initialized with Mem0.")
        except Exception as e:
            logger.error(f"Failed to initialize Mem0: {e}")
            self.memory = None

    async def store_fact(self, content: str, metadata: Dict[str, Any] = None):
        """
        将信息固化为原子事实 (Encoding)
        """
        if self.memory:
            self.memory.add(content, user_id=self.user_id, metadata=metadata)
            logger.debug(f"Stored fact for {self.user_id}: {content[:50]}...")

    async def retrieve_context(self, query: str) -> List[Dict[str, Any]]:
        """
        根据查询检索相关背景 (Retrieval)
        """
        if self.memory:
            results = self.memory.search(query, user_id=self.user_id)
            return results
        return []

    async def clear_memory(self):
        if self.memory:
            self.memory.delete_all(user_id=self.user_id)
