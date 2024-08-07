import random
computer=random.randint(1,101)
player=int(input("Guess a Number 1-100 : "))
attempt=1
while True:
    if(player>computer):
        player=int(input((f'{player} is greater \n Guess another number : ')))
        attempt+=1
    elif(player<computer):
        player=int(input((f'{player} is lesser \n Guess another number : ')))
        attempt+=1
    else:
        print(f'Your Guess is right \nYou attempted {attempt} times')
        break
        
