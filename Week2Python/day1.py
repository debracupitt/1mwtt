# Functions, parameters
# def moo(n):
#     print('moo' * n)
#     return 'moo' * n

# moo(0)
# moo(1)
# moo(2)

# for i in range(3):
#     moo(i)

# Testing


# Import file
# filename = "alice_in_wonderland.txt"
# file = open(filename, "r")

# for line in file:
# 	print(line)

# raw = file.read()
# print('From zero to sixty-five: ' + raw[:65])

# print('AGAIN: ' + raw[0:65])

# print('The length of Alice in Wonderland in this text file is: ' + str(len(raw)))

# 163817

# Calculate a table for each letter in the alphabt from a-z, and cound how many times wach letter appears in Alice in Wonderland (the fancy word for counting stuff is 'frequency distribution')

# a: 59667
# b: 86876
# ...
# z: 576


# Recursion

# def ask_recursively(question):
# 	print(question)
# 	reply = input('> ').lower()
# 	if reply == 'yes':
# 		return True
# 	if reply == 'no':
# 		return False
# 	else:
# 		print('Please answer "yes" or "no".')
# 		ask_recursively(question)

# ask_recursively("Do you wet the bed?")













# coding: utf-8

# ================ DAY 1 HOMEWORK - Calculator ================ #

# hrs_year = 24*365
# print('Hours in a yr: ' + str(hrs_year))
#
# mins_dec = (hrs_year*60)*10
# print('Minutes in a decade: ' + str(mins_dec))
#
# secs_dec = mins_dec*60
# my_age_secs = (secs_dec)*2.73
# print("I am " + str(my_age_secs) + " seconds old.")
#
# # Andreea Visanoiu​/s age is 48,618,000 seconds old (not counting leap years) at 11:30 am Jul 16, 2018. Convert to years
# yrs_dec = 10
# secs_dec = mins_dec*60
#
# andreea_age_secs = 48618000
# andreea_decs = float(andreea_age_secs)/float(secs_dec)
# andreea_age_yrs = andreea_decs*yrs_dec
#
# print("Andrea Visanoiu​ is " + str(andreea_age_yrs) + " years old.")


# ================ DAY 2 HOMEWORK - n/a =============================== #

# ================ DAY 3 HOMEWORK - Inputs and Responses ================ #

# Full name greeting. Write a program that asks for a person’s first name, then middle, and then last. Finally, it should greet the person using their full name.

# first_name = ""
# middle_name = ""
# last_name = ""
# first_name = input("What is your first name?  ")
# middle_name = input("What is your middle name?  ")
# last_name = input("What is your last name?  ")
# print("It's lovely to meet you " + first_name + " " + middle_name + " " + last_name + "!")

--------------------------------------------------------------------------------------------

# Bigger, better favorite number. Write a program that asks for a person’s favorite number. Have your program add 1 to the number, and then suggest the result as a bigger and better favorite number. (Do be tactful about it, though.)

# fav_number = input("What is your favourite number?  ")
# def make_better_number (fav_number):
#     better_number = fav_number + 1
#     return better_number
#
# print("That's a great choice! However, perhaps " + str(make_better_number (fav_number)) + " is a bigger and better favourite number?")



# Angry boss. Write an angry boss program that rudely asks what you want. Whatever you answer, the angry boss should yell it back to you and then fire you. For example, if you type in I want a raise, it should yell back like this:
# WHADDAYA MEAN "I WANT A RAISE"?!? YOU'RE FIRED!!

# def answer_boss():
#     answer = str(input("What do you want? "))
#     if answer == "I want a raise":
#         print('WHADDAYA MEAN "I WANT A RAISE"?!? YOU\'RE FIRED!!')
#     else:
#         print('I SAID,')
#         answer_boss()
#
# answer_boss()


# Table of contents. Here’s something for you to do in order to play around more with center, ljust, and rjust: write a program that will display a table of contents so that it looks like this:
# Table of Contents
# Chapter 1: Getting Started page 1 Chapter 2: Numbers page 9 Chapter 3: Letters page 13
