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
    return db_search_notes(keyword)


def delete_note(index):
    return db_delete_note(index)


def update_note(index, text):
    return db_update_note(index, text)