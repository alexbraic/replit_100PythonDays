"""Name of exam.:
Max possible score:
yourscore:
90% A+
80% A-
70% B
60% C
50% D
40% E"""

examName = input("What is the name of the exam?\n")
maxScore = float(input("What is maximum score one can get?\n"))
yourScore = float(input("How much did you get?\n"))

perc = round((yourScore / maxScore) * 100, 2)

# print(perc)

if perc >= 90.0 and perc < 100.0:
    print(f"That's {perc}% of the grade!")
    print("So you get an A+! Well done! 😁")
elif perc >= 80.0:
    print(f"That's {perc}% of the grade!")
    print("A- 😁")
elif perc >= 70.0:
    print(f"That's {perc}% of the grade!")
    print("B 😁")
elif perc >= 60.0:
    print(f"That's {perc}% of the grade!")
    print('Ah well, the "C" is full of average sized fish! Geit it?!😁')
elif perc >= 50.0:
    print(f"That's {perc}% of the grade!")
    print("D for dear god... haha 😄")
elif perc >= 40.0 and perc < 50.0:
    print(f"That's {perc}% of the grade!")
    print("Barelly made it, you get an E! 😝")
else:
    print(f"That's {perc}% of the grade!")
    print("Yea, that's an F! You'll need to take that test again!")
