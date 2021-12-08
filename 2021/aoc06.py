#!/usr/bin/env python3
"""Advent of Code"""
import csv

def main():
    """MAIN"""
    ex_data = read_in_data('./ex6')
    my_data = read_in_data('./input6')

    # Part 1
    print('Example 1:')
    part1(ex_data, 18)
    part1(ex_data, 80)
    print('\nSolution 1:')
    part1(my_data, 80)

    # Part 2
    print('\nExample 2:')
    part2(ex_data, 18)
    part2(ex_data, 80)
    part2(ex_data, 256)
    part2(my_data, 256)

def part1(fishes, days):
    """part 1"""
    for _ in range(0, days):
        fishes = [ x-1 for x in fishes ]
        for i, fish in enumerate(fishes):
            if fish == -1:
                fishes[i] = 6
                fishes.append(8)
    print(len(fishes))

def part2(fishes, days):
    """part 2"""
    num_per_days = [0] * 9
    for fish in fishes:
        num_per_days[fish] += 1
    for day in range(1, days+1):
        births = num_per_days.pop(0)
        num_per_days.append(births)
        num_per_days[6] += births
    print(day, sum(num_per_days))

def read_in_data(data_file):
    """read in the file"""
    raw_data=[]
    with open(data_file, encoding='utf-8', mode='r') as input_file:
        reader = csv.reader(input_file, delimiter=',')
        for row in reader:
            raw_data.append(row) # if single element
    final_data = alter_data(raw_data[0])
    return final_data

def alter_data(raw_data):
    """alter the inputs to fit the problem"""
    final_data = [int(i) for i in raw_data]
    return final_data

if __name__ == '__main__':
    main()
