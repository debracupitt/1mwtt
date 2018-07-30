# -*- coding: utf-8 -*-

filename = "alice_in_wonderland.txt"
# the open() method opens files and requires two arguments, the file name and whether you want to "r" (read) or "w" (write) the file.
file = open(filename, "r")

# for line in file:
#     print(line)


raw = file.read()
# print('From zero to sixty-five: ' + raw[:65])
#
# print('AGAIN: ' + raw[0:65])
#
# print('The length of Alice in Wonderland in this text file is: ' + str(len(raw)))

# create a list with every alphabet letter and a count of 0 to start with.

def alphabet_setup():
    alphabet_list = []
    for i in range(97,97+26):
        alphabet_list.append([chr(i), 0])
    return alphabet_list

alphabet_count = alphabet_setup()
# print(alphabet_count[0][0])

# convert the string to lower case.
alice = raw[0:65]
lc_alice = raw.lower()
# print(alice)
# print(lc_alice)

# # iterate through entire string and see if each character matches a letter in the alphabet.
def check_chr(book, list):
    letter_count = list
    n = 0
    while n < len(book):
        for b in book:
            # print(b)
            for l in letter_count:
                # print(a[0] + b)
                if l[0] == b:
                    l[1] = int(l[1]) + 1
                    n = n + 1
                    # print(alphabet_count)
    print(letter_count)
    return letter_count

# check_chr(lc_alice, alphabet_count)
check_chr(lc_alice, alphabet_count)

# if there's a match, add a count to that letter in it's list form.
