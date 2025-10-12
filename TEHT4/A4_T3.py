print("Program starting.")

star = int(input("\nInsert starting value: "))
stp = int(input("Insert stopping value: "))

print("\nStarting while-loop:")

while star<= stp-1:
    print(star, end=" ")
    star += 1
else:
    print(stp)

print("\nProgram ending.")