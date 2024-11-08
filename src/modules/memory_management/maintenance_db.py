def create_backup():
    shutil.copytree("Notes", "Backup/Notes_Backup")

def restore_backup(backup_folder):
    shutil.copytree(backup_folder, "Notes")

def export_notes_as_txt():
    for note in list_all_notes():
        with open(f"Exported/{note['title']}.txt", "w") as file:
            file.write(read_note(note['id']))

def import_notes_from_text(folder_path):
    for filename in os.listdir(folder_path):
        with open(f"{folder_path}/{filename}", "r") as file:
            create_note(filename.replace(".txt", ""), file.read())
