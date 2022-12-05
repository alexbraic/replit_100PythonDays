#myAgenda = []

#def printList():
#  print()
#  for item in myAgenda:
#    print(item)
#  print()

#while True:
#  menu = input("Add or Remove?: ")
#  if menu == "add":
#    item = input("What's next on the Agenda?: ")
#    myAgenda.append(item)
#  elif menu == "remove":
#    item = input("What doyou want to remove?: ")
#    myAgenda.remove(item)
#  else:
#    print(f"{item} was not in the list.")
#  printList()

# toDo list manager
# view
# add
# edit (which)
tdList = []
count = 0
print("=== ToDo ===")
print()
while True:

    for item in tdList:
        print(f"{tdList[item]} {item}")
    print()

    if count == 0:
        item = input("Add item or Exit?: ")
    else:
        item = input("Add, Remove, Edit or Exit?:\n")

    if item == "add":
        addItem = input("New item: ")
        tdList.append(addItem)
        count += 1
        print()
    elif item == "remove":
        remItem = input("Remove which item?: ")
        for it in tdList:
            if it == remItem:
                tdList.remove(remItem)
                count -= 1
            else:
                print("Item not in list.")
        print()
    elif item == "edit":
        it = int(input("Which item to edit?: "))
        tdList.pop(it - 1)
        tdList.insert(it, it)
        print()
    elif item == "exit":
        print("See you next time!")
        exit()
