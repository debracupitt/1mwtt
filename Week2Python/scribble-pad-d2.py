# -*- coding: utf-8 -*-
# python scrapy library
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


# print(len(world))
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
    return board_words

print("Normal board: ")
print_board(world2)

# world2_reversed = list(reversed(world2))
# # list(reversed(list1))
#
# print_board(world2_reversed)
# print("Reversed board 1: ")
# print(world2[::-1])

# world2_reversed = world2[::-1]
# world2_row1_reversed = world2_reversed[0][::-1]
# world2_row2_reversed = world2_reversed[1][::-1]
#
#
# print("Reversed board A: ")
# print(world2_reversed)
# print("Reversed board B: ")
# print(world2_row1_reversed)
# print(world2_row2_reversed)

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
    print(new_board)
    return new_board

print("Reversed board: ")
print_board_reverse(world2)
