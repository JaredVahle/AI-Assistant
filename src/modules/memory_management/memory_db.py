import sqlite3

def init_memory_db():
    conn = sqlite3.connect("memory.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS commands (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            command TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS preferences (
            key TEXT PRIMARY KEY,
            value TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS facts (
            fact TEXT PRIMARY KEY,
            details TEXT
        )
    ''')
    conn.commit()
    conn.close()

def store_command(command):
    conn = sqlite3.connect("memory.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO commands (command) VALUES (?)", (command,))
    conn.commit()
    conn.close()

def set_preference(key, value):
    conn = sqlite3.connect("memory.db")
    cursor = conn.cursor()
    cursor.execute("REPLACE INTO preferences (key, value) VALUES (?, ?)", (key, value))
    conn.commit()
    conn.close()

def get_preference(key):
    conn = sqlite3.connect("memory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT value FROM preferences WHERE key = ?", (key,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def store_fact(fact, details):
    conn = sqlite3.connect("memory.db")
    cursor = conn.cursor()
    cursor.execute("REPLACE INTO facts (fact, details) VALUES (?, ?)", (fact, details))
    conn.commit()
    conn.close()

def recall_fact(fact):
    conn = sqlite3.connect("memory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT details FROM facts WHERE fact = ?", (fact,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

# Storing and referring to prior commands
command = "search_notes_for: 'favorite movies'"
store_command(command)

# Retrieve recent commands
recent_command = "What did I search for last time?"
if "last time" in recent_command:
    # Fetch last command and reference it
    last_command = get_last_command()
    print(f"Last command was: {last_command}")

# User preferences for avatar expressions or game
set_preference("favorite_game", "Pong")
favorite_game = get_preference("favorite_game")
if favorite_game:
    print(f"Would you like to play {favorite_game} again?")
