# Snake Water Gun Game.
"""
------ Rules -------
computer & you -> Players
(computer ='s') & (you ='g') => You Win
(computer ='w') & (you ='s') => You Win
(computer ='g') & (you ='w') => You Win
    All Other Cases You Lose
"""
import random
def result(comp, you):
    if (comp == you):
        return None
    elif(comp=='s' and you=='g'):
        return True
    elif(comp=='w' and you=='s'):
        return True
    elif(comp=='g' and you=='w'):
        return True
    else:
        return False
choice=('s','w','g')
comp=random.randint(0,2)
comp=choice[comp]
you=input("Choice Either ('s','w','g') :")
result=result(comp,you)
if(result is None):
    print("Match is drown")
elif result:
    print("You Won!")
else:
    print("You Lose")
print(f'Your Choice - {you} \nComputer Choice - {comp}')
