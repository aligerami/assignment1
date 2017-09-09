import turtle
import math

turtle.penup()
turtle.goto(-200,0)
turtle.pendown()
turtle.forward(400)
turtle.left(160)
turtle.forward(10)
turtle.goto(200,0)
turtle.left(40)
turtle.forward(10)
turtle.left(160)

turtle.penup()
turtle.goto(0,-150)
turtle.pendown()
turtle.left(90)
turtle.forward(300)
turtle.left(20)
turtle.backward(10)
turtle.goto(0,150)
turtle.right(40)
turtle.backward(10)

turtle.penup()
turtle.goto(100,-10)
turtle.pendown()
turtle.write("2π")
turtle.penup()
turtle.goto(-100,-10)
turtle.pendown()
turtle.write("-2π")

turtle.penup()
turtle.goto(-175,50)
turtle.pendown()



for x in range(-175, 176):
    turtle.color("red")
    turtle.goto(x, 50 * math.sin((x / 100) * 2 * math.pi))
turtle.penup()
turtle.goto(-175,0)
turtle.pendown()
for x in range(-175, 176):
    turtle.color("blue")
    turtle.goto(x, 50 * math.cos((x / 100) * 2 * math.pi))
