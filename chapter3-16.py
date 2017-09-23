import turtle

def drawLine(start_x,line_size,repetation):
    turtle.penup()
    turtle.goto(start_x,0)
    turtle.pendown()
    angle=180-((repetation-2)*180)/repetation
    for i in range (0,repetation):
        turtle.forward(line_size)
        turtle.left(angle)

drawLine(-300,50,3)
drawLine(-230,45,4)
drawLine(-160,35,5)
drawLine(-80,30,6)
drawLine(0,25,7)
drawLine(80,23,8)
drawLine(160,19,9)
drawLine(240,17,10)

turtle.exitonclick()
