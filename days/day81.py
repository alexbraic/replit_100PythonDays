from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
  page = """
  <a href="/human"><button type="button">Login page</button></a>
  """
  return page

@app.route('/human')
def human():
  page = """
  <form method="post" action="/letssee">
    <div style="padding: 5px">
      <label for="yesno">Are you made of metal?</label>
      <input type="radio" name="yesno" value="yes"><label for="yes">Yes</label>
      <input type="radio" name="yesno" value="no"><label for="no">No</label>
    </div>
    <div style="padding: 5px">
      <label for="textbox">What is the value of double infinity?</label>
      <input type="text" placeholder="Enter answer here" name="textbox" id="textbox">
    </div>
    <div style="padding: 5px">
      <label for="food">Which is your favorite food?
      <select name="food">
        <option value="Human food">Human food</option>
        <option value="Synthetic Oil">Synthetic Oil</option>
      </select>
      </label>
    </div>
    <label for="check">
    <div class="input-container" style="padding: 5px; margin-left: 5px; height: 50px; width: 200px; background-color: lightgrey; border-inline-width: 3px; border-radius: 5px;">
      <div style="margin-top: 15px;">
        <input type="checkbox" name="check" value="done">
        <span>I'm not a robot</span>
      </div>
      <div>
        <span style="float:right;margin-top: -35px;"><img src="https://www.gstatic.com/recaptcha/api2/logo_48.png"></span>
      </div>
    </div>
    </label>
    <div style="padding: 5px;">
      <button type="submit">Submit</button>
    </div>
  </form>
  """
  return page


@app.route('/letssee', methods=["POST"])
def letssee():
  form = request.form
  #value = request.form.getlist('check') 
  #checked = {"yesno":"yes", "food":"Human food", "textbox": None, "check": "done"}
  
  if form["yesno"] == "no" and form["food"] == "Human food" and form["textbox"] != None and form["check"] != None:
    return "Welcome, human! 😁"
  else:
    return "Heh, silly robot! Go away! 😤"

app.run(host='0.0.0.0', port=81)