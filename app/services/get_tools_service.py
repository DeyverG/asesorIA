from app.utils.settings import settings
from langchain_mcp_adapters.client import MultiServerMCPClient


def get_tools_service():

    client =  MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["-m", "app.tools.math_tools"],
                "transport": "stdio",
            },
        }
    )

    return client

