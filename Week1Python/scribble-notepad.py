# coding: utf-8

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
world = create_wld(wld_sz_fnl)

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

your_continent = continent_counter(world, x_fnl, y_fnl)

print(your_continent)

print("The size of the continent you landed on at coordinates (" + str(x_fnl) + ", " + str(y_fnl) + ") is: " + str(your_continent) + " hectares")
