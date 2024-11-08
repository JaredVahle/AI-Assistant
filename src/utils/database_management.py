def backup_database():
    shutil.copy("notes.db", "Backup/notes_backup.db")

def optimize_database():
    conn = sqlite3.connect("notes.db")
    conn.execute("VACUUM")
    conn.close()

def check_database_integrity():
    conn = sqlite3.connect("notes.db")
    integrity = conn.execute("PRAGMA integrity_check").fetchone()[0]
    conn.close()
    return integrity == "ok"
