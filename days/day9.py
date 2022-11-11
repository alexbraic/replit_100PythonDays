yob = int(input("What's your birth year?: "))

if yob > 1925 and yob <= 1946:
  print("ok, you're a Traditionalist.")
elif yob > 1946 and yob <= 1964:
  print(
    "You're a Baby Boomer. Did your generation plant explosives under babies?")
elif yob > 1965 and yob <= 1981:
  print("You're part of Generation X. Irradiated much?!")
elif yob > 1982 and yob <= 1995:
  print("So, you're a Millenial. You're all right.")
elif yob > 1996 and yob <= 2015:
  print("You're a Generation Z. Zooper annoying!")
else:
  print("Jeez you're old!")
