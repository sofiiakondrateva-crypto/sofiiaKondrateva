print("""Program starting.
Welcome to the unit converter program!
Follow the menu instructions below.""")

print("""\nOptions:
1 - Length
2 - Weight
0 - Exit""")
feed = int(input("Your choice: "))


if feed == 1:
    print("""Length options:
    1 - Meters to kilometers
    2 - Kilometers to meters
    0 - Exit""")
    choice = int(input("Your choice: "))
    if choice ==1:
        m = float(input("Insert meters: "))
        print(f"{m} m is {round(m/1000,2)} km")
    elif choice ==2:
        km = float(input("Insert kilometers: "))
        print(f"{km} km is {round(km*1000,2)} m")
    elif choice == 0:
        print(f"Exiting...")
    else:
        print("Unknown option.")
elif feed == 2:
    print("""Weight options:
    1 - Grams to pounds
    2 - Pounds to grams
    0 - Exit""") 
    choice = int(input("Your choice: "))
    if choice == 1:
        gr = float(input("Insert grams: "))
        print(f"{gr} g is {round(gr*0.002205,5)} lb")
    elif choice == 2:
        po = float(input("Insert pounds: "))
        print(f"{po} lb is {round(po/0.002205,5)} g")
    elif choice == 0:
        print(f"Exiting...")
    else:
        print("Unknown option.")
elif feed == 0:
    print(f"\nExiting...")
else:
     print("Unknown option.")

print("\nProgram ending.")