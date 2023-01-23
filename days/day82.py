from flask import Flask, request

app = Flask(__name__)


@app.route('/language', methods=["GET"])
def index():
  get = request.args

  if get['lang'].lower() == "en":
    return "Hello Alex"
  elif get['lang'].lower() == "es":
    return "Buenos dias Alex"
  return "No data"


app.run(host='0.0.0.0', port=81)