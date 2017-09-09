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
turtle.goto(5,130)
turtle.pendown()
turtle.write("Y")

turtle.penup()
turtle.goto(0,0)
turtle.pendown()



for x in range(0, 100):
    turtle.goto(x, (1/100)*x*x)

turtle.penup()
turtle.goto(0,0)
turtle.pendown()

for x in range(0, -100,-1):
    turtle.goto(x,(1/100)* x*x)
    
turtle.exitonclick()


    
