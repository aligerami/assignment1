def is_prime(number):
    for i in range(number-1,1,-1):
        if(number%i ==0):
            return False
    return True

def reverse(number):
    reversed_number = 0
    while number > 0:
        reversed_number *= 10
        reversed_number += number % 10
        number=number // 10
    return reversed_number

def is_palindrome(number):
    if number== reverse(number):
        return True;
    else:
        return False;

counter=0
for i in range (2,1000):
    if is_prime(i):
        if is_palindrome(i):
            counter=counter+1
            print("{:4}".format(i),end="  ")
            if counter%10==0:
                print(" ")
            