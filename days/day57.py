# recursion

def factorial(value):
  if value == 1:
    return 1
  else:
    return value * factorial(value -1)

print(factorial(5))


#def reverse(value):
#  if value <= 0:
#    print("Done!")
#  else:
#    for i in range(value):
#      print("😎", end="")
#    print()
#    reverse(value-2)

#reverse(10)


