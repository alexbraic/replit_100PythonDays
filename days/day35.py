tdList = []


# function to print items in list
def printIt():
    print("Your list:")
    i = 0
    for item in tdList:
        print(f"{i + 1}. {item}")
        i += 1
    print()


# check if item is in list
def check(item, list):
    for i in list:
        if item != i:
            res = "Item not in list"
        else:
            res = input(f"Are you sure you want to remove {item}?(y/n) > ")
        return res


# title
print("=== ToDo ===")

while True:
    printIt()
    if len(tdList) == 0:
        print("Your list is currently empty.")
        item = input("Add item or Exit? ")
    else:
        item = input("Add, Remove, Edit or Exit?\n")

    # add item
    if item == "add":
        addItem = input("New item: ")
        tdList.append(addItem)
        print()

    # remove item
    elif item == "remove":
        print("Remove which item?")
        printIt()
        remItem = input("> ")
        res = check(remItem, tdList)
        if res == "y":
            for i in tdList:
                if i != remItem:
                    print("Item not in list.")
                else:
                    tdList.remove(remItem)
            print()

    # edit item
    elif item == "edit":
        print()
        printIt()
        x = int(input("Enter the number of the item to edit?\n> "))
