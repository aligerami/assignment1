while True:
        number = input("Please enter 4 digit number ")
        if len(number)!=4 : 
            print("Sorry, your number is wrong, please try again.")
            continue
        else:
            break
#number="1234"     
    
i=len(number)
temp=""
while i>0 :
    temp=temp+number[i-1]
    i=i-1

print(temp)
