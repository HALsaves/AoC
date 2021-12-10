#!/usr/bin/env python3
"""Advent of Code"""
import csv

def main():
    """MAIN"""
    ex_data = read_in_data('./ex7')
    my_data = read_in_data('./input7')

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
    data.sort()
    median = int((len(data)+1)/2)
    print(data[median])
    print(cost1(data, data[median]))

def part2(data):
    """part 2"""
    #data.sort()
    mean = int((sum(data) / len(data)) + .5)
    cost_min = cost2(data, mean-5)
    print(mean-5, cost_min)
    for i in range(-4,5):
        print(i, mean+i)
        cost = cost2(data, mean+i)
        if cost < cost_min:
            cost_min=cost
        print(mean+i, cost, cost_min)
    print('min: ',cost_min)

def cost1(positions, position):
    """ part 1 cost"""
    distances = [ abs(position - i) for i in positions ]
    return sum(distances)

def cost2(positions, position):
    """ part 2 cost"""
    distances = [ int(abs((position-i)*(abs(position - i)+1)/2)) for i in positions ]
    return sum(distances)

def read_in_data(data_file):
    """Read in the data"""
    raw_data=[]
    with open(data_file, encoding='utf-8', mode='r') as input_file:
        reader = csv.reader(input_file, delimiter=",")
        for row in reader:
            raw_data.append(row)
            #raw_data.append([int(x) for x in row])
            #raw_data.append(row[0]) # if single element
    final_data = alter_data(raw_data)
    return final_data

def alter_data(raw_data):
    """Alter the data to fit the problem"""
    final_data = [int(i) for i in raw_data[0]]
    return final_data

if __name__ == '__main__':
    main()
