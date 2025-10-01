print("""Program starting.
Testing decision structures.""")

value = int(input("Insert an integer: "))

print("""Options:
1 - In one multi-branched decision
2 - In multiple independent if-statements
0 - Exit""")
choice = int(input("Your choice: "))

if choice == 1:
    print("Using one multi-branched decision structure.")
    if value >= 400:
        result = value+44
    elif value >= 200:
        result = value+22
    elif value >= 100:
        result = value+11
    else:
        result = value
    print(f"Result is {result}")
elif choice == 2:   
    print("Using multiple independent if-statements structure.")
    result = value
    if value >= 400:
        result += 44
    if value >= 200:
        result  += 22
    if value >= 100:
        result  += 11
    print(f"Result is {result}")
elif choice == 0:
    print(f"Exiting...")
else: 
    print("Unknown option.")

print("\nProgram ending.")