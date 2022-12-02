# f strings
#name = "Alex"
#age = 28
#pronouns = "him/his"

#print()
#print("This is {}, using {} and is {} years old.".format(name, pronouns, age))
#print()
#print(f"This is {name}, using {pronouns} and is {age} years old.")
#print()
#response = "This is {name}, using {pronouns} and is {age} years old. Hello {name}, how are you? Have you been having a great {age} years old so far?".format(name=name,pronouns=pronouns, age=age)
#print(response)
#print()
#for i in range(1, 31):
#  print(f"Day {i: ^3} of 100")

# challenge
#print()
for i in range(1, 6):
    print(f"Day {i}:")
    userInput = input("\033[32m")
    print("\033[0m")
    userReview = f"You thought Day {i} was"
    print(f"{userReview:^50s}")
    print(f"\033[33m{userInput:^50s}\033[0m")
    print()
