print("Program starting.")

print("Insert two integers.")
first = int(input("Insert first integer: "))
scnd =int(input("Insert second integer: "))

print("Comparing inserted integers.")
if first < scnd:
    print("Second integer is greater.")
elif scnd < first:
    print("First integer is greater.")
else: 
    print("Integers are the same")

print("\nAdding integers together")
sum = int(first + scnd)
print(f"{first} + {scnd} = {sum}")

print("\nChecking the parity of the sum...")
if sum % 2 == 0:
    print("Sum is even.")
else:
    print("Sum is odd.")

print("Program ending.")