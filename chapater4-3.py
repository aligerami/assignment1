'''
a=int(input("please enter \"a\" for equations ax + by = e :"))
b=int(input("please enter \"b\" for equations ax + by = e :"))
e=int(input("please enter \"e\" for equations ax + by = e :"))
c=int(input("please enter \"c\" for equations cx + dy = f :"))
d=int(input("please enter \"d\" for equations cx + dy = f :"))
f=int(input("please enter \"f\" for equations cx + dy = f :"))
'''
a=1
b=2
e=3
c=4
d=5
f=6

      
if(a*d-b*c ==0):
    print("********* The equation has no solution *********")
    exit()

x=(e*d-b*f)/(a*d-b*c)
y=(a*f-e*c)/(a*d-b*c)
print("values of x is :",x)
print("values of y is :",y)