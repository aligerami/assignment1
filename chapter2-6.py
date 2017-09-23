while True:
        number = int(input("Please enter number between 0 and 1000 : "))
        if number>1000 or number<0:
            print("Sorry, your number is wrong, please try again.")
            continue
        else:
            break

print("sum of digits is : ",number%10 + ((number//10))%10 + ((number//100))%10)
