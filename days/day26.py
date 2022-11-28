import os, time

# for i in range(1,1000):
#   print(i)
#   os.system("clear")

#title list and playlists
titles = [" MyPOD Music Player ", " Your playlists "]
playlist = ["Skipping Time", "Classic Rock"]

print(titles[0].center(60, "="))
time.sleep(1)
os.system("clear")

#print main menu
#def main_menu():
print("\tPress 1 to see Playlists")
print("\tPress 2 to Exit")
print("Press anything else to see the menu again")
press = int(input(""))
  #return press
  
#main_menu()
choice = "0"
while True:
  if press == 1:
    #os.system("clear")
    print(titles[1].center(60, "="))
    print(f"\t1: {playlist[0]}")
    print(f"\t2: {playlist[1]}")
    choice = input("")
    if choice == "1":
      print(f'Playing {playlist[0]}')
      continue
    if choice == "2":
      print(f'Playing {playlist[1]}')
      continue
    if choice == "0":
      main_menu()
  elif press == 2:
    print("Goodbye")
    break
  else:
    print("\tPress 1 to see Playlists")
    print("\tPress 2 to Exit")
    print("Press anything else to see the menu again")
    press = int(input(""))
