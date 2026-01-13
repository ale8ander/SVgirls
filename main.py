# main.py
from server import mcp

# Import tools so they get registered via decorators
import tools.employment_tools

# Entry point to run the server in STDIO mode
if __name__ == "__main__":
    mcp.run()
