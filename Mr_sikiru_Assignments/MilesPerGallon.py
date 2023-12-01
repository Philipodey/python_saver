miles_driven = int(input("Enter the miles driven(enter -1 to quit): "))
gallons = float(input("Enter the gallons used(enter -1 to quit): "))
miles_per_gallon = float(miles_driven / gallons)
print(f"The miles per gallon is {miles_per_gallon:.2f}")
total_miles_per_gallon = 0
count = 1
while miles_driven != -1 and gallons != -1:
    count += 1
    total_miles_per_gallon += miles_per_gallon
    miles_driven = int(input("Enter the miles driven(enter -1 to quit): "))
    gallons = float(input("Enter the gallons used(enter -1 to quit): "))
    miles_per_gallon = float(miles_driven / gallons)
    print(f"The miles per gallon is {miles_per_gallon:.2f}")
print(f"The total miles per gallon is {total_miles_per_gallon:.2f}")
