number1=int(input("Enter first number :"))
number2=int(input("Enter second number :"))

temp=number1

if number1>number2:
    temp=number2
while temp>0:
    if(number1%temp == number2%temp == 0):
        break
    temp=temp-1
    
if temp==0:
    print("There is no greatest common divisor")  
    exit()  

print(temp)
    