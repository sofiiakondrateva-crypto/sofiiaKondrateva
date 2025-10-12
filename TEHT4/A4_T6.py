print("Program starting.")

feed=int(input("\nInsert a positive integer: "))

loop = [str(feed)]
steps = 0
while feed !=1:
    if feed %2==0:
        feed = feed // 2
    elif feed %2==1:
        feed = feed*3+1
    steps += 1
    loop.append(str(feed))
print(" ->".join(loop))
print(f"Sequence had {steps} total steps.")

print("\nProgram ending.")
