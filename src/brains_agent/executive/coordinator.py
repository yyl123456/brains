import json
from typing import TypedDict, Annotated, List, Union, Dict, Any
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from brains_agent.memory.hippocampus import Hippocampus
from brains_agent.tools.registry import registry
from loguru import logger
import operator

PLAN_PROMPT = """你是一个智能体的前额叶 (Prefrontal Cortex)，负责制定任务计划。
你的目标是将用户的请求拆解为一系列逻辑步骤。

当前可用的工具 (基底神经节技能):
{tools_schema}

检索到的背景记忆 (海马体):
{context}

用户当前请求:
{task}

请输出一个 JSON 格式的计划，包含以下字段:
1. "thought": 你的推理过程。
2. "plan": 一个简单的字符串，描述整体计划。
3. "next_step": 下一步要执行的动作（如果是直接回答用户，填 "respond"；如果要调用工具，填工具名称）。
4. "parameters": 调用工具所需的参数（字典格式，如果不调用工具则为空）。
5. "is_complete": 布尔值，标识任务是否已完成。

只输出 JSON，不要包含任何其他文字。"""

class AgentState(TypedDict):
    """
    工作记忆 (Working Memory) - 任务执行中的临时状态
    """
    messages: Annotated[List[BaseMessage], operator.add]
    context: List[str]
    current_plan: str
    next_step: str
    parameters: Dict[str, Any]
    task_completed: bool

class PrefrontalCortex:
    """
    前额叶 (Prefrontal Cortex) - 增强版逻辑中枢
    利用 LangGraph 实现状态驱动的任务编排。
    """
    def __init__(self, hippocampus: Hippocampus):
        self.hippocampus = hippocampus
        self.llm = ChatOpenAI(model="gpt-4o", temperature=0) 
        self.workflow = self._build_workflow()

    def _build_workflow(self):
        graph = StateGraph(AgentState)

        # 定义节点
        graph.add_node("loader", self._load_context)
        graph.add_node("planner", self._generate_plan)
        graph.add_node("executor", self._execute_action)
        graph.add_node("reflector", self._reflect)

        # 定义边
        graph.set_entry_point("loader")
        graph.add_edge("loader", "planner")
        graph.add_edge("planner", "executor")
        graph.add_edge("executor", "reflector")
        
        # 决策边：判断任务是否完成
        graph.add_conditional_edges(
            "reflector",
            self._should_continue,
            {
                "continue": "planner",
                "end": END
            }
        )

        return graph.compile()

    async def _load_context(self, state: AgentState):
        logger.debug("Loading context from Hippocampus...")
        last_message = state['messages'][-1].content
        facts = await self.hippocampus.retrieve_context(last_message)
        context_strings = [f["text"] for f in facts]
        return {"context": context_strings}

    async def _generate_plan(self, state: AgentState):
        logger.debug("Generating plan using LLM...")
        
        tools_schema = json.dumps(registry.get_tool_schemas(), ensure_ascii=False, indent=2)
        context_str = "\n".join(state["context"])
        task_str = state["messages"][-1].content

        prompt = PLAN_PROMPT.format(
            tools_schema=tools_schema,
            context=context_str,
            task=task_str
        )

        response = await self.llm.ainvoke([SystemMessage(content=prompt)])
        
        try:
            # 去除可能存在的 markdown 格式
            clean_content = response.content.replace("```json", "").replace("```", "").strip()
            plan_data = json.loads(clean_content)
            logger.info(f"Plan generated: {plan_data['thought']}")
            
            return {
                "current_plan": plan_data["plan"],
                "next_step": plan_data["next_step"],
                "parameters": plan_data.get("parameters", {}),
                "task_completed": plan_data["is_complete"]
            }
        except Exception as e:
            logger.error(f"Failed to parse plan JSON: {e}. Content: {response.content}")
            return {"next_step": "respond", "task_completed": True}

    async def _execute_action(self, state: AgentState):
        next_step = state["next_step"]
        logger.info(f"Executing action: {next_step}")

        if next_step == "respond":
            # 如果是直接回答，调用 LLM 生成最终响应
            response = await self.llm.ainvoke(state["messages"])
            return {"messages": [AIMessage(content=response.content)], "task_completed": True}
        
        try:
            # 调用工具 (基底神经节)
            result = await registry.execute(next_step, **state["parameters"])
            return {
                "messages": [AIMessage(content=f"工具执行结果 ({next_step}): {result}")],
                "task_completed": False # 执行完工具后通常需要反思
            }
        except Exception as e:
            logger.error(f"Tool execution failed: {e}")
            return {"messages": [AIMessage(content=f"错误: 工具 {next_step} 执行失败。")], "task_completed": True}

    async def _reflect(self, state: AgentState):
        logger.debug("Reflecting on task progress...")
        # 此处可以增加更复杂的自评逻辑
        return {"task_completed": state.get("task_completed", True)}

    def _should_continue(self, state: AgentState):
        if state.get("task_completed"):
            return "end"
        return "continue"

    async def execute_task(self, task_description: str) -> str:
        initial_state = {
            "messages": [HumanMessage(content=task_description)],
            "context": [],
            "current_plan": "",
            "next_step": "",
            "parameters": {},
            "task_completed": False
        }
        
        final_state = await self.workflow.ainvoke(initial_state)
        
        # 固化记忆
        last_response = final_state['messages'][-1].content
        await self.hippocampus.store_fact(f"Task: {task_description}. Response: {last_response}")
        
        return last_response
