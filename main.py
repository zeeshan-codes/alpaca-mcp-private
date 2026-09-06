import os

# Import the pre-configured server directly from the Alpaca package
from alpaca_mcp_server.server import mcp

# Ensure the required Alpaca credentials exist before booting
if not os.getenv("ALPACA_API_KEY") or not os.getenv("ALPACA_SECRET_KEY"):
    raise ValueError(
        "Missing Alpaca API credentials. "
        "Ensure ALPACA_API_KEY and ALPACA_SECRET_KEY are set in the deployment environment."
    )

if __name__ == "__main__":
    # MCP Hosting automatically assigns a port via the PORT environment variable.
    # We default to 8000 if it's not found.
    port = int(os.getenv("PORT", 8000))
    
    print(f"Starting Alpaca MCP Server on port {port}...")
    
    # Run the server using Server-Sent Events (SSE) so it can be accessed over HTTP
    mcp.run(transport="sse", host="0.0.0.0", port=port)