from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from tools import (
    save_note,
    read_notes,
    search_notes,
    update_note,
    delete_note
)

router = APIRouter()


class NoteCreate(BaseModel):
    text: str


class NoteUpdate(BaseModel):
    text: str


@router.post("/notes", status_code=201)
def create_note(note: NoteCreate):
    return save_note(note.text)


@router.get("/notes")
def get_notes():
    return read_notes()


@router.get("/notes/search")
def search_note(keyword: str):
    return search_notes(keyword)


@router.put("/notes/{note_id}")
def update_note_endpoint(note_id: int, note: NoteUpdate):
    result = update_note(note_id, note.text)

    if result == "Invalid note number.":
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    return result


@router.delete("/notes/{note_id}")
def delete_note_endpoint(note_id: int):
    result = delete_note(note_id)

    if result == "Invalid note number.":
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    return result