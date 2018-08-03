# -*- coding: utf-8 -*-

# Redo the frequency distribution of alice_in_wonderland.txt and save your result in a dictionary.

filename = "alice_in_wonderland.txt"
file = open(filename, "r")
raw = file.read()
lc_alice = raw.lower()

# Variables for testing
alice_test = raw[0:30]
lc_alice_test = alice_test.lower()

# Creates a list with every alphabet letter and a count of 0 to start with.
def alphabet_setup():
    alphabet_dict = {}
    for i in range(97,97+26):
        alphabet_dict[chr(i)] = 0
    print(alphabet_dict)
    return alphabet_dict

alphabet_count = alphabet_setup()
alphabet_count_test = alphabet_setup()

# Iterates through entire string and see if each character matches a letter in the alphabet. If there's a match, add a count to that letter in it's list form.
def check_chr(book, list):
    letter_count = list
    for b in book:
        if bool(letter_count[b]):
            letter_count[b] = letter_count[b] + 1
    print(letter_count)
    return letter_count

check_chr(lc_alice, alphabet_count)
