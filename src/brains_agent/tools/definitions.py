import os
import datetime
import subprocess
from typing import Dict, Any
from brains_agent.tools.registry import registry, ToolMetadata

# --- 工具定义 ---

async def get_current_time() -> str:
    """获取当前的日期和时间。"""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

async def list_directory(path: str = ".") -> str:
    """列出指定目录下的文件和文件夹。"""
    try:
        items = os.listdir(path)
        return "\n".join(items)
    except Exception as e:
        return f"Error listing directory: {str(e)}"

async def read_file(file_path: str) -> str:
    """读取指定文件的内容。"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"

async def write_file(file_path: str, content: str) -> str:
    """向指定文件写入内容。"""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"Successfully wrote to {file_path}"
    except Exception as e:
        return f"Error writing file: {str(e)}"

# --- 注册工具 ---

registry.register_tool(ToolMetadata(
    name="get_current_time",
    description="获取当前的日期和时间。",
    parameters={}
))(get_current_time)

registry.register_tool(ToolMetadata(
    name="list_directory",
    description="列出指定目录下的文件和文件夹。",
    parameters={
        "type": "object",
        "properties": {
            "path": {"type": "string", "description": "要列出的目录路径，默认为当前目录 '.'"}
        }
    }
))(list_directory)

registry.register_tool(ToolMetadata(
    name="read_file",
    description="读取指定文本文件的内容。",
    parameters={
        "type": "object",
        "properties": {
            "file_path": {"type": "string", "description": "文件的完整路径"}
        },
        "required": ["file_path"]
    }
))(read_file)

registry.register_tool(ToolMetadata(
    name="write_file",
    description="向指定文件写入文本内容（会覆盖原内容）。",
    parameters={
        "type": "object",
        "properties": {
            "file_path": {"type": "string", "description": "文件的完整路径"},
            "content": {"type": "string", "description": "要写入的内容"}
        },
        "required": ["file_path", "content"]
    }
))(write_file)
