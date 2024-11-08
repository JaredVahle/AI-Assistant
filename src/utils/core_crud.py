def create_note(title, content=""):
    file_path = f"Notes/{title}.txt"
    with open(file_path, "w") as file:
        file.write(content)
    # Add entry to the database (assuming a function `add_to_database`)
    add_to_database(title, file_path)

def read_note(note_id):
    # Fetch note path from database and read content
    file_path = fetch_file_path_from_db(note_id)
    with open(file_path, "r") as file:
        return file.read()

def update_note_content(note_id, new_content):
    file_path = fetch_file_path_from_db(note_id)
    with open(file_path, "w") as file:
        file.write(new_content)

def delete_note(note_id):
    file_path = fetch_file_path_from_db(note_id)
    os.remove(file_path)
    delete_from_database(note_id)

def rename_note(note_id, new_title):
    file_path = fetch_file_path_from_db(note_id)
    new_path = f"Notes/{new_title}.txt"
    os.rename(file_path, new_path)
    update_file_path_in_db(note_id, new_path)
