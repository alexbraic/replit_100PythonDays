# Blog
# login page
# if logged in see list of blog posts
# save them in replit db
# if not logged in, just see a list of blog articles

# a session key needs to be created
#db["alex"] = {"username": "alex", "password": "Alex1"}

import os
from flask import Flask, redirect, request, session
from replit import db
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ['sessionKey']


# index
@app.route('/')
def index():
  if session.get("loggedIn"):
    return redirect('/home')
  page = """
    <button type='submit' onclick="location.href='/login'">Login</button>
  """
  #page = ""
  f = open("blog.html", "r")
  page += f.read()
  page = page.replace("{content}", getArticles())
  f.close()

  return page


@app.route('/login')
def login():
  if session.get("loggedIn"):
    return redirect('/home')
  page = ""
  f = open('login.html', 'r')
  page = f.read()
  f.close()
  return page


@app.route('/login', methods=["POST"])
def doLogin():
  if session.get("loggedIn"):
    return redirect('/home')
  keys = db.keys()
  form = request.form
  if form["username"] == db["alex"]["username"] and form["password"] == db[
      "alex"]["password"]:
    session['loggedIn'] = form["username"]
    return redirect('/home')
  else:
    return redirect('/')


@app.route('/home')
def home():
  if not session.get("loggedIn"):
    return redirect('/')
  page = ''
  page += f"""
          <p>Welcome, {db[session["loggedIn"]]["username"].capitalize()}!</p>
          <button type='submit' onclick="location.href='/reset'">Log out</button>
          """
  f = open("edit.html", "r")
  page += f.read()
  page = page.replace("{content}", getArticles())
  f.close()

  return page


@app.route('/add', methods=["POST"])
def add():
  form = request.form
  entry = {"title": form["title"], "date": form["date"], "body": form["body"]}
  db[datetime.now()] = entry
  return redirect('/home')


@app.route('/reset')
def reset():
  session.clear()
  return redirect('/')


def getArticles():
  entry = ""
  f = open('entry.html', 'r')
  entry = f.read()
  f.close()
  keys = db.keys()
  content = ""
  for key in keys:
    thisEntry = entry
    if key != "alex":
      thisEntry = thisEntry.replace("{title}", db[key]["title"])
      thisEntry = thisEntry.replace("{date}", db[key]["date"])
      thisEntry = thisEntry.replace("{body}", db[key]["body"])
      content += thisEntry
  return content


app.run(host='0.0.0.0', port=81)

# files
#================================
# login.html
#<div>
#  <form method="post" action="/login">
#    <p>Username: <input type="text" name="username" required></p>
#    <p>Password: <input type="password" name="password" required></p>
#    <button type="submit">Login</button>
#  </form>
#</div>
#================================
# blog.html
#<!DOCTYPE html>
#<html lang="en">
#<head>
#  <meta charset="UTF-8">
#  <meta http-equiv="X-UA-Compatible" content="IE=edge">
#  <meta name="viewport" content="width=device-width, initial-scale=1.0">
#  <title>The Blog</title>
#</head>
#<body>
#  <title>Day 86 Challenge, The Blog</title>
#  <hr>
#  {content}
#</body>
#</html>
#================================
# entry.html
#<h2>{title}</h2>
#<h3>{date}</h3>
#<p>{body}</p>
#<hr>
#================================
# edit.html
#<!DOCTYPE html>
#<html lang="en">
#<head>
#  <meta charset="UTF-8">
#  <meta http-equiv="X-UA-Compatible" content="IE=edge">
#  <meta name="viewport" content="width=device-width, initial-scale=1.0">
#  <title>Day 86 Challenge, The Blog</title>
#</head>
#<body>
#  <hr>
#  <form method='post' action='/add'>
#    <p>Title: <input type="text" name="title"></p>
#    <p>Date: <input type="date" name="date"></p>
#    <p>Body: <input type="text" name="body"></p>
#    <button type="submit">Submit</button>
#    <hr>
#  </form>
#  {content}
#</body>
#</html>
