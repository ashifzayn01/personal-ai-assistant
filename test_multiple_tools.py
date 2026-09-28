from langchain_core.messages import AIMessage
from agent.agent import run_agent


class MockModel:
    def __init__(self):
        self.call_count = 0

    def invoke(self, messages):
        self.call_count += 1

        print(f"\n--- LLM call {self.call_count} ---")

        if self.call_count == 1:
            print("Model is requesting two tools.")

            return AIMessage(
                content="",
                tool_calls=[
                    {
                        "name": "read_notes",
                        "args": {},
                        "id": "call_1",
                        "type": "tool_call",
                    },
                    {
                        "name": "search_notes",
                        "args": {
                            "keyword": "LangChain"
                        },
                        "id": "call_2",
                        "type": "tool_call",
                    },
                ],
            )

        print("Model received the tool results:")

        for message in messages:
            if message.type == "tool":
                print(message.content)

        return AIMessage(
            content="I have read your notes and searched for LangChain."
        )


mock_model = MockModel()

result = run_agent(
    "Read my notes and search for LangChain.",
    model=mock_model,
    max_steps=3,
)

print("\nFinal response:", result)