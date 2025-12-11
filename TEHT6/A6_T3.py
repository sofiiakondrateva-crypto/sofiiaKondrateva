print ('''Program starting.
    This program can copy a file.''')
source= input("Insert source filename: ")   
destination= input("Insert destination filename: ")

readfile=open(source,"r", encoding="utf-8")
content = readfile.read()
readfile.close()

file = open (destination,"w", encoding="utf-8")
file.write(content)
file.close()

print(f'''Reading file 'A6_T3_D1.txt' content.
    File content ready in memory.
      Writing content into file '{destination}'.
    Copying operation complete.
    Program ending.''')
