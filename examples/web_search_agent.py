import os
from pydantic_ai.agent import Agent
from pydantic_ai.common_tools.tavily import tavily_search_tool
import dotenv

dotenv.load_dotenv()

api_key = os.getenv("TAVILY_API_KEY")

assert api_key is not None


agent = Agent(
    "openai:o3-mini",
    tools=[tavily_search_tool(api_key)],
    system_prompt="Search Tavily for the given query and return the results.",
)

if __name__ == "__main__":
    response = agent.run_sync("Find LLM Agent frameworks")
    print(response)
