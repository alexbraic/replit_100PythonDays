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
    # solution 1
    counted = {}
    for item in inventory:
        if item in counted:
            counted[item] += 1
        else:
            counted[item] = 1
    for key, value in counted.items():
        print(f"{key:^20} {value}")

    # solution 2
    # seen = []
    # for item in inventory:
    #   if item not in seen:
    #     print(f"{item} {inventory.count(item)}")
    #     seen.append(item)

    # solution 3
    # uniqueItems = set(inventory)
    # for item in uniqueItems:
    #   print(f"{item} {inventory.count(item)}")

      
def removeItem():
    rmItem = input("Select item to remove: ")
    if rmItem in inventory:
      inventory.remove(rmItem)
      # inventory.pop(inventory.index(rmItem))
    else:
      print("Item not in inventory")


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
