
from database import (
    add_note as db_add_note,
    get_notes as db_get_notes,
    delete_note as db_delete_note,
    update_note as db_update_note,
    search_notes as db_search_notes
)



def save_note(text):
    return db_add_note(text)


def read_notes():
    return db_get_notes()


def list_notes():
    return db_get_notes()


def search_notes(keyword):
    # We'll connect this to SQLite in the next step.
    # For now, this tool is not converted yet.
    return "Search notes is not connected to the database yet."


def delete_note(index):
    return db_delete_note(index)


def update_note(index, text):
    return db_update_note(index, text)

def search_notes(keyword):
    return db_search_notes(keyword)















# def save_note(text):
#     with open("notes.txt", "a") as file:
#         file.write(text + "\n")

#     return "Note saved successfully."


# def read_notes():
#     try:
#         with open("notes.txt", "r") as file:
#             content = file.read()

#         if content.strip() == "":
#             return "No notes found."

#         return content

#     except FileNotFoundError:
#         return "No notes found."


# def list_notes():
#     try:
#         with open("notes.txt", "r") as file:
#             notes = file.readlines()

#         if not notes:
#             return "No notes found."

#         result = ""

#         for i, note in enumerate(notes, start=1):
#             result += f"{i}. {note.strip()}\n"

#         return result.strip()

#     except FileNotFoundError:
#         return "No notes found."


# def search_notes(keyword):
#     try:
#         with open("notes.txt", "r") as file:
#             notes = file.readlines()

#         results = []

#         for i, note in enumerate(notes, start=1):
#             if keyword.lower() in note.lower():
#                 results.append(f"{i}. {note.strip()}")

#         if not results:
#             return "No matching notes found."

#         return "\n".join(results)

#     except FileNotFoundError:
#         return "No notes found."


# def delete_note(index):
#     try:
#         with open("notes.txt", "r") as file:
#             notes = file.readlines()

#         if index < 1 or index > len(notes):
#             return "Invalid note number."

#         deleted = notes.pop(index - 1)

#         with open("notes.txt", "w") as file:
#             file.writelines(notes)

#         return f"Deleted note: {deleted.strip()}"

#     except FileNotFoundError:
#         return "No notes found."
    
#     def update_note(index, text):
#         try:
#             with open("notes.txt", "r") as file:
#                 notes = file.readlines()

#         if index < 1 or index > len(notes):
#             return "Invalid note number."

#         notes[index - 1] = text + "\n"

#         with open("notes.txt", "w") as file:
#             file.writelines(notes)

#         return f"Updated note {index}: {text}"

#         except FileNotFoundError:
#         return "No notes found."



