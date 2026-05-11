from typing import Dict, Any
from loguru import logger

class Amygdala:
    """
    杏仁核 (Amygdala) - 风险评估与情绪标记
    负责识别潜在风险、安全过滤以及评估任务的重要性。
    """
    def __init__(self):
        self.risk_keywords = ["delete", "rm -rf", "kill", "format"]

    async def assess_risk(self, content: str) -> Dict[str, Any]:
        """
        评估输入的风险等级
        """
        is_risky = any(kw in content.lower() for kw in self.risk_keywords)
        importance = 5 # Default importance
        
        if is_risky:
            logger.warning(f"High risk detected in input: {content}")
            return {"level": "high", "action": "block", "reason": "Detected risky keywords."}
        
        return {"level": "low", "action": "allow", "importance": importance}
