# this game will be annoying, sorry

name = input("Name, please: ")
name = name.capitalize()
dow = input("What day is it again? ")
dow = dow.capitalize()

if dow in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
           "Sunday"):
  if dow == "Saturday" or dow == "Sunday":
    print("Why you bothering me on the weekend? See you Monday!")
    quit()
  print(
    "Ok, tell me some of your interests. We'll see if you can retain my interest."
  )
  # interest 1
  intrst1 = input("\nYour favourite fruit: ")
  print()
  if intrst1 == "apple":
    print("Ugh, I'm already bored, bye!")
    quit()
  elif intrst1 == "mango":
    print("Man..go away! Why yes, that WAS a trap! 😈")
    quit()
  elif intrst1 == "banana":
    print("That's a good pick, well done!")
    print()
# interest 2
  intrst2 = input("Your favourite color: ")
  print()
  if intrst2 == "orange":
    print("That's a fruit! Bye!")
    print("Oh no, wait wait wait! That's actually my favourite color! 😎")
    print()
# interest 3
  intrst3 = input("Your favourite superhero: ")
  intrst3 = intrst3.capitalize()
  if intrst3 == "Hawkeye":
    print("The Avengers Robin Hood fella?! Bye!")
    quit()
  elif intrst3 == "Thor":
    print("Charming fella'")
    print()
# empty interest check
  if intrst1 == "" or intrst2 == "" or intrst3 == "":
    print(f"Really {name}, you don't have 3 things that interest you?!")
    print("So, it's true what they say abut you then..")
    quit()

elif dow in ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"):
  print("You like shortcuts, here's another one! The end 😈")
  quit()
else:
  print("Come back when you can spell 🙄")
  quit()

if intrst1 == "banana" and intrst2 == "orange" and intrst3 == "Thor":
  print("All great choices! I'll keep you as a friend, great job!")
else:
  print(
    f"So {name}, your favourite fruit is {intrst1}, your favourite color is {intrst2}, and your favourite superhero is {intrst3}."
  )
  print(
    "Not bad! I mean it's not that interesting, but at least you got through it!"
  )
  print("I wonder how many times you tried it, hehe")
