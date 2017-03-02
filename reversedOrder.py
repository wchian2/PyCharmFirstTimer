# This script contains a homemade function reversing the order of a list

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(alphabet)

# Printing number of letters of alphabet to ensure I didn't leave out a letter :P
print(len(alphabet))

# Here we go... unrolls sleeves
def reversedOrder(list):
    newlist = []

    while len(list) != 0:
        newlist.append(list[-1])
        list.pop(-1)
    print("The reversed order is: " + str(newlist))

# Moment of truth...
print "-" * 10
reversedOrder(alphabet)