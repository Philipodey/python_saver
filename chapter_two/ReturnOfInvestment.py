principal = int(input("Enter amount to be invested: "))
percentage_rate = 0.07
number_of_years = int(input("Enter the number of years: "))
rate = 1 + percentage_rate
amount_on_deposit = float(principal(rate)**number_of_years)

print(f"The amount on deposit is {amount_on_deposit:.2f}")
