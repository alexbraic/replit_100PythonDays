# scrape replit every 6 hrs
# https://replit.com/community-hub
# send emails for new interesting repls

import schedule, time, os, smtplib, requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Replit import db
from bs4 import BeautifulSoup

keys = db.keys()
for key in keys:
  del db[key]


def sendMail(text, link):
  password = os.environ['some_mail_pass']
  username = os.environ['username']
  # which server
  server = "smtp.gmail.com"
  port = 587
  # connect to server
  s = smtplib.SMTP(host=server, port=port)
  s.starttls()
  s.login(username, password)

  msg = MIMEMultipart()
  msg["To"] = username
  msg["From"] = username
  msg["Subject"] = "Check this out!"
  # email content
  email = f"""<a href='{link}'>{text}</a>"""
  msg.attach(MIMEText(email, "html"))
  s.send_message(msg)
  del msg


interests = ["teams", "education"]


def getHub():
  url = "https://replit.com/community-hub"
  response = requests.get(url)
  html = response.text

  soup = BeautifulSoup(html, 'html.parser')

  repl_links = soup.find_all('div', class_='css-36v8q4')

  keys = db.keys()
  counter = 0
  for link in repl_links:
    if 'Community spaces' in link.text:
      break
    if counter != 0:
      print(link.text)
      thisLink = link.find('a')['href']
      print(thisLink)
    words = link.text.split()
    interested = False
    for word in words:
      if word.lower() in interests:
        interested = True
    if interested and link.text not in keys:
      db[link.text] = thisLink
      sendMail(link.text, thisLink)
    counter += 1


getHub()
schedule.every(6).hours.do(sendMail)

while True:
  schedule.run_pending()
  time.sleep(1)
