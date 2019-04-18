#Dice Rolling Simulator
#dice.py

from random import randint

def rand():
    return randint(0,6)
    
repeat = True
while repeat:
    print("You rolled",rand())
    print("Do you want to roll again?")
    repeat = ("y" or "yes") in input().lower()
print("Game Over")