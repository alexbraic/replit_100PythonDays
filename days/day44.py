listr = []


def prettyPrint():
    print()
    for row in listr:
        for item in row:
            print(f"{item:^10}", end=" | ")
        print()
    print()


while True:
    decide = input("Add or Remove? ").strip().lower()
    if decide == "add":
        name = input("What is your name? ")
        age = input("What is your age? ")
        pref = input("What is your computer platform? ")
        row = [name, age, pref]
        listr.append(row)

    else:
        rmv = input("Which name to remove? ")
        for row in listr:
            if name in row:
                listr.remove(row)
    prettyPrint()

    exit = input("Exit? y/n: ").strip().lower()

    if exit == "y":
        print(prettyPrint())
        break
    else:
        continue
