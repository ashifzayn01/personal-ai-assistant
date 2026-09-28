from langchain_core.tools import tool

from tools import (
    save_note as existing_save_note,
    read_notes as existing_read_notes,
    search_notes as existing_search_notes,
    delete_note as existing_delete_note,
    update_note as existing_update_note,
)


@tool
def save_note(text: str) -> str:
    """Save a new note."""
    return existing_save_note(text)


@tool
def read_notes() -> str:
    """Read all saved notes."""
    return existing_read_notes()


@tool
def search_notes(keyword: str) -> str:
    """Search saved notes using a keyword."""
    return existing_search_notes(keyword)


@tool
def delete_note(index: int) -> str:
    """Delete a note using its index."""
    return existing_delete_note(index)


@tool
def update_note(index: int, text: str) -> str:
    """Update an existing note using its index and new text."""
    return existing_update_note(index, text)