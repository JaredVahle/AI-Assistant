def list_all_notes():
    return get_all_notes_from_db()  # Fetches list of all notes from the database

def delete_all_notes():
    for note in list_all_notes():
        delete_note(note['id'])  # Delete each note

def export_notes_to_folder(destination_folder):
    os.makedirs(destination_folder, exist_ok=True)
    for note in list_all_notes():
        with open(note['file_path'], "r") as original:
            with open(f"{destination_folder}/{note['title']}.txt", "w") as copy:
                copy.write(original.read())
