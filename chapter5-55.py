import turtle

flag=False
turtle.penup()
turtle.goto(-160,-160)
turtle.pendown()
counter=0

for j in range(-160,160,40):
   
    for i in range (-160,160,40):
        turtle.penup()
        turtle.goto(i,j)
        turtle.pendown()
        print("j is :",j," i =",i," flag=",flag)
        if(flag):
            turtle.begin_fill()
        
        for k in range(4):  
            turtle.forward(40) 
            turtle.left(90)
        if(flag):
            flag=False
            turtle.end_fill()
        else:
            flag=True
    if(flag):
        flag=False
    else:
        flag=True

turtle.exitonclick()


   
        
 