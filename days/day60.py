# time
import datetime

#today = datetime.date.today()
#print(today)
#print()

#day = int(input("Day: "))
#month = int(input("Month: "))
#year = int(input("Year: "))

#date = (datetime.date(year, month, day))
#print(date)
#print()
# timde delta (delta = difference)
#difference = datetime.timedelta(days=14)

#new_date = today + difference
#print(new_date)

#holiday = datetime.date(year=2023, month=1, day=1)

#if holiday > today:
#  print("Coming soon")
#elif holiday < today:
#  print("Hope you enjoyed it")
#else:
#  print("HOLIDAY TIME!")


# Today's challenge

# work out today's date
# ask the user for the name of the event and date
# Objective: how many days until event and display
# if event = today => emoji + today
# if event = in the past => sad emoji and how many days ago the event happened

today = datetime.date.today()
print(f"Today's date: {today}")
print()
print("Enter the date of the event below.")
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

event = datetime.date(year, month, day)
diff = (event - today).days

print()
if diff > 0:
  print(f'{diff} days to event')
elif diff < 0:
  print("That's gone already 😭😭😭😭😭")
else:
  print(f"😁😁😁 Let's go!")