'''
quiz_AlexYu.py
Alex Yu
Sept 27th 2017
1.0
My code quizes the user on general trivia
'''

########### Set-up
print("____________________________________________________________________________________________")
print("Welcome to the python quiz of Doom!")
print("You are almost guaranteed to fail this quiz!")

p = 0
c = "Correct!"
w = "Wrong!"

########### Question 1
print("____________________________________________________________________________________________")
print("Question 1:  ")

a1 = raw_input("What is the name of the famous house elf in Harry Potter?   ")

if a1.lower() == "dobby":
    print(c)
    p += 1
else:
    print(w + "His name is Dobby.")

########### Question 2
print("____________________________________________________________________________________________")
print("Question 2:  ")

a2 = raw_input("True or False: Did Pierre Trudeau change the name F.I.R.A into the Canadian Investment Agency? ")


if a2.lower() == "false":
    print(c)
    p += 1
else:
    print(w + " It was PM Brian Mulroney who renamed to the Agency!")

########### Question 3
print("____________________________________________________________________________________________")
print("Question 3:  ")

print("Here is a list of colours!")

print("Marroon")
print("Lavender")
print("Flourescent Green")
print("Orange")

a3 = raw_input("Which one is my favourite?  ")

if a3.lower() == "lavender":
    print(c)
    p += 1
else:
    print(w + "My favourite is lavender.")

########### Question 4
print("____________________________________________________________________________________________")
print("Now for some math:")

print("Question 4:  ")

a4 = raw_input("What is the result of 2 to the power of -1?    ")

if a4.lower() == ("one half") or a4.lower() == ("one over two") or a4.lower() == ("one divided by two") or a4.lower() == ("1 over 2") or a4.lower() == ("half") or a4.lower() == ("0.5") or a4.lower() == ("zero point five"):
    print(c)
    p += 1
else:
    print(w + " The answer is 0.5 or one half")

########### Question 5
print("____________________________________________________________________________________________")
print("Question 5:  ")

print("Here are different types of numbers in math.")

print("Natural Numbers")
print("Rational Numbers")
print("Irrational Numbers")
print("Imaginary Numbers")

a5 = raw_input("The square root of negative one belongs to ___.    ")

if a5.lower() == "imaginary" or a5.lower() == "imaginary numbers":
    print(c)
    p += 1
else:
    print(w + "The answer is imaginary numbers")

########### Finish
print("____________________________________________________________________________________________")
print("You got " + str(float(p) / 5 * 100) + "%.")

if float(p) / 5 > 0.5:
    print("You passed!")
else:
    print("You failed. Better luck next time!")
