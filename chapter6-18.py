import random
def print_matrix(n):
    for i in range(1,n):
        for j in range (1,n):
            print(random.randint(0,1),end=" ")
        print("")

print_matrix(10)