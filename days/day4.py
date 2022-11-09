# challenge on Day4

# make up a story
# get input from user
import time
print("=== Your Adventure Simulator ===")
print("""
You'll be asked a bunch of questions,
then we'll make you up an amazing story
with YOU as the star!
""")
print()
name = input("Ok hero, please Enter your name: ")
nemesis = input("Who is your greatest enemy: ")
race = input("What's your nemesis race?: ")
superpower = input("Your superpower: ")
def react(r):
    if r == "1":
        print("What do you mean?! Who are you talking about?")
    elif r == "2":
        print("I'll be ready for him! He'll meet his end just like you ", nemesis, "!")
    elif r == "3":
        print("Not another one of these wankers..")
    else:
        print("You ruined it, The End!")
def go_in(g):
    for val in g:
        if val == "y":
            print("Ok then, let's get this basterd!")
            continue
        else:
            print()
            print("Ok chicken, run away, why don't ya?")
            print("Jeez... what a let down.")
            quit()

print()
print("""After many journeys,
you were finally able to track down your arch nemesis,""", nemesis,"!")
print("Off course he was hiding from you, knowing you finally mastered",superpower,",your ultimate super power!")
print("Hiding in an old cellar,",nemesis,"the", race,"had no way out...")
print()
time.sleep(10)
print("Is",name, "going to finally face his biggest enemy so far?")
act = input("(y/n):")
go_in(act)
print()
print("Having blocked his only exit,",name,"says:")
print("I finally have you trapped",nemesis,"you basterd! There's no more running from justice!")
print(nemesis,"trying to strike first, rushes with his axe at",name,"!")
print()
print("Waaaargh!!")
time.sleep(10)
print()
print("..But, just as his enemy started approaching", name, "evaded",nemesis,"and with his superpower,",superpower," our hero strikes his foe!")
print("With a loud roar", nemesis, "after that deadly blow, with his final words uttered...")
print("... you've finaly become a man",name,". Now the real test begins...")
print("... be prepared for when HE arrives...")
print("Shocked from what he heard",name,"races to his dying enemy's side.")
reaction = input("How do you react? (1 - surprised, 2 - angry, 3 - whatever)\n")
react(reaction)
time.sleep(7)
print("The end..?")
