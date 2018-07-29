# coding: utf-8

# ================ DAY 1 HOMEWORK - Calculator ================ #

hrs_year = 24*365
print('Hours in a yr: ' + str(hrs_year))

mins_dec = (hrs_year*60)*10
print('Minutes in a decade: ' + str(mins_dec))

secs_dec = mins_dec*60
my_age_secs = (secs_dec)*2.73
print("I am " + str(my_age_secs) + " seconds old.")

# Andreea Visanoiu​/s age is 48,618,000 seconds old (not counting leap years) at 11:30 am Jul 16, 2018. Convert to years

yrs_dec = 10
secs_dec = mins_dec*60

andreea_age_secs = 48618000
andreea_decs = float(andreea_age_secs)/float(secs_dec)
andreea_age_yrs = andreea_decs*yrs_dec

print("Andrea Visanoiu​ is " + str(andreea_age_yrs) + " years old.")


# ================ DAY 2 HOMEWORK - n/a =============================== #

# ================ DAY 3 HOMEWORK - Inputs and Responses ================ #

# Full name greeting. Write a program that asks for a person’s first name, then middle, and then last. Finally, it should greet the person using their full name.

first_name = ""
middle_name = ""
last_name = ""
first_name = input("What is your first name?  ")
middle_name = input("What is your middle name?  ")
last_name = input("What is your last name?  ")
print("It's lovely to meet you " + first_name + " " + middle_name + " " + last_name + "!")

# ----------------------------------------------------------------------------------------

# Bigger, better favorite number. Write a program that asks for a person’s favorite number. Have your program add 1 to the number, and then suggest the result as a bigger and better favorite number. (Do be tactful about it, though.)

fav_number = input("What is your favourite number?  ")
def make_better_number (fav_number):
    better_number = fav_number + 1
    return better_number

print("That's a great choice! However, perhaps " + str(make_better_number (fav_number)) + " is a bigger and better favourite number?")

# ----------------------------------------------------------------------------------------------

# Angry boss. Write an angry boss program that rudely asks what you want. Whatever you answer, the angry boss should yell it back to you and then fire you. For example, if you type in I want a raise, it should yell back like this:
# WHADDAYA MEAN "I WANT A RAISE"?!? YOU'RE FIRED!!

def answer_boss():
    answer = str(input("What do you want? "))
    if answer == "I want a raise":
        print('WHADDAYA MEAN "I WANT A RAISE"?!? YOU\'RE FIRED!!')
    else:
        print('I SAID,')
        answer_boss()

answer_boss()

# ----------------------------------------------------------------------------------------------

# Table of contents. Here’s something for you to do in order to play around more with center, ljust, and rjust: write a program that will display a table of contents so that it looks like this:
# Table of Contents
# Chapter 1: Getting Started page 1 Chapter 2: Numbers page 9 Chapter 3: Letters page 13

scrum_contents = [
["Chapter 1: The Way the World Works Is Broken", "p. 1"],
["Chapter 2 The Origins of Scrum", "p. 23"],
["Chapter 3 Teams", "p. 41"],
["Chapter 4 Time", "p. 71"],
["Chapter 5 Waste Is a Crime", "p. 85"],
["Chapter 6 Plan Reality, Not Fantasy", "p. 111"],
["Chapter 7 Happiness", "p. 145"],
["Chapter 8 Priorities", "p. 171"],
["Chapter 9 Change the World", "p. 203"],
["Acknowledgments", "p. 232"],
["Appendix: Implementing Scrum-How to Begin", "p. 234"],
["Notes", "p. 239"],
["Index", "p. 242"]
]

def print_contents(contents):
    print("Table of Contents")
    i = 0
    for c in contents:
        print(contents[i][0].ljust(60) + contents[i][1])
        i = i + 1

print_contents(scrum_contents)

# ================ DAY 4 HOMEWORK - Loops & Lists ================ #

# “99 Bottles of Beer on the Wall.” Write a program that prints out the lyrics to that beloved classic, “99 Bottles of Beer on the Wall.”

for b in range (99,1,-1):
    print(str(b) + " bottles of beer on the wall, " + str(b) + " bottles of beer. Take one down and pass it around, " + str(b) + " bottles of beer on the wall.")

print(str(1) + " bottle of beer on the wall, " + str(1) + " bottle of beer. Take one down and pass it around, " + str(1) + " bottle of beer on the wall.")

print("No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.")


# ----------------------------------------------------------------------------------------------

# Deaf grandma. Whatever you say to Grandma (whatever you type in), she should respond with this: HUH?! SPEAK UP, GIRL! Unless you shout it (type in all capitals). If you shout, she can hear you (or at least she thinks so) and yells back:

import random

year = str(random.randrange(1930, 1950))

