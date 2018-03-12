'''
customcalculator_AlexYu.py
Alex Yu
Sept 20th 2017
1.0
The program calculates the hypotenuse, perimeter, and area of a right angle triangle after being given sides 1 & 2
It also calculates the sum of arithemetic and geometric series'
Lastly, it is able to convert between degree values and radiand values.
'''

#import math library
import math

# RIGHT ANGLE TRIANGLE
# instructions
print("Calculate the hypotenuse, perimeter, and area of a right angle triangle!")
print("You must input the two non-hypotenuse sides.")

# user input
side_1 = float(input("Input side one: "))
side_2 = float(input("Input side two: "))

# assigning elements to variables
hypotenuse = math.sqrt(float(side_1) ** 2 + float(side_2) ** 2)
perimeter = float(side_1 + side_2 + hypotenuse)
area = float(side_1) * float(side_2) / 2

# catching any invalid input
if side_1 <= 0 and side_2 <= 0:
    print("You must enter non-zero, positive values!")
elif side_1 <= 0 or side_2 <= 0:
    print("Both values must be positive, non-zero numbers!")

# if everything checks out
else:
    print("The length of the hypotenuse is " + str(hypotenuse) + " units!")
    print("The perimeter of the triangle is " + str(perimeter) + " units!")
    print("The area of the triangle is " + str(area) + " units!")

# SEQUENCE AND SERIES

# a-series

print("Find the sum of an arithemetic series!")
as_d = float(input("Type the common difference: "))
as_t1 = float(input("Type the first term: "))
as_n = float(input("Type the number of terms: "))

# Note: you must write out each operation (eg. *)
as_sn = float(as_n / 2 * (2 * as_t1 + (as_n - 1) * as_d))

print("The sum of the a-series is " + str(as_sn) + "!")


# g-series THIS THING IS VERY BROKEN

print("Find the sum of an (infinite) geometric series!")
gs_r = float(input("Type the common ratio: "))
gs_t1 = float(input("Type the first term: "))
gs_n = float(input("Type the number of terms: "))

gs_sn = float(gs_t1 * ((gs_r ** gs_n - 1) - 1) / (gs_r - 1))

print("The sum of the g-series is " + str(gs_sn) + ".")

# Radiand and Degree Converter:
print("Convert from radiands to degrees with this custom calculator!")
print("Dp you want to convert:")

choice = raw_input("From radiand to degree or degree to radiand?    ")

if choice.lower() == "degree to radiand":
    deg = raw_input("Enter your degree value:    ")
    print(str(float(deg) * (math.pi / 180)) + " radiands.")
elif choice.lower() == "radiand to degree":
    rad = raw_input("Enter your radiand value:   ")
    print(str(float(rad) * (180 / math.pi )) + " degrees.")
else:
    print("Invalid Input!")
