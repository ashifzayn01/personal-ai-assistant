from tools import (
    save_note,
    read_notes,
    list_notes,
    search_notes,
    delete_note,
    update_note
)


TOOLS = {
    "save_note": save_note,
    "read_notes": read_notes,
    "list_notes": list_notes,
    "search_notes": search_notes,
    "delete_note": delete_note,
    "update_note": update_note
}


action = "delete_note"

tool = TOOLS.get(action)

print(tool)