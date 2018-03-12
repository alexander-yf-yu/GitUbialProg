#import math library
import math

print("Hello World \nh\ne\nl\nl\no\nw\no\nr\nl\nd")


x = "Alex"
y = 25

print(x)
print(y + 50)

print("Calculate the hypotenuse of a right angle triange!")
side_1 = input("Input side a : ")
side_2 = input("Input side b : ")

# add something that detects whether you have inputed a zero
hypotenuse = math.sqrt(float(side_1) ** 2 + float(side_2) ** 2)
perimeter = side_1 + side_2 + hypotenuse

print("The length of the hypotenuse is " + str(hypotenuse) + " units!")
print("The perimeter of the triangle is " + str(perimeter) + " units!")
#area = math.pi * r * r

#print("The area of your circle is" + area + "")

#'''float(math.pi)'''
