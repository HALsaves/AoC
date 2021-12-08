#!/usr/bin/env python3
"""Advent of Code"""
import csv
import sys
from pprint import pprint

def main():
    """MAIN"""
    ex_data = read_in_data('./ex5')
    my_data = read_in_data('./input5')

    # Part 1
    print('Example 1:')
    part1(ex_data)
    print('\nSolution 1:')
    part1(my_data)

    # Part 2
    print('\nExample 2:')
    part2(ex_data)
    print('\nSolution 2:')
    part2(my_data)

def part1(data):
    """part 1"""
    max_x, max_y = find_maxes(data)
    grid = [[0]*(max_x+1) for y in range(max_y+1)]
    for x1,y1,x2,y2 in data:
        if y1 == y2:
            for x in range(*((x1,x2+1) if x2 > x1 else (x2,x1+1))):
                grid[y1][x] += 1
        if x1 == x2:
            for y in range(*((y1,y2+1) if y2 > y1 else (y2,y1+1))):
                grid[y][x1] += 1
    sum = 0
    for row in grid:
        for i in row:
            if i >= 2:
                sum += 1
    #pprint(grid)
    print(sum)

def part2(data):
    """part 1"""
    max_x, max_y = find_maxes(data)
    grid = [[0]*(max_x+1) for y in range(max_y+1)]
    for x1,y1,x2,y2 in data:
        if y1 == y2:
            for x in range(*((x1,x2+1) if x2 > x1 else (x2,x1+1))):
                grid[y1][x] += 1
        elif x1 == x2:
            for y in range(*((y1,y2+1) if y2 > y1 else (y2,y1+1))):
                grid[y][x1] += 1
        else:
            if x1 > x2:
                x1, y1, x2, y2 = x2, y2, x1, y1
            y_step =(1 if y2 > y1 else -1)
            y = y1
            for x in range(*((x1,x2+1) if x2 >= x1 else (x2,x1+1))):
                grid[y][x] += 1
                y += y_step
    sum = 0
    for row in grid:
        for i in row:
            if i >= 2:
                sum += 1
    #pprint(grid)
    print(sum)

def find_maxes(data): 
    max_x = 0
    max_y = 0
    for x1,y1,x2,y2 in data:
        if x1 > max_x:
            max_x = x1
        if x2 > max_x:
            max_x = x2
        if y1 > max_y:
            max_y = y1
        if y2 > max_y:
            max_y = y2
    return max_x, max_y

def read_in_data(data_file):
    raw_data=[]
    with open(data_file, encoding='utf-8', mode='r') as input_file:
        reader = csv.reader(input_file, delimiter=" ")
        for row in reader:
            raw_data.append([int(x) for x in row])
            #raw_data.append(row)
            #raw_data.append(row[0]) # if single element
    final_data = alter_data(raw_data)
    return final_data

def alter_data(raw_data):
    final_data = raw_data
    #final_data = [[i[0:2],i[2:4]] for i in raw_data] 
    return final_data

if __name__ == '__main__':
    main()
