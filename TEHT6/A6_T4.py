print("""Program starting.
This program analyses a list of names from a file.""")

source = input ('Insert filename to read: ')
print(f'''Reading names from "{source}".
Analysing names...
Analysis complete!''')

names = []

info=open(source, "r", encoding="utf-8")
for line in info:
    line = line.strip()
    if line:
     parts = line.split(';')
     for name in parts:
        name = name.strip()
        if name:
            names.append(name)
info.close()

count=len(names)
lengths = [len(name) for name in names]
shortest = min(lengths)
longest = max(lengths)
average = sum(lengths) / count

print(f'''#### REPORT BEGIN ####
Name count - {count}
Shortest name - {shortest} chars
Longest name - {longest} chars
Average name - {average:.2f} chars
#### REPORT END ####
Program ending.''')