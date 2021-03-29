# When running this code there may be an issue in the replit preview, this is only an issue in replt.

# When running take this with caution and if it doesn't work attempt to run it in a different program.

# It should work there.
import math

playerChoice = ""
diameter = 0
area = 0
circumference = 0

print(
    "Welcome to my calculator, here you can can calculate the circumference or area of a circle."
)
playerChoice = input(
    "Would you like to calculate the area or the circumference of the circle: "
)

if playerChoice.lower() == "area":
    playerChoice = int(input("Please input your diameter: "))
    diameter = playerChoice
    area = math.pi * ((diameter / 2) ** 2)
    print(area)
elif playerChoice.lower() == "circumference":
    playerChoice = int(input("Please input your diameter: "))
    diameter = playerChoice
    circumference = 2 * math.pi * (diameter / 2)
    print(circumference)
else:
    print("Error this is not a option...")
