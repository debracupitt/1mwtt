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

# ================================================================================================================ #

# ================ DAY 3 HOMEWORK - Inputs & Responses ================ #

# ------ Strings ------
# print("You're swell!")
# print('You\'re swell!') # Escape the character
# print('You are swell! \\')
# print('You are \swell!')
# print('You are \\swell!')

# ------ Indexes ------
# name = 'Debra Cupitt'
# # print(name[0])
# print(name[-3]) # >> 'i' will print

# ------ Lists ------
## It is convention to use the first letter of the name of the list ('s' in 'students') as the name of the iterator in python
# students = ["Deb", "Timothy", "Lucky"]
# # for s in students:
# #     if len(s) > 6:
# #         print(s + " has the longest name.")
# #     elif len(s) > 3:
# #         print(s + " is stuck in the middle.")
# #     else:
# #         print(s + " is a super coder!")
#
# # ------ List Comprehension ------
# ## usernames = [dosomething(element) for everyelement in list]
# def log(s):
#     print(s + "help")
# usernames = [log(s) for s in students ]
# ## >>> returns:
# ## Debhelp
# ## Timothyhelp
# ## Luckyhelp
# names = [s+'123' for s in students]
# print(names)
# ## >>> returns:
## ['Deb123', 'Timothy123', 'Lucky123']

# ------ Length ------
# print(len(name))
# length = len(name)
#
# --------  For loop "for i in range('starting point', 'ending point', 'interval') --------
# for i in range(0,12):
#     print(name[i])
#
# for i in range(0,length):
#     print(name[i])
#
# for i in range(0,len(name)):
#     print(name[i])
#
# for x in range(0, 10, 2):
#     print(x)

# --------  if statement --------
# result = ""
#
# for i in range(0,length):
#     if i % 2 == 0:
#         print(name[i])
#         result = result + name[i]
#
# print(result)

# --------  string and integer methods --------
# var1 = 2
# var2 = '5'
#
# print(var2 + str(var1))
# print(int(var2) + var1)

# --------  float method --------

# class float([x])
# Return a floating point number constructed from a number or string x.

# If the argument is a string, it should contain a decimal number, optionally preceded by a sign, and optionally embedded in whitespace. The optional sign may be '+' or '-'; a '+' sign has no effect on the value produced. The argument may also be a string representing a NaN (not-a-number), or a positive or negative infinity. More precisely, the input must conform to the following grammar after leading and trailing whitespace characters are removed

# For a general Python object x, float(x) delegates to x.__float__().

# If no argument is given, 0.0 is returned.

# float('15')
# # >>> 15.0
# float('99.999')
# # >>> 99.999
# float('1e-003')
# # >>> 0.001
# float('+1E6')
# # >>> 1000000.0
# float('-Infinity')
# # >>> -inf
# # float('Your momma did.')
# # >>> ValueError: could not convert string to float: Your momma did.
# float(1.2)


# --------  input method --------
# pet = input('What is your pet\'s name?')
# print(pet)

# --------  if ... else --------
# a = 3
# b = 7
# if a > b:
#     print("You win!")
# else:
#     print("You lose!")
#
# c = 3
# d = 7
# if a == b:
#     print("Equal!")
# else:
#     print("Not Equal!")

# --------  while loops --------
text = ""
while text != "bye":
    text = input("say something please")
    if text == "bye":
        print("goodbye to you")
        break

# -- OR --
#
# while text != "bye":
#     text = input("Say something please")
#     if text == "bye":
#         print("Goodbye to you!")
#         break
#     print("You said : " + text)


# i = 1
# while i <= 11:
#     print(i)
#     i = i + 1
#
# j = 0
# while j < 5:
#     print(j)
#     if j == 3:
#         break
#     j += 1