def grandma_convo(num):
    words_to_grandma = input("What would you like to say to Grandma?")
    count = num
    if words_to_grandma == "BYE" and count == 2:
        print("Grandma says: OK BYE DEAR!")
    elif words_to_grandma == "BYE":
        print("Grandma says: HOW\'S THE WEATHER?")
        count = count + 1
        grandma_convo(count)
    elif words_to_grandma.isupper():
        print("Grandma says: 'NO, NOT SINCE " + year + "!'")
        grandma_convo(0)
    else:
        print("Grandma says: 'HUH?! SPEAK UP, GIRL!'")
        grandma_convo(0)

grandma_convo(0)


# ----------------------------------------------------------------------------------------------

# Leap years. Write a program that asks for a starting year and an ending year and then puts all the leap years between them (and including them, if they are also leap years). Leap years are years divisible by 4 (like 1984 and 2004). However, years divisible by 100 are not leap years (such as 1800 and 1900) unless they are also divisible by 400 (such as 1600 and 2000, which were in fact leap years). What a mess!

def leap_year_calc(start_yr, end_yr):
    for y in range(start_yr, end_yr):
        if y % 100 == 0 and y % 400 == 0:
            print(y)
        if y % 4 == 0 and y % 100 != 0:
            print(y)

starting_point = input("What year would you like to start counting from?  ")

ending_point = input("What year would you like to stop counting?  ")

print("The leap years between the years " + str(starting_point) + " and " + str(ending_point) + " include:")
leap_year_calc(starting_point, ending_point)


# ----------------------------------------------------------------------------------------------

# Find something today in your life, that is a calculation. Go for a walk, look around the park, try to count something. Anything! And write a program about it. estimate your books by bookshelf

def books_bookshelf(bookshelves_num):
    books = bookshelves_num * 200
    return books

bookshelves = input("How many bookshelves do you have?  ")

print("Based on this number, I predict you have approximately " + str(books_bookshelf(bookshelves)) + " books!")


# ----------------------------------------------------------------------------------------------

# Building and sorting an array. Write the program that asks us to type as many words as we want (one word per line, continuing until we just press Enter on an empty line) and then repeats the words back to us in alphabetical order. Make sure to test your program thoroughly; for example, does hitting Enter on an empty line always exit your program? Even on the first line? And the second?

def print_words(new_words_list):
    words_list = new_words_list
    word_input = str(input("Please enter one word to add to your list, or press Enter to finalise your list:  "))
    if word_input == "":
        print("Here is your sorted word list:  ")
        print(sorted(words_list))
    else:
        words_list.append(word_input)
        print_words(words_list)

print_words([])


# ----------------------------------------------------------------------------------------------

# Write a function that prints out "moo" n times.

def print_moo(n):
    for i in range(0, n):
        print("moo")

print_moo(3)


# ----------------------------------------------------------------------------------------------

# Old-school Roman numerals. In the early days of Roman numerals, the Romans didn’t bother with any of this new-fangled subtraction “IX” nonsense.
# I, II, III, IIII, V, VI, VII, VIII, VIIII, X, XI, XII, XIII, XIIII, XV ...
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000

def old_roman_numeral_converter(num):
    number = num
    remaindar = 0
    old_roman_numeral = ""

    old_roman_numeral = old_roman_numeral + "M" * (number / 1000)
    remaindar = number % 1000
    old_roman_numeral = old_roman_numeral + "D" * (remaindar / 500)
    remaindar = number % 500
    old_roman_numeral = old_roman_numeral + "C" * (remaindar / 100)
    remaindar = number % 100
    old_roman_numeral = old_roman_numeral + "L" * (remaindar / 50)
    remaindar = number % 50
    old_roman_numeral = old_roman_numeral + "X" * (remaindar / 10)
    remaindar = number % 10
    old_roman_numeral = old_roman_numeral + "V" * (remaindar / 5)
    remaindar = number % 5
    old_roman_numeral = old_roman_numeral + "I" * (remaindar / 1)

    print(old_roman_numeral)

old_roman_numeral_converter(3642)
# > MMMDCXXXXII

old_roman_numeral_converter(964)
# > DCCCCLXIIII

old_roman_numeral_converter(999)
# DCCCC LXXXX VIIII

old_roman_numeral_converter(444)
# CCCC XXXX IIII

# New-style Roman numerals so when someone calls roman_numeral 4, it should return 'IV', 90 should be 'XC' etc.
# I, II, III, IV, V, VI, VII, VIII, IX, X, XI, XII, XIII, XIV, XV ...

