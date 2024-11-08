def tag_note(note_id, tag):
    add_tag_to_db(note_id, tag)  # Adds tag to the database for this note

def filter_notes_by_tag(tag):
    return get_notes_with_tag_from_db(tag)

def search_text_in_notes(text):
    results = []
    for note in list_all_notes():
        content = read_note(note['id'])
        if text in content:
            results.append(note)
    return results

def replace_text_in_notes(search_text, replace_text):
    for note in list_all_notes():
        content = read_note(note['id'])
        updated_content = content.replace(search_text, replace_text)
        update_note_content(note['id'], updated_content)
