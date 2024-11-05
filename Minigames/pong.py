class PongGame:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=400, height=300, bg="black")
        self.canvas.pack()

        # Ball and Paddle
        self.ball = self.canvas.create_oval(190, 140, 210, 160, fill="white")
        self.paddle = self.canvas.create_rectangle(180, 280, 220, 290, fill="blue")

        self.canvas.bind("<Left>", self.move_left)
        self.canvas.bind("<Right>", self.move_right)
        self.canvas.focus_set()

        # Start Ball Motion
        self.ball_dx = 3
        self.ball_dy = 3
        self.animate_ball()

    def animate_ball(self):
        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)
        pos = self.canvas.coords(self.ball)

        # Bounce on walls
        if pos[0] <= 0 or pos[2] >= 400:
            self.ball_dx = -self.ball_dx
        if pos[1] <= 0:
            self.ball_dy = -self.ball_dy

        # Bounce on paddle
        paddle_pos = self.canvas.coords(self.paddle)
        if pos[3] >= paddle_pos[1] and paddle_pos[0] < pos[2] < paddle_pos[2]:
            self.ball_dy = -self.ball_dy

        # Game Over
        if pos[3] >= 300:
            self.canvas.create_text(200, 150, text="Game Over", fill="red", font=("Helvetica", 24))

        else:
            self.master.after(20, self.animate_ball)

    def move_left(self, event):
        self.canvas.move(self.paddle, -20, 0)

    def move_right(self, event):
        self.canvas.move(self.paddle, 20, 0)

# Run Pong game
pong_window = tk.Toplevel(app)
PongGame(pong_window)
