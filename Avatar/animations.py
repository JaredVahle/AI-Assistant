import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import random

# Initialize main app window
app = tk.Tk()
app.title("Interactive ChatGPT Assistant")

# Label to display the avatar animation
avatar_label = tk.Label(app)
avatar_label.grid(row=0, column=0, padx=10, pady=10)

# Load animations (replace with actual paths)
surfing_frames = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open("surfing.gif"))]
filing_frames = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open("filing.gif"))]
thinking_frames = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open("thinking.gif"))]
error_frames = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open("error.gif"))]

# Function to play an animation (surfing, filing, thinking, error)
def play_animation(frames):
    def animate(counter=0):
        frame = frames[counter % len(frames)]
        avatar_label.config(image=frame)
        app.after(100, animate, counter+1)  # Adjust timing for speed
    animate()

# Functions to trigger different animations based on tasks
def play_surfing_animation():
    play_animation(surfing_frames)

def play_filing_animation():
    play_animation(filing_frames)

def play_thinking_animation():
    play_animation(thinking_frames)

def play_error_animation():
    play_animation(error_frames)

# Sample usage - replace with real task triggers
play_surfing_animation()  # Call this when ChatGPT is fetching from the web
# play_filing_animation()  # Call this when accessing the database
# play_thinking_animation()  # Call this during complex processing
# play_error_animation()  # Call this when an error occurs

app.mainloop()

import tkinter as tk
import random
from PIL import Image, ImageTk, ImageSequence

# Load your different idle animations here
blinking_frames = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open("blink.gif"))]
looking_around_frames = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open("look_around.gif"))]

def play_idle_animation():
    # Randomly choose between blinking or looking around
    idle_animation = random.choice([blinking_frames, looking_around_frames])
    play_animation(idle_animation)

def play_animation(frames):
    def animate(counter=0):
        frame = frames[counter % len(frames)]
        avatar_label.config(image=frame)
        app.after(100, animate, counter+1)  # Adjust timing for speed
    animate()

def reset_idle_timer():
    app.after_cancel(idle_timer)
    start_idle_timer()

def start_idle_timer():
    global idle_timer
    idle_timer = app.after(30000, play_idle_animation)  # Play idle animation after 30 seconds

app = tk.Tk()
app.title("Interactive AI Companion")

# Setup avatar label and idle timer
avatar_label = tk.Label(app)
avatar_label.grid(row=0, column=0)
start_idle_timer()

# Call reset_idle_timer() whenever user interacts
app.mainloop()
