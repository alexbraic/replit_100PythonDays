import os, time

# this will hold the emails
listOfEmail = []


# create the logic to show the current emails once inserted
def prettyprint():
    os.system("clear")
    print("listOfEmail")
    print()
    for index in range(len(listOfEmail)):
        print(f"{index}: {listOfEmail[index]}")
    time.sleep(1)


# create the email content function
def emailContent():
    for i in range(len(listOfEmail)):
        item = listOfEmail[i]
        # print(item)
        getAt = item.rfind("@")
        sliceIt = slice(0, int(getAt))
        print(f"Dear {item[sliceIt]},")
        print()
        print(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Et ligula ullamcorper malesuada proin libero nunc consequat interdum varius. Quis blandit turpis cursus in hac habitasse platea dictumst. Elit duis tristique sollicitudin nibh sit amet. Diam in arcu cursus euismod quis viverra nibh cras. Orci dapibus ultrices in iaculis nunc."
        )
        print()
        print("In est ante in nibh,")
        print("Me")
        time.sleep(3)
        os.system("clear")


# menu logic
while True:
    print("=== SPAMMER Inc. ===")
    menu = input(
        "1. Add email\n2. Remove email\n3. Show email\n4. Get SPAMMING\n> ")

    # options
    if menu == "1":
        email = input("Email > ")
        listOfEmail.append(email)
    elif menu == "2":
        email = input("Email > ")
        if email in listOfEmail:
            listOfEmail.remove(email)
    elif menu == "3":
        prettyprint()
    elif menu == "4":
        os.system("clear")
        emailContent()
    
    time.sleep(1)
    os.system("clear")
