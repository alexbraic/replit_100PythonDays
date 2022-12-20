# write to a file
# f = open("test.txt", "a+")
# writeText = input("> ")
# f.write(f"{writeText}\n")
# f.close()

# todo
# enter 3 letter initials, score out of 100k
# save to high.score file
# in append mode
# ex INI 23255
# ask if finish entering the data
end = False
f = open("high.score", "a+")
print("Enter your 3 initials and score (between 1 - 100k).")
while True:
    initial = input("Initials: ").strip().upper()
    if len(initial) < 3 or len(initial) > 3 or initial.isalpha() == False:
        print(
            "Incorrect format, please enter 3 initals only. And no numbers.🙂")
        print()
        continue

    score = int(input("Score: "))

    if score < 1 or score > 100000:
        print("Score too low/high or not a number. Please try again.")
        continue
    f.write(f"{initial} {score}\n")

    print()
    more = input("Enter more scores? (y/n): ").strip().lower()
    if more == "n":
        f.close()
        break
