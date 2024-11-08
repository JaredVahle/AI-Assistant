def toggle_dark_mode():
    # Sample toggle logic (assuming a tkinter-based GUI)
    dark_mode = not dark_mode
    app.config(bg="black" if dark_mode else "white")

def display_word_count(note_id):
    content = read_note(note_id)
    word_count = len(content.split())
    print(f"Word Count: {word_count}")  # Or display in GUI

def spell_check_note_content(note_id):
    from spellchecker import SpellChecker
    spell = SpellChecker()
    content = read_note(note_id)
    errors = spell.unknown(content.split())
    return errors
