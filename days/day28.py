# generate 2 characters and have them duel automatically
# improvement from day27.py

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


print("=== Character Duel ===")
# Logic - keep building characters until again == "n"
while True:
    # player 1 name and class
    print("Build your legend, Player 1!")
    print("----------------------------")
    charName1 = input("Name your Legend: ")
    charType1 = input("Character Type (Human, Elf, Wizard, Orc): ")
    time.sleep(0.5)
    os.system("clear")

    hp1 = health()
    str1 = strength()

    # player 2 name and class
    print("Build your legend, Player 2!")
    print("----------------------------")
    charName2 = input("Name your Legend: ")
    charType2 = input("Character Type (Human, Elf, Wizard, Orc): ")
    time.sleep(0.5)
    os.system("clear")

    hp2 = health()
    str2 = strength()

    # print build results and add colors to it
    print(f"=== {bcolors.HEADER}{charName1}{bcolors.ENDC} ===")
    print(f"{bcolors.OKCYAN}Class: {bcolors.ENDC}{charType1}")
    print(f"{bcolors.FAIL}HEALTH{bcolors.ENDC}: {hp1}")
    print(f"{bcolors.OKGREEN}STRENGHT{bcolors.ENDC}: {str1}")
    print()
    print(f"=== {bcolors.HEADER}{charName2}{bcolors.ENDC} ===")
    print(f"{bcolors.OKCYAN}Class: {bcolors.ENDC}{charType2}")
    print(f"{bcolors.FAIL}HEALTH{bcolors.ENDC}: {hp2}")
    print(f"{bcolors.OKGREEN}STRENGHT{bcolors.ENDC}: {str2}")
    time.sleep(8)
    os.system("clear")

    # duel logic
    # subtract health from the char that takes damage
    #+by the amount of the other player's strenght
    counter = 1
    while hp1 >= 0 or hp2 >= 0:
        print("⚔️ BATTLE TIME ⚔️")
        print()
        if counter == 1:
            print("The battle begins!")
        else:
            print("The battle continues!")

        # randomly select player 1/2 to strike first
        hit = random.randint(0, 1)
        if hit == 0:
            print(f"{charName1} wins the first blow")
            print(f"{charName2} takes a hit, with {str1} damage")
            print()
            print(f"{charName1}")
            if hp1 >= 0:
                print(f"{bcolors.FAIL}HEALTH{bcolors.ENDC}: {int(hp1)}")
            else:
                print(f"{bcolors.FAIL}HEALTH{bcolors.ENDC}: 0")
            print()

            hp2 -= str1
            print(f"{charName2}")
            if hp2 >= 0:
                print(f"{bcolors.FAIL}HEALTH{bcolors.ENDC}: {int(hp2)}")
            else:
                print(f"{bcolors.FAIL}HEALTH{bcolors.ENDC}: 0")

        else:
            print(f"{charName2} wins the first blow")
            print(f"{charName1} takes a hit, with {str2} damage")
            print()
            print(f"{bcolors.HEADER}{charName1}{bcolors.ENDC}")

            hp1 -= str2
            if hp1 >= 0:
                print(f"{bcolors.FAIL}HEALTH{bcolors.ENDC}: {int(hp1)}")
            else:
                print(f"{bcolors.FAIL}HEALTH{bcolors.ENDC}: 0")
            print()
            print(f"{bcolors.HEADER}{charName2}{bcolors.ENDC}")
            if hp2 >= 0:
                print(f"{bcolors.FAIL}HEALTH{bcolors.ENDC}: {int(hp2)}")
            else:
                print(f"{bcolors.FAIL}HEALTH{bcolors.ENDC}: 0")

        # the loser is the first char that reaches 0 health
        if hp1 <= 0:
            print()
            print(f"🏆 {bcolors.OKCYAN}{charName2} wins!{bcolors.ENDC} 🏆")
            break
            exit()
        elif hp2 <= 0:
            print()
            print(f"🏆 {bcolors.OKCYAN}{charName1} wins!{bcolors.ENDC} 🏆")
            break
            exit()
        counter += 1
        time.sleep(8)
        os.system("clear")

    # go again? if yes, clear previous result and start again
    print()
    again = input("Again?(y/n): ")
    time.sleep(0.5)
    os.system("clear")
    if again == "n":
        break
