import random
print("**************************************************************")
print("************* This is scissor , rock ,paper game *************")
print("**************************************************************")

number_of_computers_win = 0
number_of_user_win = 0
game_options = ["scissor", "rock", "paper"]

while(number_of_user_win < 2 and number_of_computers_win < 2):
    computer_input = random.randint(0, 2)
    user_input = int(input("please enter,1 for scissor,2 for rock ,3 for paper \n your number:"))
    print("computer input is",computer_input)
    print("")
    user_input=user_input-1
    if (computer_input == user_input):
        print("Tie!", " computer by", game_options[computer_input], " you by", game_options[user_input])
    elif(computer_input == 0):
        if(user_input == 1):
            number_of_user_win = number_of_user_win + 1
            print("you win by ", game_options[user_input], "computer lose! by", game_options[computer_input])
        if(user_input == 2):
            number_of_computers_win = number_of_computers_win + 1
            print("computer win by ", game_options[computer_input], "you lose! by", game_options[user_input])
    elif(computer_input == 1):
            if(user_input == 0):
                number_of_computers_win = number_of_computers_win + 1
                print("computer win by ", game_options[computer_input], "you lose! by", game_options[user_input])
            if(user_input == 2):
                number_of_user_win = number_of_user_win + 1
                print("you win by ", game_options[user_input], "computer lose! by", game_options[computer_input])
    elif(computer_input == 2):
            if(user_input == 1):
                number_of_computers_win = number_of_computers_win + 1
                print("computer win by ", game_options[computer_input], "you lose! by", game_options[user_input])
            if(user_input == 0):
                number_of_user_win = number_of_user_win + 1
                print("you win by ", game_options[user_input], "computer lose! by", game_options[computer_input] )
    print("")
if(number_of_user_win==2):
    print("\n******** YOU WIN ********")
else:
    print("\n******** YOU LOSE ********",)



                
                
                


                
            
            

        
    
