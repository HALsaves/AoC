#!/usr/bin/env python3
"""Advent of Code"""
import csv
from pprint import pprint

def main():
    """MAIN"""
    ex_data = read_in_data('./ex5')
    my_data = read_in_data('./input5')

    # Part 1
    print('Example 1:')
    pprint(ex_data)
    #part1(ex_data)
    #print('\nSolution 1:')
    #part1(my_data)

    # Part 2
    #print('\nExample 2:')
    #part2(ex_data)
    #print('\nSolution 2:')
    #part2(my_data)

def part1(data):
    """part 1"""
    for xxx, yyy in data:
        print(xxx,'*', yyy)

def part2(data):
    """part 2"""
    print(len(data))

def read_in_data(data_file):
    """Read in the data"""
    raw_data=[]
    with open(data_file, encoding='utf-8', mode='r') as input_file:
        reader = csv.reader(input_file, delimiter=" ")
        for row in reader:
            raw_data.append(row)
            #raw_data.append([int(x) for x in row])
            #raw_data.append(row[0]) # if single element
    final_data = alter_data(raw_data)
    return final_data

def alter_data(raw_data):
    """Alter the data to fit the problem"""
    final_data = raw_data
    return final_data

if __name__ == '__main__':
    main()
