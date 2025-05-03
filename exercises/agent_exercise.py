from pydantic_ai import Agent, Tool, RunContext
from pydantic_graph import End


agent = Agent(
    model="gpt-3.5-turbo",
)


async def main_iter(prompt):
    nodes = []
    async with agent.iter(prompt) as agent_run:
        async for node in agent_run:
            nodes.append(node)
    print(nodes)


async def main_next(prompt):
    async with agent.iter(prompt) as agent_run:
        node = agent_run.next_node
        all_nodes = [node]
        while not isinstance(node, End):
            node = await agent_run.next(node)
            all_nodes.append(node)


def main(prompt):
    result = agent.run_sync(prompt)


if __name__ == "__main__":
    prompt = "What is the capital of France?"
    # main_iter(prompt)
    # main_next(prompt)
    main(prompt)
