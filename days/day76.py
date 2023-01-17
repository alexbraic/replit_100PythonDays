from flask import Flask
import datetime

app = Flask(__name__, static_url_path="/static")


@app.route('/')
def index():
  page = f"""<html><body>
  <p><a href="/home">Go home</a></p>
  <p><a href="/port">Fake portfolio</a></p>
  </body>
  </html>
  """
  return page


@app.route('/port')
def port():
  page = f"""<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Practice</title>
  <link href="files/style.css" rel="stylesheet" type="text/css" />
</head>

<body>
  <div class="divs">
    <h2>HTML/CSS Practice</h2>
    <p>This is just a quick exercise.</p>
    <p>This website is meant to have 5 projects from the current 100 days of code journey. But, as that seems like a lot
      of extra effort for not much punch, i will only link to 1.</p>
    <p>For a more relevant exercise in HTML/CSS, go to my <a
        href="https://alexbraic.github.io/bloomerang/" target="_blank">Bloomerang</a> website.</p>
  </div>

  <div class="divs">
    <h2>Day 55</h2>
    <p>A ToDo list program that persists data to a file. It can load/save to that file.</p>
    <a href="https://github.com/alexbraic/replit_100PythonDays/blob/main/files/Replit_day55.png"
      target="_blank">Day55</a>
  </div>

  <script src="files/script.js"></script>

  <!--
  This script places a badge on your repl's full-browser view back to your repl's cover
  page. Try various colors for the theme: dark, light, red, orange, yellow, lime, green,
  teal, blue, blurple, magenta, pink!
  -->
  <script src="https://replit.com/public/js/replit-badge.js" theme="red" defer></script>
</body>

</html>
  """
  return page


@app.route('/home')  # Creates the path to the home page
def home():  # Subroutine to create the home page
  today = datetime.date.today()
  page = f"""<html>
    
  <head>
    <title>David's World Of Baldies</title>
  </head>


  <body>
  <h1>Dave's World of Baldies</h1> 
  <h2>Welcome to our website!</h2>
  <h2>{today}</h2>
  <p>We all know that throughout history some of the greatest have been Baldies, let's see the epicness of their heads bereft of hair.</p>

  <h2>Gallery of Baldies</h2>
  <p>Here are some of the legends of the bald world.</p>

  <img src="images/picard.jpg" width = 30%> 
  <p><a href = "https://memory-alpha.fandom.com/wiki/Star_Trek:_Picard">Captain Jean Luc Picard: Baldest Star Trek captain, and legend.</a></p>

  <ul>
    <li>Beautiful bald man</li>
    <li>Calm and cool under pressure</li>
    <li>All the Picard memes</li>
  </ul>

  <p><a href = "page2.html">Go to page 2</a></p>
  
</body>
  
</html>

"""
  # Three quotes - I'm going to write or paste my HTML code here. The HTML gets assigned to the page variable
  return page  # returns the contents of the page variable


app.run(host='0.0.0.0', port=81)
