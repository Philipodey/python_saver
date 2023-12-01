age = int(input("Enter the age: "))
print(f"The age of the patient is {age}")
maximum_heart_rate = 220 - age
print(f"The maximum heart rate is {maximum_heart_rate}")
physical_intensity = float(input("Enter physical intensity between 0.64 to 0.96: "))
if 0.64 >= physical_intensity <= 0.76:
    target_heart_rate = maximum_heart_rate * physical_intensity
    print(f"The moderate physical intensity is {target_heart_rate}")
else:
    target_heart_rate = maximum_heart_rate * physical_intensity
    print(f"The vigorous physical intensity is {target_heart_rate}")