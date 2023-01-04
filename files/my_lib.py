# example of a collection of functions to reuse


def range_ten():
  for i in range(10):
    print(i + 1)


def is_leap_year(year):
  """Determine whether a year is a leap year."""
  return int(year) % 4 == 0 and (int(year) % 100 != 0 or int(year) % 400 == 0)
