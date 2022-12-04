# lists

timetable = ["Computer Science", "Math", "English", "Art", "Sport"]

for i in timetable:
    print(i)

# create a list that contains a greeting in multiple languages
# randomply print out one when run
print()
import random

greeting = [
    "Welcome", "Bun venit", "Bienvenidos", "欢迎 (Huānyíng)", "Bem-vindo"
]

g = random.randint(0, (len(greeting) - 1))
print(f"{greeting[g]}")