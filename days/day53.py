# inventory
# add, view, remove
import os, time

inventory = []
try:
    f = open("inventory.txt", "r")
    inventory = eval(f.read())
    f.close()
except:
    pass


def addItem():
    item = input("Item type: ")
    inventory.append(item)


def viewItems():
    counted = {}
    for item in inventory:
        if item in counted:
            counted[item] += 1
        else:
            counted[item] = 1
    for key, value in counted.items():
        print(f"{key:^20} {value}")


def removeItem():
    rmItem = input("Select item to remove: ")
    if rmItem in inventory:
        inventory.pop(inventory.index(rmItem))


while True:
    print("=== INVENTORY ===")
    menu = input("1. Add item\n2. View items\n3. Remove item\n4. Exit\n> ")
    if menu == "1":
        os.system("clear")
        addItem()
        while True:
            ask = input("Add another item?(y/n):\n")
            if ask == "y":
                os.system("clear")
                addItem()
            else:
                os.system("clear")
                break
    elif menu == "2":
        os.system("clear")
        viewItems()
        print()
    elif menu == "3":
        viewItems()
        removeItem()
        os.system("clear")
        viewItems()
    else:
        break

    f = open("inventory.txt", "w")
    f.write(str(inventory))
    f.close()
