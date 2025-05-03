from dataclasses import dataclass

import httpx

from pydantic_ai import Agent, RunContext


@dataclass
class MyDeps:
    api_key: str
    http_client: httpx.Client


agent = Agent(
    "openai:gpt-4o",
    deps_type=MyDeps,
)


@agent.system_prompt
def get_system_prompt(ctx: RunContext[MyDeps]) -> str:
    response = ctx.deps.http_client.get(
        "https://example.com", headers={"Authorization": f"Bearer {ctx.deps.api_key}"}
    )
    response.raise_for_status()
    return f"Prompt: {response.text}"


async def main():
    deps = MyDeps("foobar", httpx.Client())
    result = await agent.run(
        "Tell me a joke.",
        deps=deps,
    )
    print(result.output)
    # > Did you hear about the toothpaste scandal? They called it Colgate.
