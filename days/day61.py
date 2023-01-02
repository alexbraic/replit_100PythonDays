from replit import db

# db["test"] = "hello there"

#keys = db["test"]
#print(keys)

# objective
# menu add/view tweets
# if view: get timestamp of tweet
# key of tweets => timestamp = datetime.datetime.now()
# view tweets, show in reverse chronological order (most recent first)
# only show 10 at a time
# ask user if they want to see the next 10, if not, go back to main menu
import os, datetime

def addTweet():
  timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
  value = input("Insert thoughts: ")
  db[timestamp] = value
  print()
  
def viewTweets():
  os.system("clear")
  matches = db.prefix("2023")
  matches = matches[::-1]
  counter = 0
  for i in matches:
    print(db[i])
    counter += 1
    if counter % 10 == 0:
      nextPage = input("View next page? (y/n): ")
      os.system("clear")
      if nextPage.lower() == "n":
        break
  print()
  
while True:
  print("Welcome to Tweeetr")
  menu = input("1. Add tweet\n2. View tweets\n> ")

  if menu == "1":
    os.system("clear")
    addTweet()
  elif menu == "2":
    viewTweets()
  else:
    break
