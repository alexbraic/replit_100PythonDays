# for <new_variable> in range (<number_of_values):
#   <repeat_this_code>

# example: a loan of 1000 over 10 years at 5% APR
print("=== Loan calculator ===")

loan = float(input("Please enter how much you are loaning\n> "))
years = float(input("Please enter how many years the loan is for\n> "))
apr = float(input("Please enter your APR rate\n> "))
initial = loan
for i in range(1, int(years) + 1):
    loan += (loan / 100) * apr
    print(f"Year {i} is {round(loan,2)}")

print()
print(f"You paid ${round(loan - initial, 2)} in interest!")
