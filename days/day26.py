import os, time

# for i in range(1,1000):
#   print(i)
#   os.system("clear")

#title list and playlists
titles = [" MyPOD Music Player ", " Main Menu ", " Your playlists "]
playlist = ["Skipping Time", "Classic Rock"]

print(titles[0].center(60, "="))
time.sleep(1)
os.system("clear")

#print main menu
def main_menu():
  print(titles[1].center(60, "="))
  print("\tPress 1 to see Playlists")
  print("\tPress 2 to Exit")
  print()
  print("Press anything else to see the menu again")

def play_lists():
  print(titles[2].center(60, "="))
  print(f"\t1: {playlist[0]}")
  print(f"\t2: {playlist[1]}")
  print()
  print("To return to the Main Menu, press 0.")
main_menu()
press = int(input(""))
choice = "0"
os.system("clear")
while press != 2:
  if press == 1:
    play_lists()
    p_list = int(input())
    os.system("clear")
    if p_list == 1:
      print(f'Now playing {playlist[0]}. Enjoy!\n')
      ch = input("To return to playlists, press 0.\n> ")
      os.system("clear")
      if ch == int(0):
        play_lists()
        os.system("clear")
        #continue
    if p_list == 2:
      print(f'Now playing {playlist[1]}. Enjoy!\n')
      ch = input("To return to playlists, press 0.\n> ")
      os.system("clear")
      if ch == int(0):
        play_lists()
        os.system("clear")
    if p_list == 0:
      main_menu()
      continue
    
  
  else:
    main_menu()
    press = int(input(""))
