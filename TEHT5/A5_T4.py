def askDimension(PPrompt: str) -> float:
   Feed = input(f"Insert {PPrompt}: ")
   return float(Feed)


def calculateArea(PWidth: float, PHeight: float) -> float:
   Area = PWidth  * PHeight
   return Area


def main():
    print("Program starting.")  
    Width = askDimension("width")
    Height = askDimension("height")
    Area = calculateArea(Width, Height)
    print(f"Area is {Area}²")
    print("Program ending.")

main()