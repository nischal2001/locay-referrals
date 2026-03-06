from tools.search_professionals_tool import SearchProfessionalsTool
from tools.mcp.search_professionals_schema import SEARCH_PROFESSIONALS_TOOL


class ToolRegistry:

    tools = {
        "search_professionals": SearchProfessionalsTool
    }

    schemas = [
        SEARCH_PROFESSIONALS_TOOL
    ]

    @staticmethod
    def execute(tool_name, arguments):

        tool = ToolRegistry.tools.get(tool_name)

        if not tool:
            raise Exception(f"Tool not found: {tool_name}")

        return tool.run(**arguments)