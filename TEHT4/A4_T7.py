import math

print("Program starting.")

print("\nCheck multiplicative persistence.")
feed = int(input("Insert an integer: "))
steps = 0 

while True:
    if len(str(feed)) > 1:
        digits = [int(d) for d in str(feed)]
        product = math.prod(digits)
        feed = product
        steps += 1
        print(" * ".join([str(d) for d in digits]), "=", product)
    else:
        break 
     
print("No more steps.")

print(f"\nThis program took {steps} step(s)")

print("\nProgram ending.")