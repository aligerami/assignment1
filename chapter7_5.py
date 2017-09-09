import math
class  regular_polygon:
    def __init__(self,n=3,side=1,x=0,y=0):
                 self.__n=n
                 self.__y=y
                 self.__x=x
                 self.__side=side
    def get_n(self):
        return self.__n
    def get_side(self):
        return self.__side
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    def set_n(self,n):
        self.__n=n
    def set_y(self,y):
        self.__y=y
    def set_x(self,x):
        self.__x=x
    def set_side(self,side):
        self.__side=side

    def get_perimeter(self):
        return self.__n*self.__side
    def get_area(self):
        return self.__n*self.__side*self.__side/4*math.tan(math.pi/self.__n)
    
def main():
    p10=regular_polygon(10,4,5.6,7.8)
    p6=regular_polygon(6,4)
    print("p10 perimeter is: ",str(p10.get_perimeter()))
    print("p10 area is: ",str(p10.get_area()))
    print("p6 perimeter is: ",str(p6.get_perimeter()))
    print("p6 area is: ",str(p6.get_area()))
    
main()