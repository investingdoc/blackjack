#new blackjack file

import random


#user1choice = input ("How Much Would You Like To Bet?")

deckOfCards = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']

newChoice = random.choice(deckOfCards)

print (newChoice)

userCards = []





for i in range (2):
    userCards.append(random.choice(deckOfCards))


print (f'Your cards are {userCards[0]} and {userCards[1]}')






