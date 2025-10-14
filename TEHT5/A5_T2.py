def main():
    print("Program starting.")
    print("\n")
    feed = input("Insert word: ")
    def frameWord(PWord):
        print("*"*(len(PWord)+4))
        print("* "+PWord+" *")
        print("*"*(len(PWord)+4))
        return None
    frameWord(feed)
    print("\n")
    print("\nProgram ending.")
    return None
main()