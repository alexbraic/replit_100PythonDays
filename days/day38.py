# vowels =["a", "e", "i", "o", "u"]

# statement =input("Write something: ")
# for i in statement:
#   if i.lower() in vowels:
#     print('\033[33m', end='')
#   print(i, end='')
#   print('\033[0m', end="")

# Output writing from a user's input
# When detecting the starting letter of a color
#+change the color of the text tot that color.
# When there is a space, turn the color back to default

statement = input("Write something: ")
print()
for i in statement:
    if i.lower() == "r":
        print('\033[91m', end='')
    elif i.lower() == "o":
        print('\033[33m', end='')
    elif i.lower() == "y":
        print('\033[93m', end='')
    elif i.lower() == "g":
        print('\033[92m', end='')
    elif i.lower() == "b":
        print('\033[34m', end='')
    elif i.lower() == "p":
        print('\033[95m', end='')
    elif i.lower() == " ":
        print('\033[0m', end='')
    print(i, end='')
