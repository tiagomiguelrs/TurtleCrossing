from turtle import Turtle

class Hero(Turtle):

    def __init__(self, canvas_height: int):
        super().__init__()
        self.canvas_height = canvas_height
        self.build_hero()
        self.start()

    def build_hero(self):
        self.shape("turtle")
        self.penup()
        self.setheading(90)

    def start(self):
        self.goto(x=0, y=-self.canvas_height / 2 + 50)

    def move_up(self):
        self.fd(5)

    def move_down(self):
        if self.ycor() > -self.canvas_height/2:
            self.bk(5)