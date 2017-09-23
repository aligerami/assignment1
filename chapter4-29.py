import math
circle1=str(input("Enter circle1's center x , y coordinates, and radius: ")).split(",")
circle2=input("Enter circle2's center x , y coordinates, and radius: ").split(",")

distanc=math.sqrt(math.pow(float(circle1[0])-float(circle2[0]),2)+math.pow(float(circle1[1])-float(circle2[1]),2))

if(distanc<=math.fabs(float(circle1[2])-float(circle2[2]) )):
    print("circle2 is inside circle1") 
elif(distanc< float(circle1[2])+float(circle2[2]) ):
    print("circle2 overlaps circle1") 
else:
    print("circle2 doesn't overlap circle1") 
