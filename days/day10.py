###################
# bill calculator #
###################
# ask for bill
# split betweeen nr of people
# ask for tip percentage (5, 10 15%)
# ask for total bill

# 1. ask for bill
bill = float(input("What is the bill?: "))
# 2. how many are we?
nrOfPeople = int(input("How many people?: "))
# 3. if no tip, output bill / people
ppp_notip = bill / nrOfPeople
ppp_notip = round(ppp_notip, 2)
# print(f"You all owe {ppp}.")

# 4. if tipped, calculate
tip = int(input("How much will we tip? (5, 10, 15 %): "))

# total = bill + (bill / 100 * tip)
if tip == "" or tip == 0:
  print("No tip then")
  print(f"You all owe {ppp_notip}.")
else:
  bill_and_tip = bill + (bill / 100 * tip)
  ppp_andtip = (bill_and_tip) / nrOfPeople
  ppp_andtip = round(ppp_andtip, 2)
  print(f"Ok, the total with tip is {bill_and_tip}")
  print(f"You each owe {ppp_andtip}.")