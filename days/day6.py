import getpass
#userbase = ("Alex", "Sandy")
#uname = input("Username: ")
#if uname in userbase:
#  passwd = getpass.getpass()
#else:
#  print(f"Yea, we don't know you {uname}, go away!")
#if uname == "Alex" and passwd == "passw0rd":
#  print(f"Welcome, {uname}!")
#elif uname == "Sandy" and passwd == "n8Passw0rd":
#  print(f"Welcome, {uname}")

print("MY LOGIN SYSTEM")
print("===============")

userbase = ("Alex", "Sandy", "Joey")
uname = input("Username: ")
if uname in userbase:
  passwd = getpass.getpass()
else:
  print(f"Yea, we don't know you {uname}, go away!")
if uname == "Alex" and passwd == "passw0rd":
  print(f"Welcome, {uname}!")
  print(
    "So happy you're here, the other ones bore me 😂, but i have to be nice, hehe."
  )
elif uname == "Sandy" and passwd == "n8Passw0rd":
  print(f"Welcome, {uname}! I hope you're having a great day so far, my dear!")
  print("Go on, enjoy the rest of it! You're the best!")
elif uname == "Joey" and passwd == "Passw0rds":
  print(f"How YOU doooin'?! \nGreat to see you again {uname}!")
  print()
  print("By the way, there's fresh pizza for you in the kitchen!")
