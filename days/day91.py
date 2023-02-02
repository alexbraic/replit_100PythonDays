import requests, json, time, os
from replit import db

# lesson
#result = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
#  joke = result.json()
#  print(json.dumps(joke, indent=2))
#print(result.content)

# challenge
# dad jokes
# show a menu to get a new joke, save it if you like it, load all saved
# save the id to replit db
# load old jokes to screen


# request a new joke from the API
def getJokes():
  result = requests.get("https://icanhazdadjoke.com/",
                        headers={"Accept": "application/json"})
  global joke
  joke = result.json()
  print(joke["joke"])


# save by joke id to replit db
def save():
  item = joke["id"]
  body = joke["joke"]
  db[item] = {"joke": body}
  print("Saved!")
  print()


# load jokes to program
def load():
  keys = db.keys()
  print("-------------------------------------------------------------")
  for key in keys:
    # print saved jokes from local db
    print(f'''"{db[key]["joke"]}"''')
    time.sleep(1)
    print()
    # or load the saved joke id from the API
    # rslt = requests.get(f"https://icanhazdadjoke.com/j/{key}", headers={"Accept": "application/json"})
    # jk = rslt.json()
    # print(jk["joke"])
    # time.sleep(1)
    # print()
  print("-------------------------------------------------------------")
  print()


# run the programm loop
while True:
  menu = input("(n)ew joke, (s)ave joks, (l)oad old jokes\n> ").strip().lower()
  print()
  if menu == "s":
    save()  # save to local replit db
  elif menu == "l":
    load()  # load from db/API
  elif menu == "n":
    getJokes()  # request an new joke
    print()
  else:
    break
