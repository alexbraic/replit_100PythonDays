from flask import Flask, request

app = Flask(__name__)

users = {}
users["alex"] = {
  "username": "alex",
  "email": "alex@alex.com",
  "passwd": "Alexander1"
}
users["ali"] = {
  "username": "ali",
  "email": "alex@alex.com",
  "passwd": "No_aleeex1"
}
users["Alex"] = {
  "username": "Alex",
  "email": "alex@alex.com",
  "passwd": "Aleeeeeex1"
}


@app.route("/login", methods=["POST"])
def login():
  form = request.form
  isUser = False
  details = {}
  try:
    details = users[form["username"]]
    isUser = True
  except:
    return "Wrong credentials, please create a user"

  if form["email"] == details["email"] and form["passwd"] == details["passwd"]:
    return "Welcome"
  else:
    return "Wrong credentials, please create a user"


# <p>Website: <input type="url" name="website"> </p>
# <p>Age: <input type="number" name="age"> </p>
# <input type="hidden" name="userID" value="232"> </p>


@app.route('/')
def index():
  page = """<form method = "post" action="/login">
    <p>Userame: <input type="text" name="username" required> </p>
    <p>Email: <input type="Email" name="email" required> </p>
    <p>Password: <input type="password" name="passwd" required> </p>

    <button type="submit">Login</button>
  </form>
    """
  return page


app.run(host='0.0.0.0', port=81)