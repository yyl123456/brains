from fastapi import FastAPI
from brains_agent.core.thalamus import Thalamus, SenseInput
from brains_agent.memory.hippocampus import Hippocampus
from brains_agent.executive.coordinator import PrefrontalCortex
from brains_agent.safety.cerebellum import Cerebellum
from brains_agent.tools.registry import registry
import brains_agent.tools.definitions # Ensure tools are registered
import uvicorn

app = FastAPI(title="Brains Agent API")
thalamus = Thalamus()
hippocampus = Hippocampus()
prefrontal = PrefrontalCortex(hippocampus)
cerebellum = Cerebellum()

@app.get("/")
async def root():
    return {"status": "online", "system": "Brains Agent v2"}

@app.post("/sense")
async def sense(input_data: SenseInput):
    """
    模拟感觉输入网关 (Thalamus)
    """
    sensory_result = await thalamus.process_input(input_data)
    
    if sensory_result.get("status") == "rejected":
        return sensory_result

    if sensory_result["routing_target"] == "prefrontal_cortex":
        # 1. Execute
        raw_response = await prefrontal.execute_task(input_data.content)
        
        # 2. Refine (Cerebellum)
        final_response = await cerebellum.refine_output(raw_response, sensory_result["intent"])
        
        return {
            "sensory_analysis": sensory_result,
            "response": final_response
        }
    
    return sensory_result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
