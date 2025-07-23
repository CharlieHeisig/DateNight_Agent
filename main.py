from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor


load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

llm = ChatOpenAI(model="gpt-4o", temperature=1.0, max_tokens=1000)
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages([
    ("system", 
     """
     You are a helpful research and planning assistant.
    Answer the user query and use necessary tools.
    Wrap the output in this format and provide no other text\n{format_instructions}
    """
    ),
    ("placeholder","{chat_history}"),
    ("human", "{query}"),
    ("placeholder","{agent_scratchpad}"),
]).partial(format_instructions=parser.get_format_instructions())

agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools = []
)

agent_executor = AgentExecutor(
    agent=agent, tools=[], verbose=True,)
raw_response = agent_executor.invoke({
    "query": "What are some romantic date ideas?",
})
print(raw_response)

try:
    structured_response = parser.parse(raw_response["output"])
except Exception as e:
    print("Error parsing response:", e, "Raw response:", raw_response)