print("Program starting.")

print("""\nOptions:
1 - Celsius to Fahrenheit
2 - Fahrenheit to Celsius
0 - Exit""")
choice = int(input("Your choice: "))

if choice == 1:
    cel = float(input("Insert the amount of Celsius: "))
    far = float(1.8*cel+32)
    print(f"{round(cel,1)} °C equals to {round(far,1)} °F")
elif choice == 2:
    far = float(input("Insert the amount of Fahrenheit: "))
    cel = float((far - 32)/1.8)
    print(f"{round(far,1)} °F equals to {round(cel,1)} °C")
elif choice == 0:
    print(f"Exiting...")
else:
    print("Unknown option.")

print("\nProgram ending.")