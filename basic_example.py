import os

import logfire
from pydantic import BaseModel

from pydantic_ai import Agent

# 'if-token-present' means nothing will be sent (and the example will work) if you don't have logfire configured
logfire.configure(
    send_to_logfire="if-token-present",
    console=logfire.ConsoleOptions(min_log_level="debug", verbose=True),
)


class MyModel(BaseModel):
    city: str
    country: str


model = os.getenv("PYDANTIC_AI_MODEL", "openai:gpt-4o")
print(f"Using model: {model}")
agent = Agent(model, output_type=MyModel, instrument=True)

if __name__ == "__main__":
    result = agent.run_sync("The windy city in the US of A.")
    print(result.output)
    print(result.usage())
