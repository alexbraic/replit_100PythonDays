# store dicts with urls of prodcts, current price and price you would like to buy at
# scrape every day for changes
# once the desired price has been reached, email with the link and price

import os, time, requests, smtplib, re, schedule
from replit import db
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# used to delete the key after testing that the email works
#keys = db.keys()
#for key in keys:
#  del db[key]


def mailMe(title, price):
  # email auth variables, kept in repl secrets
  password = os.environ['pass']
  username = os.environ['user']

  server = 'smtp.gmail.com'
  port = 587

  s = smtplib.SMTP(host=server, port=port)
  s.starttls()
  s.login(username, password)

  msg = MIMEMultipart()
  msg["To"] = username
  msg["From"] = username
  msg["Subject"] = "Sale on!"

  email = f"""The price of the {title} 
    has gone down to €{price}.
    <a href='https://www.did.ie/products/asus-tuf-gaming-a15-15-6-amd-ryzen-5-8gb-512gb-laptop-fa506ihr-hn057w'>Click here</a>"""

  msg.attach(MIMEText(email, 'html'))
  s.send_message(msg)
  del msg


keys = db.keys()


def getDeal():
  url = "https://www.did.ie/products/asus-tuf-gaming-a15-15-6-amd-ryzen-5-8gb-512gb-laptop-fa506ihr-hn057w"

  response = requests.get(url)
  html = response.text
  #print(html)

  soup = BeautifulSoup(html, 'html.parser')

  # get the name of the item
  title = soup.find('h1', class_='product_name title')
  title_text = title.text

  # get the price of the item
  price = soup.find('p', class_='modal_price subtitle')
  #print(price)
  cost = price.find('span', class_='span_money money sale')
  #print(cost.text[1:])
  current_price = float(cost.text[1:])

  if title_text not in keys:
    db[title_text] = {'current_price': current_price}

  mailMe(title_text, current_price)
  counter = 0
  if current_price < 900.00:
    mailMe(title_text, current_price)
    couter += 1
    pass

  if counter == 1:
    del db[title_text]


# test it
# getDeal()

# check the price every 3 days
schedule.every(72).hours.do(getDeal)
# run the cron job
while True:
  schedule.run_pending()
  time.sleep(1)
