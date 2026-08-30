from tools import (
    save_note,
    read_notes,
    list_notes,
    search_notes,
    delete_note,
    update_note
)

import inspect


# Same registry we use in chat.py
TOOLS = {
    "save_note": save_note,
    "read_notes": read_notes,
    "list_notes": list_notes,
    "search_notes": search_notes,
    "delete_note": delete_note,
    "update_note": update_note
}


# Pretend this came from GPT
data = {
    "action": "save_note",
    "text": "Test from chat layer"
}


# Get the action
action = data["action"]

# Find the correct function
tool = TOOLS.get(action)

if tool:
    # Copy arguments
    arguments = data.copy()

    # Remove action because the tool doesn't need it
    arguments.pop("action")

    # Inspect the function
    signature = inspect.signature(tool)

    # Get its parameters
    required = signature.parameters

    # Find missing arguments
    missing = [
        name
        for name in required
        if name not in arguments
    ]

    if missing:
        result = f"Missing arguments: {', '.join(missing)}"
    else:
        result = tool(**arguments)

    print("Result:", result)

else:
    print("Unknown action.")