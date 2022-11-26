# subroutines
#def rollDice():
# import random
# dice = random.randint(1, 6)
# print("You rolled", dice)

#rollDice()

# login system

# hard coded user and password
user = "Joe"
passwd = "passwd"


# define simple login logic
def login():
    uname = input("Username: ")
    upass = input("Password: ")

    while uname != user or upass != passwd:
        print("Wrong credentials, please try agin")
        uname = input("Username: ")
        upass = input("Password: ")


# first line, print welcome message
print("Welcome, please log in.")

# ask user to log in, and display a log in msg once successful login
loggedin = False
while loggedin == False:
    login()
    loggedin = True

print(f"Welcome back {user}!")