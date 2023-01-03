# private diary

# time + replit db
# type in password to get in
# add/view diary entry
# store as key = timestamp
# view choose latest, then previous entry, then next; option to exit loop

import datetime, time, os
from replit import db

# solution at the bottom

# this one kind of works, but needs adjustments and it is too late today
# comment out until line 86 to see solution
# check keys
# keys = db.keys()
# print(keys)


# if user is not set, set user and password
# if user is set, check password and continue to menu()
def user():
  match = db.prefix("user")
  if len(match) != 0:
    check_user = input("Who are you? > ").strip().lower()
    if check_user == db["user"]:
      pass_check = input("Password please: ")
      if pass_check == db["password"]:
        time.sleep(1)
        os.system("clear")
        greet = print("Hi Alex, Welcome to your diary!")
        return greet
      else:
        exit()
  else:
    usr = input("Name please: ").strip().lower()
    db["user"] = usr
    the_pass = input("Set your password: ").strip()
    db["password"] = the_pass
    time.sleep(1)
    os.system("clear")


# welcome menu once user authenticates and choices
def menu():
  menu = input("1. Add thoughts\n2. View your past\n> ")
  return menu


# add today's thoughts
def addNewDay():
  # get timestamp at input and convert it to a "decimal" string
  timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
  value = input("What's on your mind today?\n> ")
  # create the key using the timestamp and value above
  db[f"key-{timestamp}"] = value


# view past thoughts one by one, or exit
def viewOldDays():
  matches = db.prefix("key-")
  matches = matches[::-1]

  for i in matches:
    print(f'{i}: {db[i]}')
    next_or_not = input("See next? (y/n) > ")
    if next_or_not == "y":
      os.system("clear")
      continue
    else:
      break


while True:
  user()
  menu()
  if menu() == "1":
    addNewDay()
  elif menu() == "2":
    viewOldDays()
  else:
    break


def addEntry():
  time.sleep(1)
  os.system("clear")
  timestamp = datetime.datetime.now()
  print(f'Diary entry for my {timestamp}.')
  print()
  entry = input("> ")

  db[timestamp] = entry


def viewEntry():
  keys = db.keys()

  for key in keys:
    time.sleep(1)
    os.system("clear")
    print(f"""{key}
    {db[key]}""")
    print()
    opt = input("Next or exit? > ")

    if opt.lower()[0] == "e":
      break


passwd = input("Password: ")
if passwd != "Alex1":
  exit()

while True:
  os.system("clear")
  menu = input("1. Add\n2. View\n> ")
  if menu == "1":
    addEntry()
  else:
    viewEntry()
