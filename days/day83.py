from flask import Flask, request

app = Flask(__name__, static_url_path='/files/template')

my_reflections = {}

my_reflections["77"] = {
  'day':
  "77",
  "link":
  "https://replit.com/@AlexB78/Day77100Days#main.py",
  'reflection':
  "I really should give more attention to this Flask thing. Maybe read more about it, or check out more projects built around it."
}

my_reflections["78"] = {
  'day':
  "78",
  'link':
  "https://replit.com/@AlexB78/Day78100Days#main.py",
  'reflection':
  "Programming can be really demotivating when it doesn't go the way you want it to go, but keep at it, it might lead to something good."
}


@app.route('/')
def index():
  page = f"""<html>
              <body>
                <p><a href="/77">77</a></p>
                <p><a href="/78">78</a></p>
              </body>
            </html>
  """
  return page


@app.route('/<page_number>', methods=["GET"])
def number(page_number):
  # register the arguments and change accordingly
  get = request.args
  # default style as you go on the page
  style = "regular"
  # change the style (theme) to the new one
  if get != {}:
    style = get["style"]

  page = ""
  f = open("files/template/base_index.html", "r")
  page = f.read()
  f.close()

  page = page.replace("{day}", page_number)
  page = page.replace("{link}", my_reflections[page_number]["link"])
  page = page.replace("{reflection}",
                      my_reflections[page_number]['reflection'])
  # replaces the theme file usigng the GET argument
  page = page.replace("{style}", style)

  return page


app.run(host='0.0.0.0', port=81)
