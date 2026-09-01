from fastapi import FastAPI

from routers.notes import router as notes_router
from routers.chat import router as chat_router

app = FastAPI()

app.include_router(notes_router)
app.include_router(chat_router)








# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel

# from tools import (
#     save_note,
#     read_notes,
#     search_notes,
#     update_note,
#     delete_note
# )

# app = FastAPI()


# # ---------- Request Models ----------

# class NoteCreate(BaseModel):
#     text: str


# class NoteUpdate(BaseModel):
#     text: str


# # ---------- CREATE ----------

# @app.post("/notes", status_code=201)
# def create_note(note: NoteCreate):
#     return save_note(note.text)


# # ---------- READ ALL ----------

# @app.get("/notes")
# def get_notes():
#     return read_notes()


# # ---------- SEARCH ----------

# @app.get("/notes/search")
# def search_note(keyword: str):
#     return search_notes(keyword)


# # ---------- UPDATE ----------

# @app.put("/notes/{note_id}")
# def update_note_endpoint(note_id: int, note: NoteUpdate):
#     result = update_note(note_id, note.text)

#     if result == "Invalid note number.":
#         raise HTTPException(
#             status_code=404,
#             detail="Note not found"
#         )

#     return result


# # ---------- DELETE ----------

# @app.delete("/notes/{note_id}")
# def delete_note_endpoint(note_id: int):
#     result = delete_note(note_id)

#     if result == "Invalid note number.":
#         raise HTTPException(
#             status_code=404,
#             detail="Note not found"
#         )

#     return result