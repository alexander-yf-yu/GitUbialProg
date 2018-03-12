'''
functionspractice.py
Alex Yu
October 25th 2017
Version 1.0
Shows how to use functions
'''

import math

def min3(a, b, c):
    """Takes three numbers and returns the smallest value."""

    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    elif c <= a and c <= b:
        return c
    else:
        return ("Invalid Input.")

def box(y, x):
    """Prints a box of *s y high and x wide"""

    star = "*"

    for i in range(y):
        print(star * x)

def find(my_list, key):
    """Takes a list of nums and a key and returns all the locations where that key exists."""
    # j = 0
    #
    # for i in my_list:
    #
    #     if i == key:
    #         print("Found " + str(key) + " in position " + str(j)
    #     else:
    #         j += 1


def main():
    print(min3(4, 7, 5))                # print 4
    print(min3(4, 5, 5))                # print 4
    print(min3(4, 4, 4))                # print 4
    print(min3(-2, -6, -100))                # print -100
    print(min3("Z", "B", "A"))              # print "A"
    box(7,5)              # Print a box 7 high, 5 across
    print                   # Blank line
    box(3,2)                # Print a box 3 high, 2 across
    print                # Blank line
    box(3,10)              # Print a box 3 high, 10 across

    my_list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86,
    11, 17, 17]


    find(my_list, 12)
    # "Found 12 in position 11."
    # "Found 12 in position 13."
    find(my_list, 91)
    # "Found 91 in position 5."
    find(my_list, 80)
    # nothing


if __name__ == "__main__":
    main()
    # nums = []
    # nums[0].append = raw_input("Choose a number! ")
    # nums[1].append = raw_input("Choose another number! ")
    # nums[2].append = raw_input("Choose the last number! ")

    # print(min3(nums))


    # num1 = raw_input("Choose a number! ")
    # num2 = raw_input("Choose another number! ")
    # num3 = raw_input("Choose the last number! ")
    #
    # print(min3(num1, num2, num3))








# def surface_a_of_sphere(radius):
#     sa = 4 * math.pi * radius ** 2
#     text = ("The surface area is " + str(sa) + " units.")
#     return text
#
#
# output = abs(float(raw_input("What is your radius?  ")))
#
# print(surface_a_of_sphere(output))
