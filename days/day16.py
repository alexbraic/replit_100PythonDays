# second version of while loop
print("Fill in the blank lyrics!")
print()

counter = 0
while True:
  one = input("Never gonna ______ you up.\n\t\t\t") # give
  counter += 1
  if one == "give":
    two = input("Never gonna ______ you down.\n\t\t\t") #let
    counter += 1
    if two == "let":
      three = input("Never gonna ______ around and desert you.\n\t\t\t") #run
      counter += 1
      break
  else:
    print("Nope, try again")
print()
if counter == 3:
  print(f"Well done! It only took you {counter} attempts.")
elif counter <= 5:
  print(f"Well done! {counter} times! Almost as good as me!")
else:
  print("Whoa! That took a while 😅")