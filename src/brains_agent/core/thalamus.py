from typing import List, Dict, Any
from pydantic import BaseModel
from brains_agent.safety.amygdala import Amygdala

class SenseInput(BaseModel):
    content: str
    source: str = "user"
    metadata: Dict[str, Any] = {}

class Thalamus:
    """
    丘脑 (Thalamus) - 感觉网关与路由
    负责对输入进行初步解析、优先级排序及路由分发。
    """
    def __init__(self, model: Any = None):
        self.model = model
        self.amygdala = Amygdala()

    async def process_input(self, input_data: SenseInput) -> Dict[str, Any]:
        # 1. Risk Assessment (Amygdala)
        safety_check = await self.amygdala.assess_risk(input_data.content)
        if safety_check["action"] == "block":
            return {
                "original_input": input_data,
                "intent": "blocked_by_safety",
                "status": "rejected",
                "reason": safety_check["reason"]
            }

        # 2. Intent Recognition
        intent = "general_query"
        if "help" in input_data.content.lower():
            intent = "request_help"
        
        return {
            "original_input": input_data,
            "intent": intent,
            "priority": "normal",
            "routing_target": "prefrontal_cortex",
            "safety_context": safety_check
        }
