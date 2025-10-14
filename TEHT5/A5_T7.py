DELIMITER = ','

def collectWords():
    words = []
    while True:
        feed=input("Insert word(empty stops): ")
        if feed == "":
            break
        words.append(feed)  
    return DELIMITER.join(words)
        

def analyseWords(result):
    if result == "":
        list = []
    else:
        list = result.split(DELIMITER)

    allwords = len(list)
    char = sum (len(word) for word in list)

    if allwords > 0:
        avg = char / allwords
    else:
        avg = 0
    
    print(f"- {allwords} Words")
    print(f"- {char} Characters")
    print(f"- {avg:.2f} Average word length")
    return None


def main():
    print("Program starting.")
    words = collectWords()
    analyseWords(words)
    print("Program ending.")

main()