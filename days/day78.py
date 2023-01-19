from flask import Flask

app = Flask(__name__)

my_reflections = {}

my_reflections["77"] = {
  'day': "77",
  "link": "https://replit.com/@AlexB78/Day77100Days#main.py",
  'reflection': "I really should give more attention to this Flask thing"
}

my_reflections["78"] = {
  'day':
  "78",
  'link':
  "https://replit.com/@AlexB78/Day78100Days#main.py",
  'reflection':
  'Programming can be really demotivating, but keep at it, it might lead to something good.'
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


@app.route('/<page_number>')
def number(page_number):
  #global Reflections
  page = ""
  f = open("template/base_index.html", "r")
  page = f.read()
  f.close()

  page = page.replace("{day}", page_number)
  page = page.replace("{link}", my_reflections[page_number]["link"])
  page = page.replace("{reflection}", my_reflections[page_number]['reflection'])

  return page


app.run(host='0.0.0.0', port=81)
