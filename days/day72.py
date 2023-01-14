import os, time, datetime, random
from replit import db


def login():
  keys = db.keys()
  if len(keys) == 0:
    time.sleep(1)
    os.system("clear")
    print("=== Set User ===")
    user = input("Usename: ")
    password = input("Password: ")
    salt = random.randrange(1000, 9999)

    set_pass = hash(f'{password}{salt}')
    db[user] = {"username": user, "password": set_pass, "salt": salt}

  else:
    time.sleep(1)
    os.system("clear")
    print("=== Login ===")
    username = input("Username: ").strip()

    if username not in keys:
      print("Sorry, Not your diary.")
      exit()

    salt = db[username]["salt"]

    count = 0
    while count < 3:
      password = input("Password: ").strip()
      pass_check = hash(f'{password}{salt}')

      if db[username]["password"] == pass_check:
        print()
        print(f"Welcome, {username}!")

        time.sleep(2)
        os.system("clear")
        break
      else:
        count += 1
        if count == 3:
          print("Too many failed attempts, check your credentials.")
          exit()
        print("Wrong password! Try again.")
        print()


def addEntry():
  time.sleep(1)
  os.system("clear")
  timestamp = datetime.datetime.now()
  print(f'Diary entry for my {timestamp}.')
  print()
  entry = input("> ")
  db[timestamp] = entry


def viewEntry():
  keys = db.prefix("2")
  for key in keys:
    time.sleep(1)
    os.system("clear")
    print(f"""{key}
    {db[key]}""")
    print()
    opt = input("Next or exit? > ")

    if opt.lower()[0] == "e":
      time.sleep(1)
      os.system("clear")
      break
  time.sleep(1)
  os.system("clear")


login()

while True:
  keys = db.keys()
  #for key in keys:
  #  print(db[key])
  menu = input("1. Add\n2. View\n> ")
  if menu == "1":
    addEntry()
  else:
    viewEntry()

# print a part of a key
#keys = db.keys()
#  for key in keys:
#    if key == "joe":
#      print(db[key]['salt'])
