from pydantic_graph import Graph, Edge, End, GraphRun, GraphRunContext

import sys
from pathlib import Path

from pydantic_graph import End
from pydantic_graph.persistence.file import FileStatePersistence
from pydantic_ai.messages import ModelMessage  # noqa: F401
from example import Ask, Answer, Evaluate, QuestionState, question_graph


async def main():
    answer: str | None = sys.argv[1] if len(sys.argv) > 1 else None
    persistence = FileStatePersistence(Path("question_graph.json"))
    persistence.set_graph_types(question_graph)

    question_graph.run_sync(
        start_node=Ask(),
        state=QuestionState(question="What is the capital of France?"),
        persistence=persistence,
    )
