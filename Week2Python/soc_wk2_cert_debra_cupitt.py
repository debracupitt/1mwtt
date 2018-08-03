# -*- coding: utf-8 -*-

# ================ DAY 1 HOMEWORK - Alice Alphabet ================ #

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

# Python the Hard Way exercise - printing strings

my_name = 'Deb Cupitt'
my_age = 27
my_height = 153
my_weight = 54
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Brown'

print("Let's talk about %s." % my_name)
print("He's %d inches tall." % my_height)
print("He's %d pounds heavy." % my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee." % my_teeth)
print("If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight))


# ================ DAY 2 HOMEWORK ====================== #
# Make a function that prints A-Z & a-z

print(chr(65))
# > 'A'
def print_alphabet():
    for i in range(65,65+26):
        print(i, " stands for ", chr(i))
    for i in range(97,97+26):
        print(i, " stands for ", chr(i))

print_alphabet()

# -----------------------------------------------------------------------------
# Make a function that asks the user for a message, and turns it into a list of numbers (a cypher)

secret_message = input("What is the secret message you would like to send?")
secret_number = int(input("What would you like your secret number to be?"))

def cypher(secret_message, secret_number):
    coded_message = []
    for s in secret_message:
        character = ord(s) + secret_number
        coded_message.append(character)
    print("Your secret coded message: " + str(coded_message))
    return coded_message

coded_msg = cypher(secret_message, secret_number)

def decode(coded_message):
    decoded_characters = []
    for c in coded_message:
        character = chr(c - secret_number)
        decoded_characters.append(character)
    decoded_message = "".join(decoded_characters)
    print("Your decoded message: " + decoded_message)
    return decoded_message

decode(coded_msg)

# -----------------------------------------------------------------------------

# Write a function that prints out all elements of the above board, starting from the first element of the first line, till the end. Each line should be read from beginning to end.

M = 'land'
o = 'water'
world = [
            [o,o,o,o,o,o,o,o,o,o,o],
            [o,o,o,M,M,o,o,M,o,o,o],
            [o,M,o,o,o,o,o,M,M,M,o],
            [o,o,o,o,o,o,M,M,o,o,o],
            [o,M,M,M,o,o,o,M,o,o,o],
            [M,M,M,M,M,M,o,o,o,o,o],
            [o,M,o,M,o,o,o,M,o,M,o],
            [o,o,o,o,o,M,M,M,o,o,o],
            [o,o,o,M,o,o,o,o,o,o,o],
            [M,o,o,o,M,o,M,o,o,o,o],
            [o,o,o,o,M,M,M,M,o,o,o]
        ]

world2 = [
        [o,M,o],
        [o,M,M]
        ]

def print_board(board):
    board_words = []
    b = 0
    for b in range(0,len(board)):
        r = 0
        for r in range(0,len(board[b])):
            print(board[b][r])
            board_words.append(board[b][r])
            r = r + 1
        b = b + 1
    print("Normal board:  " + str(board_words))
    return board_words

print("Normal board: ")
print_board(world)

# -----------------------------------------------------------------------------

# Now write a function that prints out all elements in reverse.

def print_board_reverse(board):
    board_rev = board[::-1]
    new_board = []
    b = 0
    n = 0
    # creates new reversed board
    for b in range(0,len(board_rev)):
        board_rev[b] = board_rev[b][::-1]
        new_board.append(board_rev[b])
        b = b + 1
    # prints new reversed board
    for n in range(0,len(new_board)):
        i = 0
        for i in range(0,len(new_board[n])):
            print(new_board[n][i])
            i = i + 1
        n = n + 1
    print("Board reversed:  " + str(new_board))
    return new_board

print("Reversed board: ")
print_board_reverse(world)

# -----------------------------------------------------------------------------

# There is one small bug in the continent counter above. Can you find it and fix it? (Hint: change the world so that the continent borders the edge). Write a function that generates an n x n sized board with either land or water chosen randomly. Run your continent counter for a 20 x 20 board.... got to a 800 x 800 size board. The function only took about a second to run!

import random
M = 'land'
o = 'water'

def create_wld(wld_sz):
    world = []
    for w in range(0,wld_sz):
        row = []
        i = 0
        while i < wld_sz:
            if random.randrange(2) == 0:
                tile = o
                row.append(tile)
                i = i + 1
            else:
                tile = M
                row.append(tile)
                i = i + 1
        world.append(row)
    print(world)
    return world

world_size_input = int(input('What size would you like your world to be? Please choose a number between 2 and 800.  '))

def check_sz(wld_sz_input):
    while wld_sz_input < 0 or wld_sz_input > 800:
        wld_sz_input = int(input('What size would you like your world to be? Please choose a number between 2 and 800. '))
    return wld_sz_input

wld_sz_fnl = check_sz(world_size_input)
civIII_world = create_wld(wld_sz_fnl)

x_coordinate = int(input('What "x" coordinate would you like to land on? You must choose a number between 0 and ' + str(wld_sz_fnl) + ":  "))
print(x_coordinate)

def check_x(wld_sz, x):
    while x < 0 or x > wld_sz:
        x = int(input('What "x" coordinate would you like to land on? You must choose a number between 0 and ' + str(wld_sz) + ":  "))
    return x

x_fnl = check_x(wld_sz_fnl, x_coordinate)
print(x_fnl)

y_coordinate = int(input('What "y" coordinate would you like to land on? You must choose a number between 0 and ' + str(wld_sz_fnl) + ":  "))
print(y_coordinate)

def check_y(wld_sz, y):
    while y < 0 or y > wld_sz:
        y = int(input('What "y" coordinate would you like to land on? You must choose a number between 0 and ' + str(wld_sz) + ":  "))
    return y

y_fnl = check_y(wld_sz_fnl, y_coordinate)
print(y_fnl)

def continent_counter(world, x, y):
    if x >= len(world) or x < 0 or y >= len(world) or y < 0:
        return 0
    if world[y][x] != 'land':
        return 0
    size = 1
    world[y][x] = 'counted land'

    # row above
    size = size + continent_counter(world, x-1, y-1)
    size = size + continent_counter(world, x  , y-1)
    size = size + continent_counter(world, x+1, y-1)

    # same row
    size = size + continent_counter(world, x-1, y  )
    size = size + continent_counter(world, x+1, y  )

    # row below
    size = size + continent_counter(world, x-1, y+1)
    size = size + continent_counter(world, x  , y+1)
    size = size + continent_counter(world, x+1, y+1)
    return size

your_continent = continent_counter(civIII_world, x_fnl, y_fnl)

print(your_continent)

print("The size of the continent you landed on at coordinates (" + str(x_fnl) + ", " + str(y_fnl) + ") is: " + str(your_continent) + " hectares")



# ====================== DAY 3 HOMEWORK  ================================ #
# Modify "a" for another name in my_dict. Hint: you will have to create a new key-value pair, copy in the value, and then delete the old one.

my_dict = {
    "a": 35000,
    "b": 8000,
    "z": 450
}

my_dict["d"] = my_dict["a"]
del my_dict["a"]


# -----------------------------------------------------------------------------

# Redo the frequency distribution of alice_in_wonderland.txt and save your result in a dictionary.










# -----------------------------------------------------------------------------

# Create a dictionary with your own personal details, feel free to be creative and funny so for example, you could include key-value pairs with quirky fact, fav quote, pet. Practice adding, modifying, accesing.
