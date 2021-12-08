#!/usr/bin/env python3
"""Advent of Code"""
import csv
import pprint

def main():
    """MAIN"""
    example_data = []
    my_data = []

    with open("./ex4", encoding='utf-8', mode='r') as input_file:
        reader = csv.reader(input_file, delimiter=" ")
        for row in reader:
            example_data.append([int(x) for x in row])

    with open("./input4", encoding='utf-8', mode='r') as input_file:
        reader = csv.reader(input_file, delimiter=" ")
        for row in reader:
            my_data.append([int(x) for x in row])

    ex_draw, ex_boards = org_data(example_data)
    my_draw, my_boards = org_data(my_data)
    # Part 1
    print('Example 1:')
    part1(ex_draw, ex_boards)
    print('\nSolution 1:')
    part1(my_draw, my_boards)

    # Part 2
    print('\nExample 2:')
    part2(ex_draw, ex_boards)
    print('\nSolution 2:')
    part2(my_draw, my_boards)

def part1(draws, boards):
    """part 1"""
    for draw in draws:
        for b, board in enumerate(boards):
            for r, row in enumerate(board):
                for i,v in enumerate(row):
                    if v == draw:
                        boards[b][r][i] = -1 
            score = check_for_win(board)
            if score:
                print(score * draw)
                return
    return 1  

def part2(draws, boards):
    """part 2"""
    board_list = [*range(0, len(boards))]
    for draw in draws:
        for b, board in enumerate(boards):
            if b not in board_list:
                continue
            for r, row in enumerate(board):
                for i,v in enumerate(row):
                    if v == draw:
                        boards[b][r][i] = -1 
            score = check_for_win(board)
            if score:
                board_list.remove(b)
                if len(board_list) == 0:
                    print(score * draw)
                    return
    return 1  

def check_for_win(board):
    for i,row in enumerate(board):
        if sum(row) == -5:
            return score(board)
        if sum([row[i] for row in board]) == -5:
            return score(board)
    return

def score(board):
    score = 0
    for row in board:
        score += sum([0 if x == -1 else x for x in row])
    return score

def org_data(data):
    draw = data[0]
    i = -1
    #boards = [0] * (len(data)-1)/6
    boards = []
    board=[]
    for row in data[2:]:
        if len(row) == 0:
            boards.append(board)
            board = []
            continue
        board.append(row)
    boards.append(board)
    return draw, boards

if __name__ == '__main__':
    main()
