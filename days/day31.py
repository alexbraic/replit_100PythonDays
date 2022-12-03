# create 2 interfaces using print statements

import os
import time

# 1
title = "\033[31m=\033[0m=\033[36m=\033[0m \033[33mMusic App\033[0m \033[36m=\033[0m=\033[31m=\033[0m"

print(f"{title.center(100)}")
print()
print("🔥▶  Radio Gaga")
print("\t \033[33mQueen\033[0m")
print()
print()
prev = "prev"
print(f"{prev.upper()}")
print("\t\t \033[33mNEXT\033[0m")
print("\t\t \t\t  \033[35mPAUSE\033[0m")

time.sleep(5)
os.system("clear")

# 2
title2 = "WELCOME TO"
title3 = "\033[34m--    ARMBOOK    --\033[0m"
print(f"{title2.center(55)}")
print(f"{title3.center(64)}")
state1 = "\033[33mDefinitely not at rip off of\033[0m"
state2 = "\033[33ma certain other social\033[0m"
state3 = "\033[33mnetworking site.\033[0m"
h = "Honest."
u = "Username:"
p = "Password:"
#print(f"")
print()

print(state1.rjust(65, " "))
print(state2.rjust(65, " "))
print(state3.rjust(65, " "))
print()
print(f"\033[31m{h.center(55)}\033[0m")
print()
print(f"{u.center(55)}")
print(f"{p.center(55)}")