weight = float(input("Please enter your weight: "))
unit = input("Is this your weight in (K)g or (L)bs?: ")
if unit.upper() == "K":
    converted = weight * 2.2
    input("Your weight in Lbs is: " + str(converted))
elif unit.upper() == "L":
    converted = weight / 2.2
    input("Your weight in Kg is: " + str(converted))
else:
    print("Please enter a valid unit of measurement")
