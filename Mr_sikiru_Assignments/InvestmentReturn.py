deposit = int(input("Enter investment amount: "))
count = 0
for count in range(1, 31):
    investment_amount = deposit
    percentage = 0.07
    investment_amount *= percentage
    deposit += investment_amount
    print(f"The RoI is {investment_amount} investment return {deposit} for year{count}")


