def main():
    print("Program starting.")
    count = 0
    choice = None

    while choice != 0:
        showOptions()
        choice = askChoice()
        if choice == 1:
            print(f"Current count - {count}")
            
        elif choice == 2:
            count = count + 1
            print("Count increased!")
            
        elif choice == 3:
            count = 0
            print("Cleared count!")
            
        elif choice == 0:
            print("Exiting program.")
        else:
            print("Unknown option")
            
    print("\nProgram ending.")
    return None
    


def showOptions ():
    print("""Options:
        1 - Show count
        2 - Increase count
        3 - Reset count
        0 - Exit""")
    return None

def askChoice ():
    feed = (input("Your choice: "))
    if feed.isnumeric():
        return int(feed)
    else:
        print("Unknown option!")
        return -1
    
main()

    



