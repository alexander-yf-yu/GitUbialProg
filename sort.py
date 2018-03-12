# file = open('RandomNumbers.txt')
#
# numbers = []
#
# for line in file:
#     numbers.append(int(line.strip()))
#
# file.close()
#
# print(numbers)
#
# for currentposition in range(len(numbers)):
#         minimumposition = currentposition
#
#         for scanposition in range(currentposition + 1, len(numbers)):
#             if numbers[scanposition] < numbers[minimumposition]:
#                 minimumposition = scanposition
#
#         temp = numbers[minimumposition]
#         numbers[minimumposition] = numbers[currentposition]
#         numbers[currentposition] = temp
#
# print(numbers)
# # for nums in numbers:
# #     print(nums)
#
# print("We have " + str(len(numbers)) + " numbers in our file.")
#
# # for current position in range(len(numbers)):
# #     minimumposition


# FIB

sequence = []
init_1 = 0
init_2 = 1

sequence.append(init_1)
sequence.append(init_2)

ind = 1
# currentpos = sequence[ind]





def fib(lim):

    ind = 1

    while ind <= lim:

        nextnum = int(sequence[ind - 1] + sequence[ind])
        sequence.append(nextnum)
        print(sequence[ind + 1])

        ind += 1

# TODO:

# def euler(max):
#
#
#
#     while
