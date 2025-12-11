SEPARATOR = ";"

def readValues(filename) -> str:
    values = ""
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            number = line.strip()
            if i == len(lines) - 1:
                values += number       
            else:
                values += number + SEPARATOR
    return values


def analyseNumbers(valueString: str) -> str:
    numbers = [int(n) for n in valueString.split(SEPARATOR)]

    count = len(numbers)
    total = sum(numbers)
    greatest = max(numbers)
    average = total / count

    result = f"{count}{SEPARATOR}{total}{SEPARATOR}{greatest}{SEPARATOR}{average:.2f}"
    return result


def displayResults(filename: str, resultString: str):
    print("#### Number analysis - START ####")
    print(f'File "{filename}" results:')
    print("Count;Sum;Greatest;Average")
    print(resultString)
    print("\n#### Number analysis - END ####")



print("Program starting.")
filename = input("Insert filename: ")

values = readValues(filename)
results = analyseNumbers(values)
displayResults(filename, results)

print("Program ending.")
