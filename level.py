from turtle import Turtle

class Level(Turtle):

    def __init__(self, level, canvas_height):
        super().__init__()
        self.canvas_height = canvas_height
        self.level = level
        self.go_there()
        self.write_score()

    def go_there(self):
        self.ht()
        self.penup()
        self.goto(0, self.canvas_height/2 - 30)

    def write_score(self):
        self.write(f"Level {self.level}", align="center", font=("Courier", 30, "bold"))

    def game_over(self):
        self.goto(0, self.canvas_height/2 - 80)
        self.write("Game Over", align="center", font=("Courier", 30, "bold"))
