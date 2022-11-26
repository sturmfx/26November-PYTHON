import turtle
import time
import random
score = 0
screen = turtle.Screen()
screen.title("BASIC SNAKE GAME")
screen.bgcolor("black")
screen.setup(width=500, height=500)
screen.tracer(0)

snake_head = turtle.Turtle()
snake_head.speed(0)
snake_head.shape("square")
snake_head.color("red")
snake_head.penup()
snake_head.goto(0, 0)

snake_food = turtle.Turtle()
snake_food.speed(0)
snake_food.shape("circle")
snake_food.color("white")
snake_food.penup()
snake_food.goto(0, 200)

def up():
    if snake_head.heading != 270:
        snake_head.heading = 90


def down():
    if snake_head.heading != 90:
        snake_head.heading = 270


def left():
    if snake_head.heading != 0:
        snake_head.heading = 180


def right():
    if snake_head.heading != 180:
        snake_head.heading = 0


def snake_move():
    if snake_head.heading == 90:
        y = snake_head.ycor()
        snake_head.sety(y + 10)
    if snake_head.heading == 270:
        y = snake_head.ycor()
        snake_head.sety(y - 10)
    if snake_head.heading == 0:
        x = snake_head.xcor()
        snake_head.setx(x + 10)
    if snake_head.heading == 180:
        x = snake_head.xcor()
        snake_head.setx(x - 10)


screen.listen()
screen.onkeypress(up, "w")
screen.onkeypress(down, "s")
screen.onkeypress(right, "d")
screen.onkeypress(left, "a")

while True:
    screen.update()
    if snake_head.xcor() > 250 or snake_head.xcor() < - 250 or snake_head.ycor() > 250 or snake_head.ycor() < -250:
        time.sleep(3)
        snake_head.goto(0, 0)
        snake_head.heading = 0
    if snake_head.distance(snake_food) < 10:
        score = score + 10
        screen.title("SCORE IS: " + str(score))
        x = random.randint(-240, 240)
        y = random.randint(-240, 240)
        snake_food.goto(x, y)
    snake_move()
    time.sleep(0.1)
screen.mainloop()

