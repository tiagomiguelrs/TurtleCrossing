from turtle import Turtle
from random import choice, randint

CAR_WIDTH = 1
CAR_LENGTH = 1.5
CAR_COLORS = ["yellow", "orange", "red", "green", "blue", "purple"]

class Car(Turtle):

    def __init__(self, canvas_width, canvas_height):
        super().__init__()
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        # self.speed = randint(1, 5)  # Not a good idea to have different speeds. Creates traffic.
        self.build_car()

    def build_car(self):
        self.shape("square")
        self.penup()
        self.color(choice(CAR_COLORS))
        self.setheading(180)
        self.shapesize(stretch_wid=CAR_WIDTH, stretch_len=CAR_LENGTH)

    def position(self, lanes):
        lane = randint(1, lanes)
        self.goto(self.canvas_width/2 + 90, -self.canvas_height/2 + 60 + lane * 40)

    def initial_position(self, lanes):
        lane = randint(1, lanes)
        xpos = randint(-self.canvas_width//2, self.canvas_width//2)
        self.goto(xpos, -self.canvas_height/2 + 60 + lane * 40)

    def move(self):
        self.fd(5)

    def collision(self, position: tuple[int, int]):
        if self.distance(position) < 25:
            return True

