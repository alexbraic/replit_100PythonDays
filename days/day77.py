from flask import Flask, redirect

app = Flask(__name__, static_url_path='/static')


@app.route('/git')
def git():
  return redirect("https://github.com/alexbraic")


@app.route('/')
def index():
  page = f"""<html><body>
  <p><a href="/56">56</a></p>
  </body>
  </html>
  """
  return page


@app.route('/56')
def fiftySix():
  myName = "Alex"
  title = "Day 56 Solution"
  text = "So, day 56 was all about using csv reading and file and folder manipulation to make 100 files in dozens of folders. This was tricky because the names of the folders and files were based on the top 100 streaming songs and so weren't simple to encode."
  image = "picard.jpg"
  link = "https://github.com/alexbraic/replit_100PythonDays/blob/main/days/day56.py"

  page = ""
  f = open("template/portfolio.html", "r")
  page = f.read()
  f.close()
  page = page.replace("{name}", myName)
  page = page.replace("{title}", title)
  page = page.replace("{text}", text)
  page = page.replace("{image}", image)
  page = page.replace("{link}", link)
  return page


app.run(host='0.0.0.0', port=81)
