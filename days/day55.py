import os, random

tdList = []

#
fileExist = True
# load file logic
try:
    f = open("ToDoList.txt", "r")
    tdList = eval(f.read())
    f.close()
except:
    fileExist = False


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
        if list[int(item) - 1] not in list:
            res = "Item not in list"
        else:
            list.remove(list[int(item) - 1])
            res = "Item removed"
        return res


# title
print("=== ToDo ===")

while True:
    printIt()
    if len(tdList) == 0:
        print("Your list is currently empty.")
        item = input("Add item or Exit? ").strip().lower()
        if item == "exit":
            break
    else:
        item = input("Add, Remove, Edit or Exit?\n").strip().lower()
        if item == "exit":
            break
    # add item
    if item == "add":
        addItem = input("New item: ")
        tdList.append(addItem)
        print()
    # remove item
    elif item == "remove":
        os.system("clear")
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
        os.system("clear")
        print()
        printIt()
        try:
            x = input("Enter the number of the item to edit?\n> ")
        except IndexError:
            pass
            print("Not it")
        tdList.pop(int(x) - 1)
        tdList.insert(int(x) - 1, input("New value: "))

    # if there is a saved file, create a backup directory
    #+and create a backup file
    if fileExist:
        path = os.getcwd()
        if path + "/backups":
            pass
        else:
            os.mkdir("backups")
        name = f"bak{random.randint(1, 1000000)}.txt"
        os.popen(f"cp ToDoList.txt backups/{name}")
    # write to the file and close it
    f = open("ToDoList.txt", "w")
    f.write(str(tdList))
    f.close()
