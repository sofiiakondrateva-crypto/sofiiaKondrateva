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
else:
    if num1 < num3:
        print("Number 3 is the largest.")
    else:
        print("Number 1 is the largest.")



correct_number = 23
while True:
 guess = int(input("Enter an integer: "))
 if guess == correct_number:
        print("You guessed correctly!")
        print("Game ends here")
        break
 elif guess < correct_number:
        print("The number is higher than your guess")
 else:
        print("The number is lower than your guess")
print("This prints at the end, after the while loop.")


for i in range(1, 5):
        print(i)
print("Loop has ended.") #range(1, 5) generates numbers 1 to 4

for i in range(1, 11):
        if i == 7:
                print("Lucky number", i, "found!")
                break
        print("Checking number", i)
print("Done!")


while True:
        text = input("Enter text: ")
        if text == "stop":
                break
        if len(text) < 6:
                continue
print("Input is longer than 5 characters")

list(range(10)) # [0, 1, 2, ..., 9]
list(range(5, 10)) # [5, 6, 7, 8, 9]
list(range(0, 10, 3)) # [0, 3, 6, 9] range(start, stop, step)
list(range(-10, -100, -30)) # [-10, -40, -70]

for n in range(2, 10):
        for x in range(2, n):
                if n % x == 0:
                        print(n, "equals", x, "*", int(n/x))
                        break
        else:
                print(n, "is a prime number")


firstloop = []
" ".join(firstloop)  # пробел между числами → '3 4 5'
"".join(firstloop)   # без пробела → '345'
"-".join(firstloop)  # через дефис → '3-4-5'
loop = [str(feed)]  # начинаем список сразу с исходного числа

#git pull --rebase origin main   git push origin main