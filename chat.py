from config import client
from prompts import SYSTEM_PROMPT
from openai import RateLimitError, AuthenticationError
from memory import load_memory, save_memory, clear_memory

from tools import (
    save_note,
    read_notes,
    list_notes,
    search_notes,
    delete_note,
    update_note
)

import json
import inspect


messages = load_memory()

if not messages:
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]


# Tool Registry
TOOLS = {
    "save_note": save_note,
    "read_notes": read_notes,
    "list_notes": list_notes,
    "search_notes": search_notes,
    "delete_note": delete_note,
    "update_note": update_note
}


def start_chat():
    print("AI Chat started. Type 'exit' to quit.")

    while True:
        user_input = input("You: ")

        # Exit
        if user_input.lower() == "exit":
            break

        # Clear memory
        if user_input.lower() == "clear":
            clear_memory()

            messages.clear()

            messages.append({
                "role": "system",
                "content": SYSTEM_PROMPT
            })

            print("Memory cleared.")
            continue

        # Add user message to conversation
        messages.append({
            "role": "user",
            "content": user_input
        })

        try:
            # Send conversation to GPT
            response = client.chat.completions.create(
                model="gpt-5",
                messages=messages
            )

            # Get GPT response
            ai_reply = response.choices[0].message.content

            # Convert JSON string → Python dictionary
            data = json.loads(ai_reply)

            # Get requested action
            action = data["action"]

            # Find the function from the registry
            tool = TOOLS.get(action)

            if tool:

                # Copy GPT arguments
                arguments = data.copy()

                # Remove action because the function doesn't need it
                arguments.pop("action")

                # Inspect the selected function
                signature = inspect.signature(tool)

                # Get its parameters
                required = signature.parameters

                # Find missing arguments
                missing = [
                    name
                    for name in required
                    if name not in arguments
                ]

                # If arguments are missing
                if missing:
                    result = f"Missing arguments: {', '.join(missing)}"

                # Otherwise execute the tool
                else:
                    result = tool(**arguments)

                # Show result to user
                print("AI:", result)

                # Save AI result to conversation memory
                messages.append({
                    "role": "assistant",
                    "content": result
                })

                save_memory(messages)

            else:
                print("AI: Unknown action.")

        except AuthenticationError:
            print("Invalid API key.")

        except RateLimitError:
            print("No API credits available.")

        except Exception as e:
            print("Unexpected error:", e)


# if __name__ == "__main__":
#     start_chat()









# from config import client
# from prompts import SYSTEM_PROMPT
# from openai import RateLimitError, AuthenticationError
# from memory import load_memory, save_memory, clear_memory
# from tools import save_note, read_notes, delete_note
# import json
# import inspect

# messages = load_memory()

# if not messages:
#     messages = [
#         {
#             "role": "system",
#             "content": SYSTEM_PROMPT
#         }
#     ]

# # Tool Registry
# TOOLS = {
#     "save_note": save_note,
#     "read_notes": read_notes,
#     "delete_note": delete_note
# }


# def start_chat():
#     print("AI Chat started. Type 'exit' to quit.")

#     while True:
#         user_input = input("You: ")

#         if user_input.lower() == "exit":
#             break

#         if user_input.lower() == "clear":
#             clear_memory()

#             messages.clear()

#             messages.append({
#                 "role": "system",
#                 "content": SYSTEM_PROMPT
#             })

#             print("Memory cleared.")
#             continue

#         messages.append({
#             "role": "user",
#             "content": user_input
#         })

#         try:
#             response = client.chat.completions.create(
#                 model="gpt-5",
#                 messages=messages
#             )

#             ai_reply = response.choices[0].message.content
#             data = json.loads(ai_reply)

#             action = data["action"]
#             tool = TOOLS.get(action)

#             if tool:
#                 arguments = data.copy()
#                 arguments.pop("action")

#                 signature = inspect.signature(tool)
#                 required = signature.parameters

#                 missing = [
#                     name for name in required
#                     if name not in arguments
#                 ]

#                 if missing:
#                     result = f"Missing arguments: {', '.join(missing)}"
#                 else:
#                     result = tool(**arguments)

#                 print("AI:", result)

#                 messages.append({
#                     "role": "assistant",
#                     "content": result
#                 })

#                 save_memory(messages)

#             else:
#                 print("AI: Unknown action.")

#         except AuthenticationError:
#             print("Invalid API key.")

#         except RateLimitError:
#             print("No API credits available.")

#         except Exception as e:
#             print("Unexpected error:", e)