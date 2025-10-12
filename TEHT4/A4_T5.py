print("Program starting.")

starting_point = int(input("\nInsert starting point: "))
stopping_point = int(input("Insert stopping point: "))
inspection_point = int(input("Insert inspection point: "))



while True:
    if starting_point > stopping_point:
        print("\nStarting point value must be less than the stopping point value.")
    elif inspection_point not in range(starting_point, stopping_point+1):
        print("\nInspection value must be within the range of start and stop.")
    break


print("\nFirst loop - inspection with break:")
first_loop = []
for i in range(starting_point, stopping_point):
    if i == inspection_point:
         break
    first_loop.append(str(i))
print(" ".join(first_loop))

print("\nSecond loop - inspection with continue:")
second_loop = []
for i in range(starting_point, stopping_point):
    if i == inspection_point:
        continue
    second_loop.append(str(i))
print(" ".join(second_loop))

print("\nProgram ending.")
