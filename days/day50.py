# idea saving system
# save idea in my.ideas
# add an idea
# load a random idea, hold, clear and go back to the menu

import os, time, random


def add():
    os.system("clear")
    idea = input("Idea > ")
    f = open("my.ideas", "a+")
    f.write(f'{idea}\n')
    f.close()


def show():
    f = open("my.ideas", "r")
    ideas = f.read().split("\n")
    f.close()
    ideas.remove("")
    idea = random.choice(ideas)
    print(idea)
    time.sleep(1)
    os.system("clear")


while True:
    menu = input("1: Add idea\n2. Show random idea\n")

    if menu == "1":
        add()
    else:
        show()

# it was a long day, so i actually just looked through the solution
# no time left today to think 😴
