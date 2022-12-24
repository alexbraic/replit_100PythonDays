# pizza shop
# type in pizza quantity and size
# multiply and work out cost
# use save/load
# use try/except
# hold data in a 2d list

import os, time

orders = []
# oad orders file, or print exception if no file
try:
    f = open("orders.txt", "r")
    orders = eval(f.read())
    f.close()
except:
    print("No order list. Will start a new one after the first order.")


# menu - connects to addOrder and showOrders
def menu():
    choice = input("1. Add order\n2. View orders\n> ")

    # add orders
    if choice == "1":
        addOrder()
    # view current orders
    else:
        showOrders()
        time.sleep(3)
        os.system("clear")


# place an order logic: add name, quantity and size
def addOrder():
    name = input("Name: ")
    while True:
        try:
            qty = int(input("How many pizzas would you like to order: "))
            break
        except:
            print("Error: Quantity must be a whole number.")

    size = input("Size (s/m/l): ").lower()
    row = [name, qty, size, cost(qty, size)]
    orders.append(row)


# calculate the cost for the pizzas
def cost(nr, size):
    if size == "s":
        result = float(nr) * 5.99
    elif size == "m":
        result = float(nr) * 7.99
    else:
        result = float(nr) * 9.99
    return round(result, 2)


# display the current orders in a nice table-like structure
def showOrders():
    print()
    a = "Orders"
    b = "Name"
    c = "Quantity"
    d = "Size"
    e = "Total"
    print(f"{a:^63}\n{b:^15}|{c:^15}|{d:^15}|{e:^15}")
    print("-" * 63)
    for row in orders:
        for item in row:
            if item != row[-1]:
                print(f"{item:^15}", end="|")
            else:
                print(f"{item:^15}")
    print()


# running the program and save to file for each new order
while True:
    menu()

    f = open("orders.txt", "w")
    f.write(str(orders))
    f.close()
