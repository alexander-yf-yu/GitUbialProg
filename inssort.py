'''
insertionsort.py
'''

file = open('RandomNumbers.txt')


list = []

for line in file:
    list.append(int(line))

file.close()

print("BEFORE:")
print(list)

def linear_search(key, list):
    for i, value in enumerate(list):
        if value == key:
            return i
        else:
            return -1

    # i = 0
    # for value in list:
    #     if value == key:
    #         return i
    #     else:
    #         i += 1
    #
    #     if i > len(list):
    #         return -1
    #


def insertion_sort(list):

    for key_pos in range(1, len(list)):

        # Storing the value in the current position
        key_val = list[key_pos]

        # Scan from right to left of the list
        scan_position = key_pos - 1

        # Check each elemetn from right to left
        # Move them up if bigger
        # Stop when they're smaller
        while scan_position >= 0 and list[scan_position] > key_val:
            list[scan_position + 1] = list[scan_position]
            scan_position -= 1

            list[scan_position + 1] = key_val


insertion_sort(list)
print(linear_search(60, list))

print("AFTER")
print(list)
