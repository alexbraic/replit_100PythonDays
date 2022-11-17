from getpass import getpass as input

print("Select your move (R, P or S)!")
p1 = input("Player1, your move: ")
p2 = input("Player2, you're up: ")
print()
"""rock smashes scissors,
paper covers rock,
scissors cut paper"""
again = "y"
while again.lower(): 
  if p1 == "rock" and p2 == "scissors":
    print("Player1's rock smashes Player2's scissors!")
    print("Player1 wins!")
  elif p1 == "rock" and p2 == "paper":
    print("Player2's paper covers Player1's rock!")
    print("Player2 wins!")
  
  if p1 == "paper" and p2 == "scissors":
    print("Player2's scissors cuts Player1's paper!")
    print("Player2 wins!")
  elif p1 == "paper" and p2 == "rock":
    print("Player1's paper covers Player2's rock!")
    print("Player1 wins!")
  
  if p1 == "scissors" and p2 == "paper":
    print("Player1's scissors cuts Player2's paper!")
    print("Player2 wins!")
  elif p1 == "scissors" and p2 == "rock":
    print("Player2's rock smashes Player1's scissors!")
    print("Player2 wins!")
  
  if p1 == p2:
    print("It's a draw!")

  again = input("Go again? (y or n)")