print("=== Math Game ===")

counter = 0
# name your multiples
multi = int(input("Name your multipliers: "))

for i in range(1, 11):
    value = int(input(f"{i} x {multi} = "))
    if value == i * multi:
        counter += 1
        print("Great work!")

    else:
        print("Nope! The right answer was ", i * multi, ".")

if counter == 10:
    print("Woop, woop! You got all of them right! 😎👾🤖")
else:
    print(f"You scored {counter} out of 10!")
