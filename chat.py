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


def chat_with_ai(user_input):
    messages.append({
        "role": "user",
        "content": user_input
    })

    try:
        response = client.chat.completions.create(
            model="gpt-5",
            messages=messages
        )

        ai_reply = response.choices[0].message.content

        data = json.loads(ai_reply)

        action = data["action"]

        tool = TOOLS.get(action)

        if tool:
            arguments = data.copy()
            arguments.pop("action")

            signature = inspect.signature(tool)
            required = signature.parameters

            missing = [
                name
                for name in required
                if name not in arguments
            ]

            if missing:
                result = f"Missing arguments: {', '.join(missing)}"
            else:
                result = tool(**arguments)

            messages.append({
                "role": "assistant",
                "content": result
            })

            save_memory(messages)

            return result

        else:
            return "Unknown action."

    except AuthenticationError:
        return "Invalid API key."

    except RateLimitError:
        return "No API credits available."

    except Exception as e:
        return f"Unexpected error: {e}"


def start_chat():
    print("AI Chat started. Type 'exit' to quit.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        if user_input.lower() == "clear":
            clear_memory()

            messages.clear()

            messages.append({
                "role": "system",
                "content": SYSTEM_PROMPT
            })

            print("Memory cleared.")
            continue

        result = chat_with_ai(user_input)

        print("AI:", result)