def pinPicker(number):
    import random
    pin = ""
    for i in range(number):
        pin += str(random.randint(0, 9))
    return pin


myPin = pinPicker(4)

print(myPin)

# character stats generator

# name your warrior
# roll a 6-sided dice, roll a 8-sided dice
#+to get the character health
# name the char
# put the stats in different colors

import random

print("=== Character Stats Generator ===")


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def charLife(name):
    life = random.randint(1, 7) * random.randint(1, 9)
    return life


# ask for char name and roll for the HP stat
charName = input("Name your character: ")
charHP = charLife(charName)

print()
print("Rolling...")
print()
print(f"{bcolors.HEADER}{charName}{bcolors.ENDC} has {charHP}HP.")

# declare class after roll
if int(charHP) < 20:
    print(
        f"Your character is best suited to be a {bcolors.FAIL}mage{bcolors. ENDC}!"
    )
elif int(charHP) > 20 and int(charHP) < 30:
    print(
        f"Your character is best suited to be a {bcolors.OKGREEN}rogue{bcolors. ENDC}!"
    )
else:
    print(
        f"Your character will make for a strong {bcolors.WARNING}warrior{bcolors. ENDC}!"
    )
