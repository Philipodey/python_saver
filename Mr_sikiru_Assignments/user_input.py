passes = 0
failures = 0
count = 1
number = int(input("Enter result (1=pass, 2=fail): "))
while number != -1:
    if number > -1 or number < -1:
        count += 1
        if number == 1:
            passes += 1
        elif number == 2:
            failures += 1
        else:
            number = (int(input("Enter result (1=pass, 2=fail): ")))
    number = (int(input("Enter result (1=pass, 2=fail): ")))
print("passes:", passes)
print("failures:", failures)
if passes > 8:
    print("Bonus to instructor")
