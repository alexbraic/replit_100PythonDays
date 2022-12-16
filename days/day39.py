touchimport random

list = ["first", "second", "third", "apple"]


def rules():
    print("Rules:")
    print("You have 6 lives to start with.")
    print("You can only choose 1 letter at a time.")


print("=== The Hangman Game ===")
print()
rules()
print()

word = random.choice(list)
letterPicked = []
life = 6

hint = []
#print(word)
for letter in word:
    print("_ ", end='')
    hint.append("_ ")
print()
#print(f"result {hint}")

while True:
    print()
    letter = input("Please choose a letter: ").lower()
    if letter in letterPicked:
        print("You've chosen that before")
        continue

    letterPicked.append(letter)

    if letter in word:
        print("\033[32mYou found a letter!\033[0m")
    else:
        print("Not in there!")
        life -= 1

    allLetters = True
    print()
    for i in word:
        if i in letterPicked:
            print(f"{i} ", end="")
        else:
            print("_ ", end="")
            allLetters = False
    print()

    if allLetters:
        print("You won!")
        break

    if life <= 0:
        print(f"You lose! The answer was {word}")
        break
    elif life > 1:
        print(f"{life} lives left!")
    else:
        print(f"{life} life left!")

# first try

#word = random.choice(list)
#result = []
# print(word)
#for letter in word:
#  print("_", end =' ')
#  result.append("_")
#print()
# print(f"result {result}")

#sWord = []
#for letter in word:
#    sWord.append(letter)
#print()

# print(sWord)

#while life != 0 and "_" in result:
#  print()
#  choice = input("Choose a letter: ")

#if choice in sWord:
#  for i in sWord:
#    if i == choice:
#      # print(sWord.index(choice))
#      result[sWord.index(choice)] = choice
#      print(result)
#      if "_" not in result:
#        print("You won! Well done! 😁")
#  print()

# print(f"You have {life} lives left!")
#  elif choice not in sWord:
#    print("Not it! 😋")
#    life -= 1
#    print(f"You have {life} lives left!")
#    print()
#    print(result)

#if life == 0:
#    print("Sorry, you lose! Better luck next time! 😉")
