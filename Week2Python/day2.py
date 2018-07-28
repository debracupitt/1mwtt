# ========== DAY 2 WEEK 2 =========================
# ------- char() method ---------------------------
# HOMEWORK: Make a function that prints A-Z & a-z
# print(chr(65))
# # > 'A'
# def print_alphabet():
#     for i in range(65,65+26):
#         print(i, " stands for ", chr(i))
#     for i in range(97,97+26):
#         print(i, " stands for ", chr(i))
#
# print_alphabet()

# HOMEWORK: Make a function that asks the user for a message, and turns it into a list of numbers (a cypher)
# secret_message = input("What is the secret message you would like to send?")
# secret_number = input("What would you like your secret number to be?")
# coded_message = []
# decoded_message = ""
#
# def cypher(secret_message):
#     # coded_message = []
#     for s in secret_message:
#         character = ord(s) + secret_number
#         coded_message.append(character)
#     print("Your secret coded message: " + str(coded_message))
#
# cypher(secret_message)
#
# def decode(coded_message):
#     decoded_characters = []
#     for c in coded_message:
#         character = chr(c - secret_number)
#         decoded_characters.append(character)
#     decoded_message = "".join(decoded_characters)
#     print("Your decoded message: " + decoded_message)
#
# decode(coded_message)

# -------- World --------------
import random
M = 'land'
o = 'water'
world = []

# def create_world(world_size):
#     for w in range(0,world_size):
#         row = []
#         i = 0
#         while i < world_size:
#             if random.randrange(2) == 0:
#                 tile = o
#                 row.append(tile)
#                 i = i + 1
#             else:
#                 tile = M
#                 row.append(tile)
#                 i = i + 1
#         world.append(row)
#
# create_world(2)
# print(world)

world = [
        [o,M,o],
        [o,M,M]
        ]
def continent_counter(world, x, y):
    continent_tiles = []
    for c in continent_tiles:
        if world[x][y] == 'land':
            continent_tiles.append([x, y])
            continent_counter(world, x - 1, y - 1)
        else:
            return "Not land"
    # continent_size = 0
    # for c in continent_tiles:
    #     if c[0] == x and c[1] == y:
    #         return
    #     else:
    #         if x >= len(world) or x < 0 or y >= len(world) or y < 0:
    #             # print("This coordinate is not valid")
    #             return
    #         elif world[y][x] != 'land':
    #             # continent_size = 0
    #             # print("This coordinate is water")
    #             return
    #         else:
    #             continent_tiles.append([x, y])
    #             continent_counter(world, x - 1, y - 1)
    # above
    # continent_counter(world, x - 1, y - 1)
    # continent_counter(world, x    , y - 1)
    # continent_counter(world, x + 1, y - 1)
    # # continent_size = continent_size + continent_counter(world, x - 1, y - 1)
    # # continent_size = continent_size + continent_counter(world, x    , y - 1)
    # # continent_size = continent_size + continent_counter(world, x + 1, y - 1)
    # # right
    # continent_counter(world, x + 1, y)
    # # continent_size = continent_size + continent_counter(world, x + 1, y)
    # # below
    # # continent_counter(world, x + 1, y + 1)
    # # continent_counter(world, x    , y + 1)
    # # continent_counter(world, x - 1, y + 1)
    # # continent_size = continent_size + continent_counter(world, x + 1, y + 1)
    # # continent_size = continent_size + continent_counter(world, x    , y + 1)
    # # continent_size = continent_size + continent_counter(world, x - 1, y + 1)
    # # left
    # # continent_counter(world, x - 1, y)
    # # continent_size = continent_size + continent_counter(world, x - 1, y)

    return len(continent_tiles)

# print("The size of the continent you landed on is: " + str(continent_counter(world, 4, 5)))

print(continent_counter(world, 1, 1))

# print(world[1][11])
#
# 2,7



# world = [
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
# print(len(world))






# ------- student list -----------------
#
# a = "deb"
# b = "Jess"
# c = "Elle"
# d = "tim"
# students = [a, b, c, d]
#
# print(students)
#
# sisters = ["Christina", "Jesse", "alteredco", "LamboFantastico"]
#
# print(sisters)
#
# members = [students, sisters]
#
# print(members)
#
# print(members[0][3])
