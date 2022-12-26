# read the csv file
# multiply cost by quantity
# add it all up to a total

import csv

with open("../files/Day54Totals.csv") as file:
    reader = csv.DictReader(file)

    total = 0.0
    for row in reader:
        rowSum = float(row['Cost']) * float(row['Quantity'])
        total += rowSum
        print(rowSum)
    print("===========================")
    print(f"Total: {round(total, 2)}")
