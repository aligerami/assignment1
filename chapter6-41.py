import turtle
import random
import math
turtle.penup()
turtle.goto(-125,-50)
turtle.pendown()

turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)


for i in range (0,10):
    random_x = random.randint(-125, -25)
    random_y=random.randint(-50,50)
    turtle.penup()
    turtle.goto(random_x,random_y)
    turtle.pendown()
    turtle.dot("red")

turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.dot("red")
turtle.circle(50)

for i in range (0,10):
    random_x=random.randint(25,75)
    random_y = random.randint(-25,25)
    if(math.sqrt(math.pow(random_x-50,2)+math.pow(random_y,2))<=50):
        print("x is ",random_x," y is:",random_y," distanc is :",math.sqrt(math.pow(random_x-50,2)+math.pow(random_y,2)))
        turtle.penup()
        turtle.goto(random_x,random_y)
        turtle.pendown()
        turtle.dot("blue")
    else:
        i=i-1
turtle.exitonclick()
    
