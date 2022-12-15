#my2DList = [ ["Johnny", 21, "Mac"],
#             ["Sian", 19, "PC"],
#             ["Gethin", 17, "PC"] ]

#my2DList[1][2] = "Linux"

# bingo card
# randomly generate numbers from 0-90

import random

randValue = []
for i in range(8):
    randValue.append(random.randint(1, 90))

randValue.sort()
randValue.insert(4, "BINGO")
print(randValue)

bList = [[randValue[0], randValue[1], randValue[2]],
         [randValue[3], randValue[4], randValue[5]],
         [randValue[6], randValue[7], randValue[8]]]

print(bList[1][1])
