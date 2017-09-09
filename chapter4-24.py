import random
cards=["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
cards_type=["Clubs", "Diamonds", "Hearts", "Spades"]

random_card=random.randint(0,12)
random_card_type=random.randint(0,3)

print("The card you picked is the ",cards[random_card]," of ",cards_type[random_card_type])