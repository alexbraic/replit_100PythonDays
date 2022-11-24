# bit random
import random

myNumber = random.randint(1, 100)
for i in range(10):
  myNumber = random.randint(1, 100)
  print(myNumber)
print()
for i in range(10):
  x = random.random()
  print(x)
print()
print(random.randint(5,10))
c = [1, 2, 3]
print()

def repeat(x, rep=1):
  for i in range(rep):
    print(x)

repeat("Alex", random.randint(1, 15))