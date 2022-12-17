# todo list management system
# 1 Add - what the items is, due date, priority
# 2 View - viewl all / view priority / see just a priority type
# 3 Edit - new title / due date / priority / Add a prompt to say it is upd.
# 4 Remove - done / delete
import time
import os

print("== ToDo ==")
time.sleep(1.5)
os.system("clear")

# row = []
todos = []


def todoItem():
    name = input("Task name: ").strip().lower()
    due = input("Due date: ")
    priority = input("Priority: ").strip().lower()

    row = [name, due, priority]
    return row


# print the whole ToDo list
def printIt(list):
    for row in list:
        print(f"Task Name: {row[0].capitalize()}")
        print(f" Due Date: {row[1].capitalize()}")
        print(f" Priority: {row[2].capitalize()}")
        print()
    print()


# priority filter
def priority(this):
    for item in todos:
        if item[2].lower() == this:
            print(f"Task Name: {item[0].capitalize()}")
            print(f" Due Date: {item[1].capitalize()}")
            print(f" Priority: {item[2].capitalize()}")
            print()


# menu function
def menu():
    print("1: Add")
    print("2: View")
    print("3: Edit")
    print("4: Remove")
    print("5: Exit")


# choice value before user chooses it
choice = 0

while True:
    menu()
    print("-------------")
    choice = int(input("Enter option: ").strip())
    os.system("clear")
    # check that input is one of the menu options
    if choice < 1 or choice > 5:
        print()
        print("Try again")
        time.sleep(1.5)
        os.system("clear")
        continue

    # 1 add an item
    if choice == 1:
        todos.append(todoItem())
        # print(todos)
        print()

    # 2 view all items
    if choice == 2:
        printIt(todos)

        filter = input("Filter by priority? (y/n): ").strip().lower()
        if filter == "y":
            os.system("clear")
            x = input("Which priority to view? ")
            print()
            priority(x)
        else:
            os.system("clear")

    # 3 edit items
    if choice == 3:
        sure = input("Sure to edit?(y/n) ").strip().lower()
        if sure == "y":
            printIt(todos)
            x = int(input("Which item to edit?: "))
            x -= 1
            for row in todos:
                todos.pop(x)
                #print(todos)
            print()
            print("Enter new values below.")
            todos.insert(x, todoItem())
        else:
            os.system("clear")
            continue
        print()
    # 4 remove item if in list
    if choice == 4:
        remItem = input("Which task to remove? ")
        for row in todos:
            if row[0] == remItem:
                todos.remove(row)
            else:
                remItem = input("Task does not exist. Try again: ")
                for row in todos:
                    if row[0] == remItem:
                        todos.remove(row)

    # 5 exit
    if choice == 5:
        break
