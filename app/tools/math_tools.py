# math_server.py
from mcp.server.fastmcp import FastMCP

mcp_math = FastMCP("Math")
mcp_math.settings.port = 8200
@mcp_math.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b + 2

@mcp_math.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

if __name__ == "__main__":
    mcp_math.run(transport="stdio")


