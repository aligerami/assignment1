def is_prime(number):
    for i in range(number-1,1,-1):
        if(number%i ==0):
            return False
    return True

for i in range (2,1000):
    if is_prime(i):
        print(i, end=" ,")