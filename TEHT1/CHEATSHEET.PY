print("Calculate the area of a wall.")
feed = input("enter the width on meters:")
width = int(feed)
feed = input("Enter the height in meters:")
height = int(feed)
print(f"Width {width}m and height {height}m")
product = width * height
print(f"The wall is {product} square meters")


number1 = 47
number2 = 102
sum = number1 + number2
diff = number2 - number1
product = sum * diff
print(f"{number1}+{number2}={sum}")
print(f"{number2}-{number1}={diff}")
print(f"{sum}*{diff}={product}")

sentence = "finding substring"
print(sentence[0]) # first character
print(sentence[-2]) # second last character
print(sentence[2:9]) # characters from index 2 to 8
print(sentence[:9]) # characters from beginning to index 8
print(sentence[-9:-2]) # characters from index -9 to -3
print(sentence[2:9:3]) # characters from index 2 to 8 with step 3
print(sentence[::3]) # characters from beginning to end with step 3
print(sentence[::-1]) # all characters in reverse order
word = "Student"
word[:2] # First two letters, 'St'
word[2:] # All but two first letters, 'udent'
word[0::2] # Every other letter from beginning to the end, 'Suet'
word[::] # The whole word, 'Student'



print(" Fuel consumption calculator")
feed = input("Enter travel distance(kilometers):")
distance = int(feed)
feed = input("Enter fuel usage(liters):")
FuelUsage = int(feed)
consumption = (FuelUsage/distance)*100 # fuel consumption per 100 km пропорция
consumption =int(consumption)
print(f"Fuel consumption is {consumption} l per 100 km”")

print("1, 2, 3, 4, 5, sep=‘-’")
# 1-2-3-4-5 

print("Written text. ", end="")
print("This is printed on the same line.") # Written text. This is printed on the same line.

#\n — новая строка (newline)
#\r — возврат каретки (carriage return)
#\t — табуляция (tab)
#\b — backspace (удаление предыдущего символа)
#\" → double quote (двойная кавычка)
#\' → single quote (одинарная кавычка)
#Чтобы использовать эти символы буквально, без эффекта, ставят двойной обратный слэш \\n

s = 'Deputyassistantreplacementvacationsubstitutejob'
print(len(s)) # 51
print(s[0]) # D
print(s[-1]) # b


word1 = "Co"
word2 = "ral"
print(word1 + word2) # Coral
print((word1 + "-") * 3 + word1 + word2)
# Co-Co-Co-Coral

text = " Hello, World! "
# Convert to uppercase
print(text.upper()) # Output: " HELLO, WORLD! "
# Convert to lowercase
print(text.lower()) # Output: " hello, world! "
# Remove leading and trailing whitespace
print(text.strip()) # Output: "Hello, World!"
# Split into a list of words (default separator is space)
print(text.strip().split()) # Output: ['Hello,', 'World!']
# Replace part of the string
print(text.replace("World", "Python")) # Output: "Hello,Python!"

print("Welcome to the program!")
x = input("Enter the hour (0–23): ")
hour = int(x)
    if hour < 7:
print("Zzz...")
    elif hour <= 8:
print("Time to go to class.")
    elif hour <= 12:
print("Morning classes are over, but you can still study in the afternoon.")
    else:
print("Maybe it's better to take a day off... Zzz...")
print("Thanks for visiting!")

if условие1:
    # выполняется, если условие1 == True
elif условие2:
    # выполняется, если условие1 == False и условие2 == True
elif условие3:
    # проверяется дальше
    ...
else:
    # выполняется, если все условия выше == False

x = 7
print(x > 5 and x < 10)  # True (оба условия выполняются)
print(x < 5 or x > 10)   # False (оба условия False)
print(not(x == 7))       # False (так как x == 7)

a = 5
b = 10

print(a == b)   # False
print(a != b)   # True
print(a < b)    # True
print(b >= 10)  # True


num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
if num1 == num2:
print("Numbers 1 and 2 are the same.")
if (num1 == num2) and (num2 == num3):
print("All numbers are the same.")
# Find the largest number
if num1 < num2:
if num2 < num3:
print("Number 3 is the largest.")
else:
print("Number 2 is the largest.")
    else:if num1 < num3:
print("Number 3 is the largest.")
    else:
print("Number 1 is the largest.")

#git pull --rebase origin main   git push origin main