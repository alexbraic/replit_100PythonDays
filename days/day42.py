# build a dict that takes a beast
# name, type, special move, hp, mp
# at print, if fire type print red, water print blue, air white
from colorama import Fore

beast = {"name": None, "type": None, "specMove": None, "hp": None, "mp": None}


def colors(self):
    self.green = "\033[32m"


print("Add the following details for the beast:")
print()
beast["name"] = input("Name: ").title()
beast["type"] = input("Type: ").capitalize()
beast["specMove"] = input("Special Move: ").capitalize()
beast["hp"] = input("Starting HP: ")
beast["mp"] = input("Starting MP: ")
print()

for key, value in beast.items():
    if beast["type"].lower() == "nature":
        print(f"{key:<9}| {Fore.GREEN}{value}\033[0m")
    elif beast["type"].lower() == "fire":
        print(f"{key:<9}| {Fore.RED}{value}\033[0m")
    elif beast["type"].lower() == "air":
        print(f"{key:<9}| {value}")
    elif beast["type"].lower() == "dark":
        print(f"{key:<9}| {Fore.MAGENTA}{value}\033[0m")
    elif beast["type"].lower() == "light":
        print(f"{key:<9}| {Fore.YELLOW}{value}\033[0m")
