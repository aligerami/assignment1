import random
random_number=random.randint(100,999)
random_number_hundred=int(str(random_number)[0])
random_number_one=int(str(random_number)[2])
random_number_ten=int(str(random_number)[1])

user_number=(input("please input 3 digit number :"))

user_number_one=int(str(user_number)[2])
user_number_ten=int(str(user_number)[1])
user_numberhundred=int(str(user_number)[0])

if(user_number==random_number):
    print("The award is $10,000.")
elif(str(random_number).find(str(user_number_one))!=-1 and str(random_number).find(str(user_number_ten))
   !=-1 and str(random_number).find(str(user_numberhundred))!=1):
    print("The award is $3000.")
elif(str(random_number).find(str(user_number_one))!=-1 or str(random_number).find(str(user_number_ten))
   !=-1 or str(random_number).find(str(user_numberhundred))!=-1):
        print("The award is $1000.")
else:
    print("You award is nothing, are a pathetic loser.")





