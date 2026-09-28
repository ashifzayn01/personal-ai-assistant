from langchain_core.messages import AIMessage
from agent.agent import run_agent


class MockModel:
    def __init__(self):
        self.call_count = 0

    def invoke(self, messages):
        self.call_count += 1

        print(f"\n--- LLM call {self.call_count} ---")

        if self.call_count == 1:
            print("Model is requesting an unknown tool.")

            return AIMessage(
                content="",
                tool_calls=[
                    {
                        "name": "send_email",
                        "args": {},
                        "id": "call_1",
                        "type": "tool_call",
                    }
                ],
            )

        if self.call_count == 2:
            print("Model is requesting delete_note with invalid arguments.")

            return AIMessage(
                content="",
                tool_calls=[
                    {
                        "name": "delete_note",
                        "args": {
                            "index": "invalid"
                        },
                        "id": "call_2",
                        "type": "tool_call",
                    }
                ],
            )

        if self.call_count == 3:
            print("Model received the error messages.")

            for message in messages:
                if message.type == "tool":
                    print(message.content)

            return AIMessage(
                content="I encountered and received both tool errors."
            )


mock_model = MockModel()

result = run_agent(
    "Test how the agent handles errors.",
    model=mock_model,
    max_steps=3,
)

print("\nFinal response:", result)