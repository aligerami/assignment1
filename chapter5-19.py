number=int(input("please enter number between 1 and 15"))
#umber=14

for i in range (0,number):
    for j in range (0,number-i,1):
        print("   ",end="")
    for j in range (i,0,-1):
        print(j," ",end="")
    for k in range(2,2+i-1):
        print(k," ",end="")
    print(" ")