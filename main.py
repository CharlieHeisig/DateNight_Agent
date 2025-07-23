
"""
DateNight Research Agent
-----------------------
Best practices: modular, type hints, logging, input flexibility, error handling, and maintainability.
"""

import logging
from typing import Any, Dict
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor


class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]


def setup_agent() -> AgentExecutor:
    """Initializes and returns the LangChain agent executor."""
    llm = ChatOpenAI(model="gpt-4o", temperature=0.2, max_tokens=1000)
    parser = PydanticOutputParser(pydantic_object=ResearchResponse)
    prompt = ChatPromptTemplate.from_messages([
        ("system",
         """
         You are a helpful research and planning assistant.
         Answer the user query and use necessary tools.
         Wrap the output in this format and provide no other text\n{format_instructions}
         """
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]).partial(format_instructions=parser.get_format_instructions())

    agent = create_tool_calling_agent(
        llm=llm,
        prompt=prompt,
        tools=[]
    )
    return AgentExecutor(agent=agent, tools=[], verbose=False), parser


def run_query(query: str, agent_executor: AgentExecutor, parser: PydanticOutputParser) -> ResearchResponse:
    """Runs the agent on the given query and returns a structured response."""
    try:
        raw_response: Dict[str, Any] = agent_executor.invoke({"query": query})
        return parser.parse(raw_response["output"])
    except Exception as e:
        logging.error(f"Error parsing response: {e}\nRaw response: {raw_response}")
        raise


def main() -> None:
    """Main entry point for the script."""
    import sys
    import argparse

    load_dotenv()

    parser_arg = argparse.ArgumentParser(description="DateNight Research Agent")
    parser_arg.add_argument("query", type=str, nargs="?", default="What are some romantic date ideas?",
                            help="The research query to run.")
    args = parser_arg.parse_args()

    agent_executor, parser = setup_agent()

    try:
        structured_response = run_query(args.query, agent_executor, parser)
        print(structured_response)
    except Exception:
        print("An error occurred. Check logs for details.")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    main()