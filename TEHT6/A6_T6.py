LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rot13_char(ch: str) -> str:
    if ch in LOWER_ALPHABETS:
        idx = LOWER_ALPHABETS.index(ch)
        return LOWER_ALPHABETS[(idx + 13) % 26]
    elif ch in UPPER_ALPHABETS:
        idx = UPPER_ALPHABETS.index(ch)
        return UPPER_ALPHABETS[(idx + 13) % 26]
    else:
        return ch


def rot13_line(line: str) -> str:
    result = ""
    for ch in line:
        result += rot13_char(ch)
    return result


print("Program starting.\n")
print("Collecting plain text rows for ciphering.")

plain_rows = []

while True:
    row = input("Insert row(empty stops): ")
    if row == "":
        break
    plain_rows.append(row)


ciphered_rows = [rot13_line(r) for r in plain_rows]

print("\n#### Ciphered text ####")
for r in ciphered_rows:
    print(r)

print("\n#### Ciphered text ####")

choice = input("Insert filename to save (empty = skip): ").strip()

if choice != "":
    with open(choice, "w", encoding="utf-8") as file:
        for r in ciphered_rows:
            file.write(r + "\n")
    print("Ciphered text saved!")

print("Program ending.")
