# the password and reg_pass values are saved as secters in Replit
import os

password = os.environ['password']
reg_pass = os.environ["reg_pass"]

userPass = input("Password> ")
if userPass == password:
  print("Hello normie!")
elif userPass == reg_pass:
  print("Hello admin!")
else:
  print("Better luck next time")