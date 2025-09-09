# client_agent.py
import asyncio
import logging
from fastmcp import Client

# Optional: setup logging so you can see MCP messages
logging.basicConfig(level=logging.INFO)
log_handler = logging.getLogger("fastmcp")

async def main():
    # Point client to your MCP server script
    client = Client(
        "weather_mcp.py",   # path to your MCP tool server
        log_handler=log_handler,
        timeout=30.0
    )

    # Start the client (launches weather_mcp.py as a subprocess)
    await client.start()

    # Call the MCP tool exposed by the server
    result = await client.call("get_weather", city="Hyderabad")
    print("Response:", result)

    # Shut down
    await client.stop()

if __name__ == "__main__":
    asyncio.run(main())
