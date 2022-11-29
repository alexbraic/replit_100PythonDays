# generate a character
# Name
# char type
# health = (6-sided-roll * 12-sided-roll) / 2 + 10
# str = (6-sided-roll * 8-sided-roll) / 2 + 12
# present in a menu

# import required modules
import random
import os
import time


# color class
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


# define health and strenght random generators
def health():
    h = (random.randint(1, 6) * random.randint(1, 12)) / 2 + 10
    return h


def strength():
    s = (random.randint(1, 6) * random.randint(1, 8)) / 2 + 12
    return s


# Logic - keep building characters until again == "n"
while True:
    # present main menu and clear it after charType input
    print("Character builder")
    charName = input("Name your Legend: ")
    charType = input("Character Type (Human, Elf, Wizard, Orc): ")
    time.sleep(0.5)
    os.system("clear")

    # Make it look like the computer is thinking
    print("Generating stats")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    os.system("clear")

    # print build results and add some colors to it
    print(f"=== {bcolors.HEADER}{charName}{bcolors.ENDC} ===")
    print(f"{bcolors.OKCYAN}Class: {bcolors.ENDC}{charType}")
    print(f"{bcolors.FAIL}HEALTH{bcolors.ENDC}: {health()}")
    print(f"{bcolors.OKGREEN}STRENGHT{bcolors.ENDC}: {strength()}")

    print()
    print(f"May your name go down in legend, {charName}!")
    print()

    # go again? if yes, clear previous result and start again
    again = input("Again?(y/n): ")
    time.sleep(0.5)
    os.system("clear")
    if again == "n":
        break
