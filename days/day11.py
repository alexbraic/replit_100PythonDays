# How many seconds in a year?
# Is it a leap year?
import re

sec = 1
min = 60 * sec
hour = 60 * min
day = 24 * hour
week = 7 * day
year = 365 * day
leapYear = 366 * day
# total seconds in a minute
# print("Total mseconds in a minute: ", min)
# total seconds in a hour
# print("Total mseconds in an hour: ", hour)
# total seconds in a day
# print("Total mseconds in a day: ", day*3)
# total seconds in a year
# print("Total mseconds in a year: ", year)

print("=== Second Teller ===")
print()
print("This program will first print out how many seconds there are in the specified time frame.\n\n# Input example: 3 days\n# Output example: There are 259200 seconds in 3 days.\n")
print("After that, it can tell you if a year is a leap year or not, and how many seconds that year has.")
print()

# take  input
secFor = input("How many seconds in: ")
# split the input into 2 input items
timeframe = re.split("\s", secFor)

if timeframe[1] == "second" or timeframe[1] == "seconds":
  print(f"There are {int(float(timeframe[0]) * sec)} seconds in {secFor}.")
elif timeframe[1] == "minute" or timeframe[1] == "minutes":
  print(f"There are {int(float(timeframe[0]) * min)} seconds in {secFor}.")
elif timeframe[1] == "day" or timeframe[1] == "days":
  print(f"There are {int(float(timeframe[0]) * day)} seconds in {secFor}.")
elif timeframe[1] == "week" or timeframe[1] == "weeks":
  print(f"There are {int(float(timeframe[0]) * week)} seconds in {secFor}.")
elif timeframe[1] == "year" or timeframe[1] == "years":
  print(f"There are {int(float(timeframe[0]) * year)} seconds in {secFor}.")
print()
# How many seconds in a certain year?
secYear = input("And which year? ")
def is_leap_year(year):
    """Determine whether a year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
  
y = is_leap_year(int(secYear))
# print(y)

# check y and calculate seconds
if y == True:
  print(f"{secYear} is a leap year.")
  print(f"There are {leapYear} seconds in {secYear}.")
else:
  print(f"{secYear} is NOT a leap year.")
  print(f"There are {year} seconds in {secYear}.")