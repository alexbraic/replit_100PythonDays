# Blog
# if logged in as replit user (me), see '/admin' page where i
#+can add articles
# save articles in replit db
# use Replit Authentication to check if i am the user

import os
from flask import Flask, redirect, request, session
from replit import db
from datetime import datetime

app = Flask(__name__)
# a new key needs to be created in Replit
# but the secret key does not really need to be used this time around
app.secret_key = os.environ["sessionKey"]

# the main page of the blog for users other than the admin
@app.route('/')
def index():
  username = request.headers['X-Replit-User-Name']
  if username == 'AlexB78':
    return redirect('/admin')
  else:
    return redirect('/nope')
  page = ""
  f = open("blog.html", "r")
  page += f.read()
  page = page.replace("{content}", getArticles())
  f.close()
  return page


# redirect any other user that tries to log in
@app.route('/nope')
def nope():
  return "Sorry, not allowed!"


# main page for adding new articles
@app.route('/admin')
def home():
  # check that i am the user; redirect if it isn't me
  username = request.headers['X-Replit-User-Name']
  if not username == 'AlexB78':
    return redirect('/nope')
  # build the page, use welcome note and see content
  page = ''
  page += f"""
          <p>Welcome, {username}!</p>
          """
  f = open("edit.html", "r")
  page += f.read()
  page = page.replace("{content}", getArticles())
  f.close()

  return page


# add a new arcticle
@app.route('/add', methods=["POST"])
def add():
  # get the form and create the dict. entry
  form = request.form
  entry = {"title": form["title"], "date": form["date"], "body": form["body"]}
  # each new entry has a timestamp to sort it in the db
  db[datetime.now()] = entry
  return redirect('/admin')


# bind each peace of article information to its rightful place
def getArticles():
  entry = ""
  f = open('entry.html', 'r')
  entry = f.read()
  f.close()
  keys = db.keys()
  content = ""
  for key in keys:
    thisEntry = entry
    thisEntry = thisEntry.replace("{title}", db[key]["title"])
    thisEntry = thisEntry.replace("{date}", db[key]["date"])
    thisEntry = thisEntry.replace("{body}", db[key]["body"])
    content += thisEntry
  return content


# run the app on localhost, port 81
app.run(host='0.0.0.0', port=81)


# files
#================================
# blog.html
#<!DOCTYPE html>
#<html lang="en">
#<head>
#  <meta charset="UTF-8">
#  <meta http-equiv="X-UA-Compatible" content="IE=edge">
#  <meta name="viewport" content="width=device-width, initial-scale=1.0">
#  <script src="https://replit.com/public/js/repl-auth-v2.js"></script>
#  <title>The Blog</title>
#</head>
#<body>
#  <title>Day 86 Challenge, The Blog</title>
#  <button onclick="LoginWithReplit()"> Login </button>
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