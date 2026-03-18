import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("❤️")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.width(2)

def heart(scale, color):
    t.color(color)
    t.begin_fill()
    for i in range(360):
        x = scale * 16 * math.sin(math.radians(i)) ** 3
        y = scale * (
            13 * math.cos(math.radians(i))
            - 5 * math.cos(2 * math.radians(i))
            - 2 * math.cos(3 * math.radians(i))
            - math.cos(4 * math.radians(i))
        )
        t.goto(x, y)
    t.end_fill()

# draw layers
for s in range(18, 13, -1):
    t.penup()
    t.goto(0, -10)
    t.pendown()
    heart(s, "#330000")

t.penup()
t.goto(0, -10)
t.pendown()
heart(14, "#ff1a1a")

t.penup()
t.goto(0, -170)
t.color("#ff4d6d")
t.write("143❤️", align="center", font=("Segoe UI", 22, "bold"))

turtle.done()