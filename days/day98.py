import schedule, time, os, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

password = os.environ['some_mail_pass']
username = os.environ['username']


def sendMail():
  # email content
  email = "Don't forget to take a break!"
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
  msg["Subject"] = "Break time"
  msg.attach(MIMEText(email, "html"))
  s.send_message(msg)
  del msg


def printMe():
  print("⏰")
  sendMail()


schedule.every(1).hours.do(printMe)

while True:
  schedule.run_pending()
  time.sleep(1)
