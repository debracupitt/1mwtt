# Functions, parameters
def moo(n):
    print('moo' * n)
    return 'moo' * n

moo(0)
moo(1)
moo(2)

for i in range(3):
     moo(i)

# Testing
# See test_day1.py


# Import file
# =============================================================================
# filename = "alice_in_wonderland.txt"
# file = open(filename, "r")
#
# for line in file:
#     print(line)
#
# raw = file.read()
# print('From zero to sixty-five: ' + raw[:65])
#
# print('AGAIN: ' + raw[0:65])
#
# print('The length of Alice in Wonderland in this text file is: ' + str(len(raw)))
# =============================================================================

#163817

# Calculate a table for each letter in the alphabt from a-z, and cound how many times wach letter appears in Alice in Wonderland (the fancy word for counting stuff is 'frequency distribution')

a: 59667
b: 86876
...
z: 576


# Recursion

# =============================================================================
# def ask_recursively(question):
#     print(question)
#     reply = input('> ').lower()
#     if reply == 'yes':
#         return True
#     if reply == 'no':
#         return False
#     else:
#         print('Please answer "yes" or "no".')
#         ask_recursively(question)
#
# ask_recursively("Do you wet the bed?")
# =============================================================================
