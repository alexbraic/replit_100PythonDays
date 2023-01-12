from replit import db

#ans = input("Password >")
#salt = db["david"]["salt"]
#newPassword = f"{ans}{salt}"
#newPassword = hash(newPassword)

#if ans == db["david"]["password"]:
# print("Login successful")

# login system
# add users 1. add user 2. login
# ask username for a pasword and store it with salt
# salt = randomly generated 4 digit number
# add salt at the end of the pass
# store passwords as hash values
# can store multiple users

import os, random


def add_user():
  usr = input("Username: ")
  passwd = input("Password: ")

  keys = db.keys()
  if usr in keys:
    print()
    print("User exists. Please choose another.")
    print()
    return

  salt = random.randrange(0000, 9999)
  new_password = f'{passwd}{salt}'
  new_password = hash(new_password)
  db[usr] = {"username": usr, "password": new_password, "salt": salt}
  print("User added.")
  print()


def login():
  os.system("clear")
  user = input("Username: ")
  password = input("Password: ")
  keys = db.keys()
  if user not in keys:
    print("User does not exist. Please create an account.")
    return

  salt = db[user]["salt"]
  new_pass = f'{password}{salt}'
  new_pass = hash(new_pass)
  if db[user]["password"] == new_pass:
    print()
    print("Login successful!")
    print()
  else:
    print("Incorrect credentials")
    print()
    return


while True:
  menu = input("1. Add user\n2. Login\n> ")
  if menu == "1":
    add_user()
  elif menu == "2":
    login()
  else:
    for key in db.keys():
      print(key)
