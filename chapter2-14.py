import math
string_input = input("please enter triangle's three points like this 11,12,21,22,31,32")
#string_input ="1.5,-3.4,4.6,5,9.5,-3.4"
points=string_input.split(",")
temp=len(points)-1
while temp>=0 :
        points[temp]=float(points[temp])
        temp=temp-1
    
s1=float( "{0:.2f}".format(math.sqrt(math.pow(points[0]-points[2],2)+math.pow(points[1]-points[3],2))))
s2=float( "{0:.2f}".format(math.sqrt(math.pow(points[4]-points[2],2)+math.pow(points[5]-points[3],2))))
s3= float("{0:.2f}".format(math.sqrt(math.pow(points[0]-points[4],2)+math.pow(points[1]-points[5],2))))

s = (s1+s2+s3)/2

area=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
print("{0:.2f}".format(area))
