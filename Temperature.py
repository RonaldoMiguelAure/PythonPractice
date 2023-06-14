temperature = float(input("What's the temperature outside?: "))
unit = input("Is that in (C)elcius or (F)ahrenheit?: ")
if unit.upper() == "C":
    if temperature > 30:
        print("It's a hot today!")
        print("Drink plenty of water.")
    elif temperature > 20:  # (20.30]
        print("It's nice outside.")
    elif temperature > 10:  # (10,20]
        print("It's cool outside.")
    else:
        print("It's cold outside!")
        print("Don't forget to bring a jacket.")

if unit.upper() == "F":
    if temperature > 86:
        print("It's a hot today!")
        print("Drink plenty of water.")
    elif temperature > 68:  # (20.30]
        print("It's nice outside.")
    elif temperature > 50:  # (10,20]
        print("It's cool outside.")
    else:
        print("It's cold outside!")
        print("Don't forget to bring a jacket.")

