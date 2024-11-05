def log_error(error):
    with open("error_log.txt", "a") as log:
        log.write(f"{datetime.now()} - {str(error)}\n")

def validate_note_content(content):
    if len(content) == 0:
        raise ValueError("Content cannot be empty")
    return True

def run_unit_tests():
    assert create_note("Test Note", "Sample content")
    assert len(list_all_notes()) > 0
    print("All tests passed!")
