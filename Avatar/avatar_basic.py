import tkinter as tk
from PIL import Image, ImageTk

app = tk.Tk()
app.title("Note Manager with Avatar")

# Load Avatar Image
avatar_label = tk.Label(app)
avatar_label.grid(row=0, column=0, padx=10, pady=10)

# Load a default avatar image
avatar_image = ImageTk.PhotoImage(Image.open("avatar_default.png"))  # Use your avatar image path
avatar_label.config(image=avatar_image)

app.mainloop()

# Loading different avatar states
avatar_default = ImageTk.PhotoImage(Image.open("avatar_default.png"))
avatar_thinking = ImageTk.PhotoImage(Image.open("avatar_thinking.png"))
avatar_happy = ImageTk.PhotoImage(Image.open("avatar_happy.png"))

# Function to change the avatar based on events
def set_avatar(state="default"):
    if state == "thinking":
        avatar_label.config(image=avatar_thinking)
    elif state == "happy":
        avatar_label.config(image=avatar_happy)
    else:
        avatar_label.config(image=avatar_default)

def add_note():
    set_avatar("thinking")
    # Code to add note goes here...
    set_avatar("happy")

import pyttsx3

# Initialize TTS engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Example usage
def add_note():
    set_avatar("thinking")
    speak("Creating a new note...")
    # Code to add note...
    set_avatar("happy")
    speak("Note added successfully.")

def update_avatar_gif(gif_path):
    # Use an animated GIF as avatar
    frames = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open(gif_path))]
    def animate(counter=0):
        frame = frames[counter % len(frames)]
        avatar_label.config(image=frame)
        app.after(100, animate, counter+1)  # Adjust timing for speed
    animate()
