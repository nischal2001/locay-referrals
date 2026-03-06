import os
import requests
from dotenv import load_dotenv
import json

from tools.tool_registry import ToolRegistry

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL")
MODEL = os.getenv("LLM_MODEL")


class ToolCallingAgent:

    @staticmethod
    def run(user_input):

        response = requests.post(
            f"{OPENROUTER_BASE_URL}/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": MODEL,
                "messages": [
                    {"role": "user", "content": user_input}
                ],
                "tools": ToolRegistry.schemas,
                "tool_choice": "auto"
            }
        )

        result = response.json()

        print("\nLLM Raw Response:\n", result)

        # Handle API error
        if "error" in result:
            raise Exception(f"OpenRouter API Error: {result['error']}")

        if "choices" not in result:
            raise Exception(f"Unexpected API response: {result}")

        message = result["choices"][0]["message"]

        # If no tool call happened
        if "tool_calls" not in message:
            return message.get("content", "No response")

        tool_call = message["tool_calls"][0]

        tool_name = tool_call["function"]["name"]
        arguments = json.loads(tool_call["function"]["arguments"])

        print("\nTool Called:", tool_name)
        print("Arguments:", arguments)

        return ToolRegistry.execute(tool_name, arguments)