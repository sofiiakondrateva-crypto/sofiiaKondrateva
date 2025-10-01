print("Program starting.")
print("String comparisons")
frst = input("Insert first word: ")
chr = input ("Insert a character: ")


if chr in frst:
    print(f"Word '{frst}' contains character '{chr}' ")
else: 
    print(f"Word '{frst}' doesn't contain character '{chr}'")

scnd = input("Insert second word: ")
if frst<scnd:
    print(f"The first word '{frst}' is before the second word '{scnd}' alphabetically.")
elif scnd<frst:
    print(f"The second word '{scnd}' is before the first word '{frst}' alphabetically.")
else:
    print(f"Both inserted words are the same alphabetically, '{frst}'")
print("Program ending.")