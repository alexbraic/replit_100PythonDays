# mokedex
# loop add new beasts

import os

mokedex = {}


def prettyPrint():
    print()
    print("    Name    |   Type   |   HP   |   MP   ")
    for key, value in mokedex.items():
        print(f'{key:^12}', end="|")
        for skey, sval in value.items():
            if skey == "type":
                print(f'{sval:^10}', end="|")
            elif skey == "mp":
                print(f'{sval:^8}')
            else:
                print(f'{sval:^8}', end="|")

    print()


while True:
    if len(mokedex) == 0:
        print("What beasts have you caught? Add them to your mokedex!")
    else:
        x = input("Add another beast to your collection? (y/n)\n")
        if x == "n":
            os.system("clear")
            print("Your collection:")
            prettyPrint()
            break
    print()
    name = input("Name: ").strip().title()
    type = input("Type: ").strip().capitalize()
    hp = input("Starting HP: ")
    mp = input("Starting MP: ")

    mokedex[name] = {"type": type, "hp": hp, "mp": mp}

    prettyPrint()

# clue = {}
#
# def prettyPrint():
#   print()
#   for key, value in clue.items():
#     print(key, end=" > ")
#     for subkey, subvalue in value.items():
#       print(f'{subkey}: {subvalue}', end=" | ")
#     print()
# while True:
#   name = input("Name: ")
#   location = input("Location: ")
#   weapon = input("Weapon: ")
#
#   clue[name] = {"location": location, "weapon": weapon}
#   # print(clue)
#   prettyPrint()
