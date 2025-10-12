print("Program starting.")

words = 0
characters = 0

while True:
    word = input("Insert word (empty stops): ")
    if word == "":
        break
    words += 1 
    characters = characters + len(word)

print("\nYou inserted:")
print(f"""
- {words} words 
- {characters} characters""")

print("\nProgram ending.")