from turtle import Turtle, Screen

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 250)
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score : {self.score}", align="center", font=("Courier", 18, "normal"))
        
    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align="center", font=("Courier", 18, "normal"))
        