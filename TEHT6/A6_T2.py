print ("Program starting.")

name=input("Insert first name: ")
surname=input("Insert last name: ")
filename=input("Insert filename: ")

file = open(filename,"w")
file.write(f"{name}\n{surname}\n\n")
file.close()

print("Program ending.")
