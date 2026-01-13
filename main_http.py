# main_http.py
from mcp.server.fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
import uvicorn

# Import the shared MCP instance
from server import mcp

# Import tools so they get registered
import tools.employment_tools

# Health check endpoint
async def ping(_):
    return JSONResponse({"ok": True, "service": "World Bank Employment MCP Server"})

# Create Starlette app with routes
app = Starlette(routes=[
    Route("/ping", ping),
])

# Mount MCP Streamable HTTP app at /mcp
app.mount("/mcp", mcp.streamable_http_app())

if __name__ == "__main__":
    print("Starting World Bank Employment MCP Server on http://127.0.0.1:8001")
    print("MCP endpoint: http://127.0.0.1:8001/mcp")
    print("Health check: http://127.0.0.1:8001/ping")
    uvicorn.run(app, host="127.0.0.1", port=8001, log_level="info")
