import os
from pydantic_ai.agent import Agent
from pydantic_ai.common_tools.tavily import tavily_search_tool
import dotenv
from pydantic import BaseModel

dotenv.load_dotenv()

api_key = os.getenv("TAVILY_API_KEY")

assert api_key is not None


class SearchResult(BaseModel):
    title: str
    description: str


class SearchResults(BaseModel):
    results: list[SearchResult]


agent = Agent(
    "openai:o3-mini",
    tools=[tavily_search_tool(api_key)],
    output_type=SearchResults,
    system_prompt="Search Tavily for the given query",
    instrument=True,
)

if __name__ == "__main__":
    import logfire

    logfire.configure()
    logfire.instrument_httpx()
    response = agent.run_sync(
        "Find LLM Agent frameworks."
        #  Do extra search for each framework you find to get extra details
    )
    print(response)
