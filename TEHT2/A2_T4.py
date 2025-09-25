print("Program starting.")
print("Estimate how many minutes you spent on programming...")

A1_T1 = int(input("\nA1_T1: "))
A1_T2 = int(input("A1_T2: "))
A1_T3 = int(input("A1_T3: "))
A1_T4 = int(input("A1_T4: "))
A1_T5 = int(input("A1_T5: "))
A1_T6 = int(input("A1_T6: "))
A1_T7 = int(input("A1_T7: "))

total = (A1_T1 + A1_T2 + A1_T3 + A1_T4 + A1_T5 + A1_T6 + A1_T7)
average = round(total/ 7,2)
rounded = round(average)

print(f"\nIn total you spent {total} minutes on programming.")
print(f"Average per task was {average} min and same rounded to the nearest integer {rounded} min.")

print("\nProgram ending.")
