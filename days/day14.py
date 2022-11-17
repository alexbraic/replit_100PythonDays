# while loops
# check for right user input by using while loops

from getpass import getpass as input
"""rock smashes scissors,
   paper covers rock,
   scissors cut paper"""

again = ""

# while loop to ask the player if they want to play again
while again.lower() != "n":
    # game name and ask player for input
    print("=== Rock, Paper, Scissors ===")
    print("Select your move (r, p or s)!")

    # check if player input is part of required letters
    p1 = input("Player1, your move: ")
    while p1 not in ["r", "p", "s"]:
        print("Wrong letter, try again 😉")
        p1 = input("Player1, your move: ")

    p2 = input("Player1, your move: ")
    while p2 not in ["r", "p", "s"]:
        print("Wrong letter, try again 😉")
        p2 = input("Player1, your move: ")
    print()

    # compare and set winner or draw
    if p1 == "r" and p2 == "s":
        print("Player1's rock smashes Player2's scissors!")
        print("Player1 wins!")
    elif p1 == "r" and p2 == "p":
        print("Player2's paper covers Player1's rock!")
        print("Player2 wins!\n")

    if p1 == "p" and p2 == "s":
        print("Player2's scissors cuts Player1's paper!")
        print("Player2 wins!\n")
    elif p1 == "p" and p2 == "r":
        print("Player1's paper covers Player2's rock!")
        print("Player1 wins!\n")

    if p1 == "s" and p2 == "p":
        print("Player1's scissors cuts Player2's paper!")
        print("Player2 wins!\n")
    elif p1 == "s" and p2 == "r":
        print("Player2's rock smashes Player1's scissors!")
        print("Player2 wins!\n")

    if p1 == p2:
        print("It's a draw!\n")

    # ask if they want to try again
    again = input("Go again? (y or n): ")
    while again.lower() != "y" and again.lower() != "n":
        print("Wrong letter, try again 😉")
        again = input("Go again? (y or n): ")

    # be nice even if told no :)
    if again == "n":
        print("Thank you for playing 😁")
    print()
