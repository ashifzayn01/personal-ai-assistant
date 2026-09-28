from langchain_openai import ChatOpenAI

from agent.registry import TOOLS


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

llm_with_tools = llm.bind_tools(list(TOOLS.values()))