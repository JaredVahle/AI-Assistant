# src/main.py - Main entry point for the assistant

from assistant.note_manager import NoteManager
from assistant.memory_manager import MemoryManager
from nlp.nlp import NLPProcessor
from games.pong import PongGame
import config

def main():
    # Initialize assistant components
    note_manager = NoteManager()
    memory_manager = MemoryManager()
    nlp_processor = NLPProcessor()
    
    # Example usage
    note_manager.create_note("Hello, this is a test note.")
    response = nlp_processor.analyze_text("How's the weather today?")
    
    # Start interactive loop, games, etc.
    pong = PongGame()
    pong.start()

if __name__ == "__main__":
    main()
