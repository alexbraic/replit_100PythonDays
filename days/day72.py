import os, time, datetime, random
from replit import db


def intro():
  user = input("Usename: ")
  password = input("Password: ")
  salt = random.randrange(0000, 9999)

  set_pass = f'{password}{salt}'
  set_pass = hash(set_pass)
  db[user] = {"username": user, "password": set_pass, "salt": salt}


def check_user():
  keys = db.keys()
  if keys != 0:
    user_check = input("Username: ").strip()
    if user_check != db[user_check]["username"]:
      print("Not your diary")
      exit()

    pass_check = input("Password: ").strip()


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


while True:
  keys = db.keys()
  if keys != 0:
    intro()
  os.system("clear")
  menu = input("1. Add\n2. View\n> ")
  if menu == "1":
    addEntry()
  else:
    viewEntry()
