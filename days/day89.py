# Chat app

from flask import Flask, request, redirect
import datetime
from replit import db

app = Flask(__name__)

@app.route('/')
def index():
  page = ""
  f = open("chat.html", "r")
  page = f.read()
  f.close()
  page = page.replace("{username}", request.headers["X-Replit-User-Name"])
  page = page.replace("{content}", getContent(request.headers["X-Replit-User-Name"]))
  return page


@app.route('/add', methods=["POST"])
def add():
  form = request.form
  message = form["message"]
  date = datetime.datetime.now()
  timestamp = datetime.datetime.timestamp(date)
  username = request.headers["X-Replit-User-Name"]
  db[timestamp] = {"username": username, "message": message}
  return redirect('/')


def getContent(user):
  message = ""
  f = open("entry.html", "r")
  message = f.read()
  f.close()
  keys = db.keys()
  keys = list(keys)
  result = ""
  recent = 0
  for key in reversed(keys):
    myMessage = message
    myMessage = myMessage.replace("{username}", db[key]["username"])
    myMessage = myMessage.replace("{timestamp}", key)
    myMessage = myMessage.replace("{message}", db[key]["message"])
    if db[key]["username"] == "AlexB78":
      myMessage = myMessage.replace("{admin}", f"""<a href="/delete?id={key}">Dell</a>""")
    else:
      myMessage = myMessage.replace("{admin}", "")
      result += myMessage
      recent += 1
      if recent == 5:
        break
    return result
  
@app.route('/delete', methods=["GET"])
def deleteMessage():
  if request.headers["X-Replit-User-Name"] != "AlexB78":
    return redirect('/')
  results = request.values["id"]
  del db[results]
  return redirect('/')

    
app.run(host='0.0.0.0', port=81)


