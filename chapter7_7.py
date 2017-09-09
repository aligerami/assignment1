class linear_equation:
    def __init__(self,a,b,e,c,d,f):
        self.__a=a
        self.__b=b
        self.__c=c
        self.__d=d
        self.__e=e
        self.__f=f
    def get_a(self):
        return self.__a
    def get_b(self):
        return self.__b
    def get_c(self):
        return self.__c
    def get_d(self):
        return self.__d
    def get_e(self):
        return self.__e
    def get_f(self):
        return self.__f
    
    def is_solvable(self):
        return (self.__a*self.__d) != (self.__b*self.__c)
    def get_x(self):
        if self.is_solvable():
            return (self.__e*self.__d-self.__b*self.__f)/(self.__a*self.__d - self.__b*self.__c)
        return "The equation has no solution."
    def get_y(self):
        if self.is_solvable():
            return (self.__a*self.__f-self.__e*self.__c)/(self.__a*self.__d - self.__b*self.__c)
        return "The equation has no solution."

def main():
    a =linear_equation(2,1,4,2,1,4)
    print("x is : ",a.get_x())
    print("y is:",a.get_y())

#main()
