# def whichCake(ingredient, base, coating):
#   if ingredient == "chocolate":
#     print("Hmm, chocolate!")
#   elif ingredient == "broccoli":
#     print("Eeew, that's the wrong kind of vegan cake!")
#   else:
#     print("I guess that's a goog flavor too.. ")
#
#   print("So you want a", ingredient, "cake on a", base, "base with", coating, "on top?")
# # whichCake("carrot", "biscuit", "icing")
#
# userIngredient = input("Name an ingredient: ")
# userBase = input("Name a type of base: ")
# userCoating = input("Fave cake topping: ")
# whichCake(userIngredient, userBase, userCoating)

# roll a dice of a desired number of sides
import random

print("=== 🎲 Infinity Dice 🎲 ===")
print()


def rolling(sides):
    roll = random.randint(1, sides)
    print(f"> You rolled {roll}.")


sides = int(input("How many sides? > "))
print()
rolling(sides)

while True:
    print()
    re_roll = input("Roll again?(y/n) > ")
    if re_roll == "n":
        break
    rolling(sides)
