# coding: utf-8
#  -------- World --------------
import random
M = 'land'
o = 'water'
world = []
x = ""
y = ""
a = 0
b = 0

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
print(world)

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

x_coordinate = int(input('What "x" coordinate would you like to land on? You must choose a number between 0 and ' + str(world_size - 1) + ":  "))

def check_x(world_size, x_coordinate):
    if x_coordinate >= 0 and x_coordinate < world_size:
        return x_coordinate
    else:
        x_coordinate = int(input('What "x" coordinate would you like to land on? You must choose a number between 0 and ' + str(world_size - 1) + ":  "))
        check_x(world_size, x_coordinate)

check_x(world_size, x_coordinate)
a = x_coordinate

y_coordinate = int(input('What "y" coordinate would you like to land on? You must choose a number between 0 and ' + str(world_size - 1) + ":  "))

def check_y(world_size, y_coordinate):
    if y_coordinate >= 0 and y_coordinate < world_size:
        return y_coordinate
    else:
        y_coordinate = int(input('What "y" coordinate would you like to land on? You must choose a number between 0 and ' + str(world_size - 1) + ":  "))
        check_y(world_size, y_coordinate)

check_y(world_size, y_coordinate)
b = y_coordinate

your_continent = continent_counter(world, a, b)

print(a)
print(b)

print("The size of the continent you landed on is: " + str(your_continent) + " hectares")


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
