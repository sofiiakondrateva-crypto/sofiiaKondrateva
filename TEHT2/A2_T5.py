print ("Program starting")

feed = input("\nInsert a closed compound word: ")
reversed= feed[::-1]
length= len(feed)
lastchar= feed[-1]

print(f"The word you inserted is '{feed}' and in reverse it is '{reversed}'.")
print(f"The inserted word length is {length}")
print(F"Last character is '{lastchar}'")

print ("\nTake substring from the inserted word by inserting...")

start = int(input("1) Starting point: "))
end = int(input("2) Ending point: "))
stepsize = int(input("3) Stepsize: "))
endpoint= feed[start:end:stepsize]

print(f"\nThe word '{feed}' sliced to the defined substring is '{endpoint}'.")
print ("Program ending.")