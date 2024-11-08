def sync_notes_with_database():
    for note_file in os.listdir("Notes"):
        note_title = note_file.replace(".txt", "")
        if not note_exists_in_db(note_title):
            with open(f"Notes/{note_file}", "r") as file:
                create_note_in_db(note_title, file.read())

def update_note_from_cloud(note_id, cloud_service):
    cloud_content = cloud_service.fetch_note_content(note_id)
    update_note_content(note_id, cloud_content)
