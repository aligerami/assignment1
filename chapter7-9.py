from chapter7_7 import linear_equation
def calculate_a_b(x1,y1,x2,y2):
    slope = (y2-y1)/(x2-x1)
    b=(y2-slope*x2)
    return slope,b

def main():
    
    x1,y1,x2,y2=eval(input("Enter the endpoints of the first line segment:"))
    x3,y3,x4,y4=eval(input("Enter the endpoints of the first line segment:"))
    slope1,b1=calculate_a_b(x1, y1, x2, y2)
    slope2,b2=calculate_a_b(x3, y3, x4, y4)
    
    le=linear_equation(-slope1,1,b1,-slope2,1,b2)
    print(le.get_x())
    print(le.get_y())

main()