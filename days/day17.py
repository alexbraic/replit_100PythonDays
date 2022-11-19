# day 14
# while loops
# check for right user input by using while loops

# day 16
# new while loop type
# keep score
# if either player gets a score of 3, break and exit
# also give the players the result of who won
# if score < 3, continue

from getpass import getpass as input
"""rock smashes scissors,
   paper covers rock,
   scissors cut paper"""

# new while version
# game name and ask player for input
print("=== Rock, Paper, Scissors ===")
print("=== Best out of 3 Edition ===")
print("Select your move (r, p or s)!")
print()
p1Score = 0
p2Score = 0

while True:

    # check if player input is part of required letters
    p1 = input("Player1, your move: ")
    while p1 not in ["r", "p", "s"]:
        print("Wrong letter, try again 😉")
        p1 = input("Player1, your move: ")
    p2 = input("Player2, your move: ")
    while p2 not in ["r", "p", "s"]:
        print("Wrong letter, try again 😉")
        p2 = input("Player2, your move: ")
    print()

    # compare and set winner or draw
    if p1 == "r" and p2 == "s":
        print("Player1's rock smashes Player2's scissors!")
        print("Player1 wins!\n")
        p1Score += 1
    elif p1 == "r" and p2 == "p":
        print("Player2's paper covers Player1's rock!")
        print("Player2 wins!\n")
        p2Score += 1

    if p1 == "p" and p2 == "s":
        print("Player2's scissors cuts Player1's paper!")
        print("Player2 wins!\n")
        p2Score += 1
    elif p1 == "p" and p2 == "r":
        print("Player1's paper covers Player2's rock!")
        print("Player1 wins!\n")
        p1Score += 1

    if p1 == "s" and p2 == "p":
        print("Player1's scissors cuts Player2's paper!")
        print("Player1 wins!\n")
        p1Score += 1
    elif p1 == "s" and p2 == "r":
        print("Player2's rock smashes Player1's scissors!")
        print("Player2 wins!\n")
        p2Score += 1
    if p1 == p2:
        print("It's a draw!\n")

    # once a player reaches 3 points, set winner and give score
    if p1Score == 3 or p2Score == 3:
        print()
        print(f"Player 1 score: {p1Score}\nPlayer 2 score: {p2Score}")
        if p1Score > p2Score:
            print("Player 1 wins the trophy! 🏆")
        else:
            print("Player 2 wins the trophy! 🏆")
        break
        exit()
    elif p1Score < 3 or p2Score < 3:
        continue
    print()
