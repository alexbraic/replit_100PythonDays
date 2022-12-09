# how to build the name
# first 3 letters of the first name
# first 2 letters of the surname
# first 2 letters of the mom's maiden name
# last 2 letters of the place you were born
print("=== Star Wars name generator ===")
print(
    "Ok, to do this we need the following:\n- your first name\n- your last name\n- your mom's maiden name\n- the place where you were born"
)
mySWName = input("Get typin': ")
userName = mySWName.split()
newFname = f"{userName[0][:3]}{userName[1][:2]}".capitalize()
newLname = f"{userName[2][:2]}{userName[3][-2:]}".capitalize()
print(f"Your new name is:\n{newFname} {newLname}\nWow, that's a weird name!")
