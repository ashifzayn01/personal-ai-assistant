from langchain_core.messages import HumanMessage, ToolMessage

from agent.registry import TOOLS


def run_agent(user_input: str, model=None, max_steps: int = 5):
    if model is None:
        from agent.llm import llm_with_tools
        model = llm_with_tools

    messages = [HumanMessage(content=user_input)]

    for step in range(max_steps):
        response = model.invoke(messages)

        messages.append(response)

        if not response.tool_calls:
            return response.content

        for tool_call in response.tool_calls:
            tool_name = tool_call["name"]
            tool_args = tool_call["args"]
            tool_id = tool_call["id"]

            tool = TOOLS.get(tool_name)

            if tool is None:
                result = f"Error: Unknown tool '{tool_name}'"
            else:
                try:
                    result = tool.invoke(tool_args)

                    print(f"Tool: {tool_name}")
                    print(f"Arguments: {tool_args}")
                    print(f"Result: {result}")

                except Exception as error:
                    result = f"Tool execution failed: {error}"

            messages.append(
                ToolMessage(
                    content=str(result),
                    tool_call_id=tool_id,
                )
            )

    return "Agent stopped: maximum tool-calling steps reached."