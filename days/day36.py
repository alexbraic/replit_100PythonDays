# string formatting
# create a list
# hold first name and surname separate
# no duplicates
# add name and print the list

# "i know you" list
iky = []
while True:
    print("Do i know you?")
    # get the names and format them
    fname = input("What's your name again? ").strip().capitalize()
    sname = input("And your surname? ").strip().capitalize()
    print()

    # hold the full names and check for duplicates
    full_name = (f"{fname} {sname}")
    if len(iky) == 0:
        iky.append(full_name)
    elif full_name not in iky:
        iky.append(full_name)
    else:
        print(f"Ah yea, i've met you before, hi {fname}!")
        print()

    # list the current names
    for i in iky:
        print(i)
    print()

    # option to add a new name or exit
    print("And who are you?")
    print("(1 to introduce yourself, 2 to walk away (and exit program))")
    print("1. Your friend, remember?")
    print("2. You don't know me...")
    x = int(input("> "))
    if x == 1:
        continue
    else:
        break
