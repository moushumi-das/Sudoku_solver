# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 10:01:09 2021

@author: moush
"""
sodoku_board= [
    [0,0,0,0,4,0,0,7,0],
    [7,2,0,0,6,5,0,0,1],
    [0,8,6,0,0,0,0,0,0],
    [0,0,0,0,0,0,4,0,0],
    [0,0,5,0,3,0,0,0,6],
    [0,0,0,0,1,0,0,8,0],
    [9,4,0,0,0,8,7,0,0],
    [1,7,0,0,0,0,3,0,4],
    [0,0,0,0,0,0,0,0,0]
]


# backtracking function for finding the ultimate correct solution
def solve_puzzle(bo):
    find_match = find_empty_space(bo)
    if not find_match:
        return True
    else:
        row, column = find_match

    for i in range(1,10):
        if possible_solution(bo, i, (row, column)):
            bo[row][column] = i

            if solve_puzzle(bo):
                return True

            bo[row][column] = 0

    return False


def possible_solution(board, number, position):
    # Checking row
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False

    # Checking column
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False

    # Checking square box
    square_box_x = position[1] // 3
    square_box_y = position[0] // 3

    for i in range(square_box_y*3,square_box_y*3 + 3):
        for j in range(square_box_x * 3, square_box_x*3 + 3):
            if board[i][j] == number and (i,j) != position:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("----------------------- ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty_space(bo):
    for row in range(len(bo)):
        for col in range(len(bo[0])):
            if bo[row][col] == 0:
                return (row, col)  # row, col

    return None
print("Printing sodoku puzzle: ")
print_board(sodoku_board)
solve_puzzle(sodoku_board)
print("Printing final version of solved board:")
print_board(sodoku_board)