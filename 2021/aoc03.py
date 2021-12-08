#!/usr/bin/env python3
"""Advent of Code"""
import csv

def main():
    """MAIN"""
    my_data = []
    with open("./input3", encoding='utf-8', mode='r') as input_file:
        reader = csv.reader(input_file, delimiter=" ")
        for row in reader:
            my_data.append(row[0])
    # Part 1
    print('Example 1:')
    part1(example_data)
    print('\nSolution 1:')
    part1(my_data)

    # Part 2
    print('\nExample 2:')
    part2(example_data)
    print('\nSolution 2:')
    part2(my_data)

def part1(data):
    """part 1"""
    sums = [0] * len(data[0])
    for xxx in data:
        for i, v in enumerate(xxx):
            sums[i] += int(v)
    gamma   = [ '1' if i/len(data) > .5 else '0' for i in sums ]
    epsilon = [ '0' if i/len(data) > .5 else '1' for i in sums ]
    print(int(''.join(gamma), 2) * int(''.join(epsilon),2))

def part2(data):
    """part 2"""
    ox_plus = next_list(data, 0, 'most')
    co2_minus = next_list(data, 0, 'least')
    print(ox_plus, co2_minus)
    print(int(ox_plus[0], 2) * int(co2_minus[0],2))

def next_list(nums, pos, sel_type):
    """recursion"""
    xsum = 0
    for xxx in nums:
        xsum += int(xxx[pos])
    if sel_type == 'most':
        selector = '1' if xsum/len(nums) >= .5 else '0'
    else:
        selector = '1' if xsum/len(nums) < .5 else '0'
    new_nums = [ i for i in nums if i[pos] == selector ]
    if len(new_nums) > 1 or pos == (len(xxx)-2):
        return next_list(new_nums, pos+1, sel_type)
    return new_nums

example_data = [
        '00100',
        '11110',
        '10110',
        '10111',
        '10101',
        '01111',
        '00111',
        '11100',
        '10000',
        '11001',
        '00010',
        '01010',
]

if __name__ == '__main__':
    main()
