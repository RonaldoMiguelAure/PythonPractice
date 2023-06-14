while True:
    try:
        temperature = float(input("Please enter the temperature outside:"))
    except ValueError:
        print("Sorry, I didn't understand that.")
        # repeat loop until valid temperature is entered
        continue
    else:
        break
        # valid temperature is entered, exit loop

while True:
    try:
        unit = input("Is that in (C)elcius or (F)ahrenheit?: ")
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    if unit.upper() == "C":
        converted_temperature = temperature
        break
    elif unit.upper() == "F":
        converted_temperature = (temperature - 32) * 5 / 9
        break
    else:
        print("Sorry, I didn't understand that.")
        continue

if converted_temperature > 30:
    print("It's hot outside!")
    print("I recommend drinking lots of water to stay hydrated.")
elif converted_temperature > 20:
    print("It's warm outside!")
    print("I recommend playing some soccer to enjoy the sun.")
elif converted_temperature > 0:
    print("It's nice outside")
    print("I recommend eating on the patio to enjoy the cool weather.")
else:
    print("It's cold outside!")
    print("I recommend you wear a jacket when you go out.")
