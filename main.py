from turtle import Turtle, Screen
from hero import Hero
from car import Car
from level import Level
from random import randint
from time import sleep

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600
LANES = 11
INIT_SPEED = 0.05
GAME_ON = True
NEXT_LEVEL = True

# build lanes
def build_lanes(lanes: int):
    lane_painter = Turtle()
    lane_painter.ht()
    lane_painter.color("gray")
    lane_painter.speed("fastest")
    lane_painter.penup()
    for lane in range(lanes):
        lane_painter.goto(CANVAS_WIDTH/2 + 60, -CANVAS_WIDTH/2 + 80 + lane * 40)
        lane_painter.pendown()
        lane_painter.goto(-CANVAS_WIDTH / 2 - 60, -CANVAS_WIDTH/2 + 80 + lane * 40)
        lane_painter.penup()
    del lane_painter


# Make background
screen = Screen()
screen.screensize(canvwidth=CANVAS_WIDTH, canvheight=CANVAS_HEIGHT)
screen.tracer(0)

# Build car container
cars = []

screen.listen()

l = 0
while NEXT_LEVEL:

    build_lanes(LANES + 1)
    level = Level(l+1, CANVAS_WIDTH)

    # Create hero
    hero = Hero(CANVAS_HEIGHT)

    # Create cars on the screen at the beginning of the game
    for i in range(30):
        cars.append(Car(CANVAS_WIDTH, CANVAS_HEIGHT))
        cars[i].initial_position(LANES)

    # It is important to create key bindings again because the clearscreen() method will clear them.
    screen.onkeypress(fun=hero.move_up, key="Up")
    screen.onkeypress(fun=hero.move_down, key="Down")

    while GAME_ON:
        # Move car
        for car in cars:
            car.move()

        # A new car will be created with a 20% chance
        if randint(1, 5) == 3:
            cars.append(Car(CANVAS_WIDTH, CANVAS_HEIGHT))
            cars[-1].position(LANES)

        # Detect collision with the turtle
        for car in cars:
            hero_x, hero_y = hero.pos()
            if car.collision((hero_x, hero_y)):
                level.game_over()
                print("Game Over")
                GAME_ON = False
                NEXT_LEVEL = False

        # Remove a car everytime it goes beyond the left limit. It prevents creation of infinite car objects.
        if cars[0].xcor() < -CANVAS_WIDTH/2 - 90:
            cars[0].clear()
            cars.pop(0)

        # If hero crosses all lanes, increase speed for next level.
        if hero.ycor() > 230:
            GAME_ON = False

        sleep(INIT_SPEED)
        screen.update()

    # If the level was completed, clear the car objects from the cars list, clear everything from the screen and restart again.
    if NEXT_LEVEL and not GAME_ON:
        INIT_SPEED *= 0.8
        cars.clear()
        screen.clearscreen()
        screen.tracer(0)    # Tracer after the screen clearing to create another tracer. The previous one must have been deleted.

        l += 1
        GAME_ON = True
    else:
        break

screen.mainloop()