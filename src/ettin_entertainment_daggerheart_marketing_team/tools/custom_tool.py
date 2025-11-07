import os
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class FileReadToolInput(BaseModel):
    """Input schema for SafeFileReadTool."""
    file_path: str = Field(..., description="The path to the file to be read.")

class SafeFileReadTool(BaseTool):
    name: str = "Read a file's content"
    description: str = "Read the content of a file. Use this to read files you have access to."
    args_schema: Type[BaseModel] = FileReadToolInput

    def _run(self, file_path: str) -> str:
        try:
            # Force UTF-8 encoding to prevent 'charmap' errors
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return f"Error: File not found at path: {file_path}"
        except Exception as e:
            return f"Error: Failed to read file {file_path}. {str(e)}"