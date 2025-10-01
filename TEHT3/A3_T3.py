print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs.")
feed = input("Before the menu, please insert your name: ")

print("\nOptions:")
print(" 1 - Print welcome message")
print(" 0 - Exit")
choice = int(input("Your choice: "))

if choice == 1:
    print(f"Welcome {feed}!")
elif choice == 0:
    print(f"Exiting...")
else:
    print("Unknown option.")

print("\nProgram ending.")