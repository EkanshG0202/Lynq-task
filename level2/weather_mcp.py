from fastmcp import FastMCP

mcp = FastMCP("weather-mcp")

@mcp.tool()
def get_weather(city: str) -> str:
    """
    Returns the weather for a given city.
    For now, this just returns mock data.
    Replace with an API call (like OpenWeather) if needed.
    """

    return f"The weather in {city} is Sunny, 30°C."

if __name__ == "__main__":
    mcp.run()
