import turtle

turtle.penup()
turtle.goto(0,-100)
turtle.pendown()
turtle.circle(100)

turtle.pensize(2)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.forward(80)

turtle.pensize(3)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.backward(60)

turtle.pensize(1)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.left(90)
turtle.forward(90)

turtle.penup()
turtle.goto(-10,-110)
turtle.pendown()
turtle.write("9:15:00")

turtle.penup()
turtle.goto(0,90)
turtle.pendown()
turtle.write("12")

turtle.penup()
turtle.goto(90,0)
turtle.pendown()
turtle.write("3")

turtle.penup()
turtle.goto(-90,-0)
turtle.pendown()
turtle.write("9")

turtle.penup()
turtle.goto(0,-90)
turtle.pendown()
turtle.write("6")



turtle.exitonclick()
