import os
from flask import Flask, redirect, request, session
from replit import db

app = Flask(__name__)
app.secret_key = os.environ['sessionKey']


# index
@app.route('/')
def index():
  if session.get("loggedIn"):
    return redirect('/home')
  page = """
    <p><a href="/signup">Sign up here</a></p>
    <p><a href="/login">Login page</a></p>
  """
  return page


@app.route("/signup", methods=["POST"])
def createUser():
  if session.get("loggedIn"):
    return redirect('/home')

  keys = db.keys()
  form = request.form

  if form["username"] not in keys:
    db[form["username"]] = {"name": form["name"], "password": form["password"]}
    return redirect('/login')
  else:
    return redirect('/signup')


@app.route('/login', methods=["POST"])
def doLogin():
  if session.get("loggedIn"):
    return redirect('/home')
  keys = db.keys()
  form = request.form
  if form["username"] not in keys:
    return redirect('/login')
  else:
    if form["password"] == db[form["username"]]["password"]:
      session['loggedIn'] = form["username"]
      return redirect('/home')
    else:
      return redirect('/')


@app.route('/home')
def home():
  page = ''
  page += f"""
          <p>Welcome, {db[session["loggedIn"]]["name"]}!</p>
          <button type='submit' onclick="location.href='/reset'">Log out</button>
          """
  return page


@app.route('/reset')
def reset():
  session.clear()
  return redirect('/')


@app.route('/signup')
def signup():
  if session.get("loggedIn"):
    return redirect('/home')
  page = ''
  f = open('signup.html', 'r')
  page = f.read()
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


app.run(host='0.0.0.0', port=81)

# files

# signup.html
#<div>
#  <form method="post" action="/signup">
#    <p>Username: <input type="text" name="username" required></p>
#    <p>Name: <input type="text" name="name" required></p>
#    <p>Password: <input type="password" name="password" required></p>
#   <button type="submit">Create</button>
#  </form>
#</div>

# login.html
#<div>
#  <form method="post" action="/login">
#    <p>Username: <input type="text" name="username" required></p>
#    <p>Password: <input type="password" name="password" required></p>
#    <button type="submit">Login</button>
#  </form>
#</div>
