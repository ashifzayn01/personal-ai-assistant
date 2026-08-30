import sqlite3

connection = sqlite3.connect("notes.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL
)
""")

connection.commit()

connection.close()


import sqlite3


def add_note(text):
    connection = None

    try:
        connection = sqlite3.connect("notes.db")
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO notes (text) VALUES (?)",
            (text,)
        )

        connection.commit()

        return "Note added successfully."

    except sqlite3.Error as e:
        return f"Database error: {e}"

    finally:
        if connection:
            connection.close()
            
    
    
def get_notes():
    connection = None

    try:
        connection = sqlite3.connect("notes.db")
        cursor = connection.cursor()

        cursor.execute(
            "SELECT id, text FROM notes"
        )

        notes = cursor.fetchall()

        if not notes:
            return "No notes found."

        result = ""

        for note_id, text in notes:
            result += f"{note_id}. {text}\n"

        return result.strip()

    except sqlite3.Error as e:
        return f"Database error: {e}"

    finally:
        if connection:
            connection.close()
            
            
def delete_note(index):
    connection = None

    try:
        connection = sqlite3.connect("notes.db")
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM notes WHERE id = ?",
            (index,)
        )

        if cursor.rowcount == 0:
            return "Invalid note number."

        connection.commit()

        return "Note deleted successfully."

    except sqlite3.Error as e:
        return f"Database error: {e}"

    finally:
        if connection:
            connection.close()    
        
                
def update_note(index, text):
    connection = None

    try:
        connection = sqlite3.connect("notes.db")
        cursor = connection.cursor()

        cursor.execute(
            "UPDATE notes SET text = ? WHERE id = ?",
            (text, index)
        )

        if cursor.rowcount == 0:
            return "Invalid note number."

        connection.commit()

        return f"Updated note {index}: {text}"

    except sqlite3.Error as e:
        return f"Database error: {e}"

    finally:
        if connection:
            connection.close()                           
            
            
            
def search_notes(keyword):
    connection = None

    try:
        connection = sqlite3.connect("notes.db")
        cursor = connection.cursor()

        cursor.execute(
            "SELECT id, text FROM notes WHERE text LIKE ?",
            (f"%{keyword}%",)
        )

        notes = cursor.fetchall()

        if not notes:
            return "No matching notes found."

        result = ""

        for note_id, text in notes:
            result += f"{note_id}. {text}\n"

        return result.strip()

    except sqlite3.Error as e:
        return f"Database error: {e}"

    finally:
        if connection:
            connection.close()            