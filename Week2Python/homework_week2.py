# -*- coding: utf-8 -*-

filename = "alice_in_wonderland.txt"
file = open(filename, "r")
raw = file.read()
lc_alice = raw.lower()

# Variables for testing
alice_test = raw[0:30]
lc_alice_test = alice_test.lower()

# Creates a list with every alphabet letter and a count of 0 to start with.
def alphabet_setup():
    alphabet_list = []
    for i in range(97,97+26):
        alphabet_list.append([chr(i), 0])
    return alphabet_list

alphabet_count = alphabet_setup()
alphabet_count_test = alphabet_setup()

# Iterates through entire string and see if each character matches a letter in the alphabet. If there's a match, add a count to that letter in it's list form.
def check_chr(book, list):
    letter_count = list
    for b in book:
        for l in letter_count:
            if l[0] == b:
                l[1] = int(l[1]) + 1
    print(letter_count)
    return letter_count


check_chr(lc_alice, alphabet_count)


# python scrapy library

my_name = 'Zed A. Shaw'
my_age = 35
my_height = 74
my_weight = 180
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print("Let's talk about %s." % my_name)
print("He's %d inches tall." % my_height)
print("He's %d pounds heavy." % my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee." % my_teeth)
print("If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight))
