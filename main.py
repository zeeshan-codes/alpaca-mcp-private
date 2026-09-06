import os

# In V2, we must use build_server() instead of importing an initialized mcp object
from alpaca_mcp_server.server import build_server

# Ensure the required Alpaca credentials exist before booting
if not os.getenv("ALPACA_API_KEY") or not os.getenv("ALPACA_SECRET_KEY"):
    raise ValueError(
        "Missing Alpaca API credentials. "
        "Ensure ALPACA_API_KEY and ALPACA_SECRET_KEY are set in the deployment environment."
    )

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    print(f"Starting Alpaca MCP Server V2 on port {port}...")
    
    # Initialize the server instance
    server = build_server()
    
    # Run the server using Server-Sent Events (SSE)
    server.run(transport="sse", host="0.0.0.0", port=port)