def new_roman_numeral_converter(num):
    number = num
    remaindar = 0
    new_roman_numeral = ""

    new_roman_numeral = new_roman_numeral + "M" * (number / 1000)
    remaindar = number % 1000
    if remaindar >= 900:
        new_roman_numeral = new_roman_numeral + "CM"
        remaindar = number % 100
    else:
        new_roman_numeral = new_roman_numeral + "D" * (remaindar / 500)
        remaindar = number % 500
    if remaindar >= 400:
        new_roman_numeral = new_roman_numeral + "CD"
        remaindar = number % 100
    else:
        new_roman_numeral = new_roman_numeral + "C" * (remaindar / 100)
        remaindar = number % 100
    if remaindar >= 90:
        new_roman_numeral = new_roman_numeral + "XC"
        remaindar = number % 10
    else:
        new_roman_numeral = new_roman_numeral + "L" * (remaindar / 50)
        remaindar = number % 50
    if remaindar >= 40:
        new_roman_numeral = new_roman_numeral + "XL"
        remaindar = number % 10
    else:
        new_roman_numeral = new_roman_numeral + "X" * (remaindar / 10)
        remaindar = number % 10
    if remaindar == 9:
        new_roman_numeral = new_roman_numeral + "IX"
        remaindar = number % 1
    else:
        new_roman_numeral = new_roman_numeral + "V" * (remaindar / 5)
        remaindar = number % 5
    if remaindar == 4:
        new_roman_numeral = new_roman_numeral + "IV"
    else:
        new_roman_numeral = new_roman_numeral + "I" * (remaindar / 1)

    print(new_roman_numeral)

new_roman_numeral_converter(3642)
# > MMMDCXLII

new_roman_numeral_converter(964)
# > CM LX IV

new_roman_numeral_converter(999)
# CM XC IX

new_roman_numeral_converter(444)
# CD XL IV


#  ================ Week 1 Hackathon Challenge: Continent Counter ================================

import random
M = 'land'
o = 'water'
world = []

def create_world(world_size):
    for w in range(0,world_size):
        row = []
        i = 0
        while i < world_size:
            if random.randrange(2) == 0:
                tile = o
                row.append(tile)
                i = i + 1
            else:
                tile = M
                row.append(tile)
                i = i + 1
        world.append(row)

world_size = input('What size would you like your world to be? Please choose a number between 2 and 15.  ')

def check_size_create(world_size):
    if 0 < world_size < 15:
        create_world(world_size)
    else:
        world_size = input('What size would you like your world to be? Please choose a number between 2 and 15.')
        check_size_create(world_size)

check_size_create(world_size)

def continent_counter(world, x, y):
    #print(str(x) + str(y) + str(a) + str(b))
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

x_coordinate = int(input('What "x" coordinate would you like to land on? You must choose a number between 0 and ' + str(world_size) + ":  "))

def check_x(world_size, x_coordinate):
    if x_coordinate >= 0 and x_coordinate <= world_size:
        return x_coordinate
    else:
        x_coordinate = int(input('What "x" coordinate would you like to land on? You must choose a number between 0 and ' + str(world_size) + ":  "))
        check_x(world_size, x_coordinate)

check_x(world_size, x_coordinate)
a = x_coordinate

y_coordinate = int(input('What "y" coordinate would you like to land on? You must choose a number between 0 and ' + str(world_size) + ":  "))

def check_y(world_size, y_coordinate):
    if y_coordinate >= 0 and y_coordinate <= world_size:
        return y_coordinate
    else:
        y_coordinate = int(input('What "y" coordinate would you like to land on? You must choose a number between 0 and ' + str(world_size) + ":  "))
        check_y(world_size, y_coordinate)

check_y(world_size, y_coordinate)
b = y_coordinate

your_continent = continent_counter(world, a, b)

print(a)
print(b)

print("The size of the continent you landed on at coordinates (" + str(a) + ", " + str(b) + ") is: " + str(your_continent) + " hectares")


# worldtest1 = [
#         [o,M,o],
#         [o,M,M]
#         ]
#
# worldtest2 = [
#          [o,o,o,o,o,o,o,o,o,o,o],
#          [o,o,o,o,M,M,o,o,o,o,o],
#          [o,o,o,o,o,o,o,o,M,M,M],
#          [o,o,o,M,o,o,o,o,o,M,o],
#          [o,o,o,M,o,M,M,o,o,o,o],
#          [o,o,o,o,M,M,M,M,o,o,o],
#          [o,o,o,M,M,M,M,M,M,M,o],
#          [o,o,o,M,M,o,M,M,M,o,o],
#          [o,o,o,o,o,o,M,M,o,o,o],
#          [o,M,o,o,o,M,o,o,o,o,o],
#          [o,o,o,o,o,o,o,o,o,o,o]
#         ]
# worldtest3 = [
#             [o,o,o,o,o,o,o,o,o,o,o],
#             [o,o,o,M,M,o,o,M,o,o,o],
#             [o,M,o,o,o,o,o,M,M,M,o],
#             [o,o,o,o,o,o,M,M,o,o,o],
#             [o,M,M,M,o,o,o,M,o,o,o],
#             [M,M,M,M,M,M,o,o,o,o,o],
#             [o,M,o,M,o,o,o,M,o,M,o],
#             [o,o,o,o,o,M,M,M,o,o,o],
#             [o,o,o,M,o,o,o,o,o,o,o],
#             [M,o,o,o,M,o,M,o,o,o,o],
#             [o,o,o,o,M,M,M,M,o,o,o]
#         ]

# print(continent_counter(worldtest1, 1, 0))  # 3
# print(continent_counter(worldtest2, 4, 1))  # 23
# print(continent_counter(worldtest3, 0, 6))  # 11
