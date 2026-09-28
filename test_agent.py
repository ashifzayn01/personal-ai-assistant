from langchain_core.messages import AIMessage
from agent.agent import run_agent


class MockModel:
    def __init__(self):
        self.call_count = 0
        self.note_id = None

    def invoke(self, messages):
        self.call_count += 1
        print(f"\n--- LLM call {self.call_count} ---")

        # Step 1: Save a new note
        if self.call_count == 1:
            return AIMessage(
                content="",
                tool_calls=[
                    {
                        "name": "save_note",
                        "args": {
                            "text": "TEST_AGENT_NOTE"
                        },
                        "id": "call_1",
                        "type": "tool_call",
                    }
                ],
            )

        # Step 2: Read notes and find our test note's ID
        if self.call_count == 2:
            return AIMessage(
                content="",
                tool_calls=[
                    {
                        "name": "read_notes",
                        "args": {},
                        "id": "call_2",
                        "type": "tool_call",
                    }
                ],
            )

        if self.call_count == 3:
            notes = messages[-1].content
            print("Notes returned by SQLite:")
            print(notes)

            for line in notes.splitlines():
                if "TEST_AGENT_NOTE" in line:
                    self.note_id = int(line.split(".", 1)[0])
                    break

            if self.note_id is None:
                return AIMessage(
                    content="Could not find the test note."
                )

            print("Test note ID:", self.note_id)

            # Step 3: Search for the test note
            return AIMessage(
                content="",
                tool_calls=[
                    {
                        "name": "search_notes",
                        "args": {
                            "keyword": "TEST_AGENT_NOTE"
                        },
                        "id": "call_3",
                        "type": "tool_call",
                    }
                ],
            )

        # Step 4: Update the test note
        if self.call_count == 4:
            return AIMessage(
                content="",
                tool_calls=[
                    {
                        "name": "update_note",
                        "args": {
                            "index": self.note_id,
                            "text": "UPDATED_TEST_AGENT_NOTE"
                        },
                        "id": "call_4",
                        "type": "tool_call",
                    }
                ],
            )

        # Step 5: Delete the test note
        if self.call_count == 5:
            return AIMessage(
                content="",
                tool_calls=[
                    {
                        "name": "delete_note",
                        "args": {
                            "index": self.note_id
                        },
                        "id": "call_5",
                        "type": "tool_call",
                    }
                ],
            )

        # Step 6: Read notes again to verify deletion
        if self.call_count == 6:
            return AIMessage(
                content="",
                tool_calls=[
                    {
                        "name": "read_notes",
                        "args": {},
                        "id": "call_6",
                        "type": "tool_call",
                    }
                ],
            )

        # Final response
        if self.call_count == 7:
            print("Final tool result:", messages[-1].content)
            return AIMessage(
                content="All five tools have been tested."
            )


mock_model = MockModel()

result = run_agent(
    "Test all five note tools.",
    model=mock_model,
    max_steps=7,
)

print("\nFinal response:", result)





























# from langchain_core.messages import AIMessage

# from agent.agent import run_agent


# class MockModel:
#     def __init__(self):
#         self.call_count = 0

#     def invoke(self, messages):
#         self.call_count += 1

#         print(f"\nLLM call: {self.call_count}")

#         if self.call_count == 1:
#             print("Model is requesting save_note")

#             return AIMessage(
#                 content="",
#                 tool_calls=[
#                     {
#                         "name": "save_note",
#                         "args": {
#                             "text": "I need to study LangGraph."
#                         },
#                         "id": "call_123",
#                         "type": "tool_call",
#                     }
#                 ],
#             )

#         print("Model received the tool result:")
#         print(messages[-1].content)

#         return AIMessage(
#             content="Your note has been saved successfully."
#         )


# mock_model = MockModel()

# result = run_agent(
#     "Save a note about studying LangGraph.",
#     model=mock_model,
# )

# print("\nFinal response:", result)