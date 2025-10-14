def main():
    print("Program starting.")
    name = askname()
    greetuser(name)
    print("Program ending.")
    return None

def askname():
    name = input("Insert name: ")
    return name

def greetuser(Pname):
    print(f"Hello {Pname}!")
    return None

main()