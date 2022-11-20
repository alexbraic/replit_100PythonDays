# guessing game
# display if guessed number is too high/low
# count attempts and display at the end
# if nr == negative, exit()

# added random range for fun
from random import randrange

print('=== Welcome to "Guess That Number" ===')
print()
nr = randrange(1, 101)
guess = 0
count = 1
print("What positive number am I thinking of?")
while guess != nr:
    guess = int(input("> "))

    if guess < 0:
        print("Cheeky! Now you have to start the game again!")
        exit()
    elif guess > nr:
        print("Too high!")
        count += 1
    elif guess < nr:
        print("Too low!")
        count += 1

if count == 1:
    print("OMG! You guessed it on the first try!\nStop reading my mind 👽😂")
else:
    print(f"You've guessed correctly!\nIt took you {count} times to do it! 🎉")
