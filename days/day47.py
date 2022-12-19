# store 2 items in 2d dicts
# name = Key
# store stats as the sub-dict
# draw a random card and choose a stat
# compare  with the next drawn card and print winner
import random
import time

title = "=== Top Trums - Friends Edition ==="
print(f"{title:^44}")

chars = {
    "Chandler": {
        "height": 182,
        "sarcasm": 99,
        "confidence": 35,
        "cleverness": 80
    },
    "Monica": {
        "height": 175,
        "sarcasm": 60,
        "confidence": 70,
        "cleverness": 75
    },
    "Joey": {
        "height": 176,
        "sarcasm": 40,
        "confidence": 90,
        "cleverness": 41
    },
    "Ross": {
        "height": 186,
        "sarcasm": 72,
        "confidence": 65,
        "cleverness": 89
    },
    "Phoebe": {
        "height": 176,
        "sarcasm": 63,
        "confidence": 83,
        "cleverness": 55
    },
    "Rachel": {
        "height": 172,
        "sarcasm": 59,
        "confidence": 80,
        "cleverness": 66
    }
}

c = "Characters"


def characters():
    print()
    print(f"{c:^44}")
    print("-" * 44)
    for key in chars.keys():
        if key == "Rachel":
            print(key)
        else:
            print(key, end=", ")
    print()


characters()
time.sleep(3)

while True:
    # draw a randwom card for the player and one to play against
    draw1 = random.randint(0, len(chars))
    # get thecard for the user
    drawn1 = list(chars.keys())[draw1 - 1]
    #print it
    print(f"You draw one card.\nYou drew: {drawn1}")

    # create a second char dict that does not hold the first picked char
    # the computer picks from this dict
    chars2 = chars
    del chars2[drawn1]
    # draw a card from the second set
    draw2 = random.randint(0, len(chars2))
    drawn2 = list(chars2.keys())[draw2 - 1]
    print(f"The computer picked: {drawn2}")
    time.sleep(3)
    print()

    # give user the options and have the user choose one
    print(
        "Choose between:\n1. height\n2. sarcasm\n3. confidence\n4. cleverness")
    stat = int(input("Choose which stat your character is best at:\n"))

    val1 = 0
    val2 = 0

    if stat == 1:
        for key in chars.items():
            if key == drawn1:
                for skey, sval in key.items():
                    if skey == "height":
                        val1 = sval
                        print(val1)
        for key in chars2.items():
            if key == drawn2:
                for skey, sval in key.items():
                    if skey == "height":
                        val2 = sval
                        print(val2)
        if val1 > val2:
            print("You won!")
        else:
            print("The computer wins")

    # will continue, i am too tired now
    break
