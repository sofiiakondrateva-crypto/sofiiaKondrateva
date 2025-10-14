print("Program starting.")

feed = ""
word = ""

while feed != "0":
    print("""\nOptions:
    1 - Insert word
    2 - Show current word
    3 - Show current word in reverse
    0 - Exit""")
    feed = input("Your choice: ")

    if feed == "1":
        word = input("Insert word: ")
    elif feed == "2":
        print(f"Current word - {word}")
    elif feed == "3":
        print(f"Word reversed - {word[::-1]}")
    elif feed == "0":
        print("Exiting program.")
    else:
        print("Unknown option")


print("\nProgram ending.")