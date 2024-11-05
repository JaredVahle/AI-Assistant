def backup_note_to_file(note_id):
    content = read_note(note_id)
    backup_path = f"Backup/{note_id}_backup.txt"
    with open(backup_path, "w") as file:
        file.write(content)

def restore_note_from_file(file_path):
    with open(file_path, "r") as file:
        title = os.path.basename(file_path).replace("_backup.txt", "")
        content = file.read()
    create_note(title, content)

def archive_note(note_id):
    file_path = fetch_file_path_from_db(note_id)
    archive_path = f"Archive/{os.path.basename(file_path)}"
    os.rename(file_path, archive_path)
    update_file_path_in_db(note_id, archive_path)

def load_notes_from_directory(dir_path):
    for filename in os.listdir(dir_path):
        with open(f"{dir_path}/{filename}", "r") as file:
            create_note(filename.replace(".txt", ""), file.read())
