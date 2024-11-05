import sqlite3
import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, simpledialog

# Set up the Notes directory
NOTES_DIR = "Notes"
os.makedirs(NOTES_DIR, exist_ok=True)

# Database setup (SQLite)
def init_db():
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            file_path TEXT UNIQUE,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Functions for CRUD operations
def add_note():
    title = simpledialog.askstring("New Note", "Enter note title:")
    if title:
        file_path = os.path.join(NOTES_DIR, f"{title}.txt")
        with open(file_path, "w") as file:  # Create an empty file
            pass
        conn = sqlite3.connect('notes.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO notes (title, file_path) VALUES (?, ?)", (title, file_path))
        conn.commit()
        conn.close()
        load_notes()
    else:
        messagebox.showwarning("Input Error", "Title cannot be empty.")

def load_notes():
    notes_list.delete(0, tk.END)
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, title FROM notes")
    for note in cursor.fetchall():
        notes_list.insert(tk.END, note)
    conn.close()

def view_note():
    selected = notes_list.curselection()
    if selected:
        note_id = notes_list.get(selected[0])[0]
        conn = sqlite3.connect('notes.db')
        cursor = conn.cursor()
        cursor.execute("SELECT title, file_path FROM notes WHERE id = ?", (note_id,))
        note = cursor.fetchone()
        conn.close()
        note_title.set(note[0])
        note_content.delete("1.0", tk.END)
        with open(note[1], "r") as file:
            note_content.insert(tk.END, file.read())
    else:
        messagebox.showwarning("Selection Error", "Please select a note to view.")

def save_note():
    selected = notes_list.curselection()
    if selected:
        note_id = notes_list.get(selected[0])[0]
        title = note_title.get()
        content = note_content.get("1.0", tk.END).strip()
        
        # Update file with the new content
        conn = sqlite3.connect('notes.db')
        cursor = conn.cursor()
        cursor.execute("SELECT file_path FROM notes WHERE id = ?", (note_id,))
        file_path = cursor.fetchone()[0]
        with open(file_path, "w") as file:
            file.write(content)
        
        # Update title in database if changed
        new_file_path = os.path.join(NOTES_DIR, f"{title}.txt")
        if file_path != new_file_path:
            os.rename(file_path, new_file_path)
            cursor.execute("UPDATE notes SET title = ?, file_path = ? WHERE id = ?", (title, new_file_path, note_id))
        conn.commit()
        conn.close()
        load_notes()
    else:
        messagebox.showwarning("Selection Error", "Please select a note to save.")

def delete_note():
    selected = notes_list.curselection()
    if selected:
        note_id = notes_list.get(selected[0])[0]
        conn = sqlite3.connect('notes.db')
        cursor = conn.cursor()
        cursor.execute("SELECT file_path FROM notes WHERE id = ?", (note_id,))
        file_path = cursor.fetchone()[0]
        os.remove(file_path)  # Delete the file from the Notes folder
        cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        conn.commit()
        conn.close()
        load_notes()
        note_title.set("")
        note_content.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Selection Error", "Please select a note to delete.")

# Initialize database
init_db()

# GUI Setup
app = tk.Tk()
app.title("Note Manager")

# Left panel for note list
notes_list = tk.Listbox(app, width=30)
notes_list.grid(row=0, column=0, rowspan=5, padx=10, pady=10)
notes_list.bind("<<ListboxSelect>>", lambda e: view_note())

# Buttons for operations
btn_add = tk.Button(app, text="New Note", command=add_note)
btn_add.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
btn_save = tk.Button(app, text="Save Note", command=save_note)
btn_save.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
btn_delete = tk.Button(app, text="Delete Note", command=delete_note)
btn_delete.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

# Right panel for note details
note_title = tk.StringVar()
title_entry = tk.Entry(app, textvariable=note_title, width=50)
title_entry.grid(row=0, column=2, padx=10, pady=5, sticky="ew")

note_content = tk.Text(app, width=50, height=15)
note_content.grid(row=1, column=2, rowspan=4, padx=10, pady=5)

# Load initial notes
load_notes()

app.mainloop()
