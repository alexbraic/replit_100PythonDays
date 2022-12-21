# open the file to be read
f = open("../files/highScore.txt", "r")

# create 2 empty lists to hold future values
highscores = []
hs = []

# loop through the lines of text, read them and add them to the
while True:
    content = f.readline().strip().split()
    # stop reading at empty line
    if not content:
        break
    # this list keeps all the data intact outside the loop
    highscores.append(content)
    # append the score only
    hs.append(content[1])

    # once the hs has 2 items to compare, keep the highest
    if len(hs) == 2:
        if hs[1] > hs[0]:
            hs.pop(0)
        else:
            hs.pop(1)
#close the file
f.close()

# print in a nice format
print("=== Score list ===")
print()
for line in highscores:
    print(f"{line[0]:>8}: {line[1]:^6}")
print()
print(f"Highest score: {hs[0]}")
