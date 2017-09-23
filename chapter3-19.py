import turtle
import math
x1=0
y1=10
x2=100
y2=200
x1=int(input("enter x for the first point"))
y1=int(input("enter y for the first point"))
x2=int(input("enter x for the second point"))
y2=int(input("enter y for the second point"))



m= (y2-y1)/(x2-x1)
angle=math.atan(m)*180/3.14
lenght=math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))
print(m)
print(angle)
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.left(angle)
turtle.forward(lenght)

turtle.penup()
turtle.goto(x1+5,y1)
turtle.pendown()
turtle.write(" ( "+str(x1)+" , "+str(y1)+" ) ")

turtle.penup()
turtle.goto(x2+5,y2)
turtle.pendown()
turtle.write("( "+str(x2)+" , "+str(y2)+" )")

turtle.exitonclick()