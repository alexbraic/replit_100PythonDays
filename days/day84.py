# login page that uses replit db to store users and log them in if they exist
# the signup and login files are present in this file and can be cut and pasted in another location to test

from flask import Flask, redirect, request
from replit import db


app = Flask(__name__)

@app.route('/signup', methods=["POST"])
def createUser():
  keys = db.keys()
  form = request.form

  if form["username"] not in keys:
    db[form["username"]] = {"name": form["name"], "password": form["password"]}
    return redirect('/login')
  else:
    return redirect('/signup')

  
@app.route('/signup')
def singup():
  page = ''
  f = open('signup.html', 'r')
  page = f.read()
  f.close()

  return page


@app.route('/login', methods=["POST"])
def loggedOn():
  keys = db.keys()
  form = request.form

  if form["username"] not in keys:
    return redirect('/signup')
  else:
    if form["password"] == db[form["username"]]["password"]:
      return f"""Hello {db[form["username"]]["name"]}"""
    else:
      return redirect('/')


@app.route('/login')
def login():
  page = ''
  f = open('login.html', 'r')
  page = f.read()
  f.close()

  return page

  
@app.route('/')
def index():
  page = """
    <p><a href="/signup">Sign up here</a></p>
    <p><a href="/login">Login page</a></p>
  """
  return page
  
app.run(host='0.0.0.0', port=81)


# files
    
# signup.html      
# <div>
#   <form method="post" action="/login">
#     <p>Username: <input type="text" name="username" required></p>
#     <p>Name: <input type="text" name="name" required></p>
#     <p>Password: <input type="password" name="password" required></p>
#     <button type="submit">Login</button>
#   </form>
# </div>
  
# login.html 
# <div>
#   <form method="post" action="/login">
#     <p>Username: <input type="text" name="username" required></p>
#     <p>Password: <input type="password" name="password" required></p>
#     <button type="submit">Login</button>
#   </form>
# </div>