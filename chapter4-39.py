import turtle
import math
circle1=str(input("Enter circle1's center x , y coordinates, and radius: ")).split(",")
circle2=input("Enter circle2's center x ,, y coordinates, and radius: ").split(",")

distanc=math.sqrt(math.pow(float(circle1[0])-float(circle2[0]),2)+math.pow(float(circle1[1])-float(circle2[1]),2))


turtle.penup()
turtle.goto(float(circle1[0]),float(circle1[1]))
turtle.pendown()
turtle.circle(float(circle1[2]))

turtle.penup()
turtle.goto(float(circle2[0]),float(circle2[1]))
turtle.pendown()
turtle.circle(float(circle2[2]))

turtle.penup()
turtle.goto(-100,-40)
turtle.pendown()
if(distanc+float(circle2[2])<=float(circle1[2]) ):
    turtle.write("circle2 is inside circle1",font=("Arial", 16, "normal")) 
elif(distanc<float(circle1[2])+float(circle2[2]) ):
    turtle.write("circle2 overlaps circle1",font=("Arial", 16, "normal")) 
else:
    turtle.write("circle2 doesn't overlap circle1",font=("Arial", 16, "normal"))
    
turtle.exitonclick()