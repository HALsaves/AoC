#!/usr/bin/env python3
"""Advent of Code"""
import csv
import sys
from itertools import permutations

def main():
    """MAIN"""
    ex_data = read_in_data('./ex8')
    my_data = read_in_data('./input8')

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
    uniq_sum=0
    for row in data:
        uniq_sum += len([i for i in row[11:15] if len(i) in [2,3,4,7]])
    print(uniq_sum)

def part2(data):
    """part 2"""
    vals = []
    for row in data:
        length2values = values_by_len(row)
        the_map = working_map(length2values)
        vals.append(get_value(row[11:15], the_map))
    print(vals)
    print(sum(vals))

def get_value(digits, alpha_map):
    """ Convert 4 alpha strings to the 4 digit number using the found map """
    val = []
    for digit in digits:
        binary = alpha2binary(digit, alpha_map)
        val.append(str(binary2digit(binary)))
    return int(''.join(val))

def working_map(l2v):
    """Go through all permutations until all the chars(abcdefg) work. Return map."""
    # Get all permutations of [1, 2, 3]
    perm = permutations(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    # Print the obtained permutations
    for i in list(perm):
        alpha_map = {v:k for (k,v) in dict(enumerate(i)).items()}
        if alpha2binary(l2v[2][0], alpha_map) != 48: # 2
            continue
        if alpha2binary(l2v[3][0], alpha_map) != 112: # 7
            continue
        if alpha2binary(l2v[4][0], alpha_map) != 51: # 4
            continue
        if alpha2binary(l2v[7][0], alpha_map) != 127: # 8
            continue
        for j in [0,1,2]:
            if alpha2binary(l2v[5][j], alpha_map) not in [109, 121, 91]: # 2 3 5
                break
            if alpha2binary(l2v[6][j], alpha_map) not in [126, 95, 123]: # 0 6 9
                break
        else:
            return alpha_map
    print("Never should get here")
    sys.exit()

def alpha2binary(alpha, alpha_map):
    """ Convert an alpha string to a binary for this map """
    lightmap = {
        0: 0b0000001,
        1: 0b0000010,
        2: 0b0000100,
        3: 0b0001000,
        4: 0b0010000,
        5: 0b0100000,
        6: 0b1000000,
    }
    binary = 0
    for letter in alpha:
        binary |= lightmap[alpha_map[letter]]
    return binary

def values_by_len(row):
    """ Map the values, sorted, to their length.  Remove dups."""
    vxl = {2:[], 3:[], 4:[], 5:[], 6:[], 7:[]}
    sorted_v = [''.join(sorted(i)) for i in row if i != '|']
    _ = [vxl[len(i)].append(i) for i in sorted_v if i not in vxl[len(i)]]
    return vxl

def binary2digit(binary):
    """ Convert a binary number to it's cooresponding numeric digit """
    num2lights = {
        0: 0b1111110,
        1: 0b0110000,
        2: 0b1101101,
        3: 0b1111001,
        4: 0b0110011,
        5: 0b1011011,
        6: 0b1011111,
        7: 0b1110000,
        8: 0b1111111,
        9: 0b1111011
    }
    b2d = {v:k for (k,v) in num2lights.items()} # Oops, reverse it
    return b2d[binary]

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

#    0   0   6   💡  💡  💡  💡  💡  💡      01111110    0x7E    00111111    0x3F
#    1   1   2       💡  💡                  00110000    0x30    00000110    0x06
#    2   2   5   💡  💡      💡  💡      💡  01101101    0x6D    01011011    0x5B
#    3   3   5   💡  💡  💡  💡          💡  01111001    0x79    01001111    0x4F
#    4   4   4       💡  💡          💡  💡  00110011    0x33    01100110    0x66
#    5   5   5   💡      💡  💡      💡  💡  01011011    0x5B    01101101    0x6D
#    6   6   6   💡      💡  💡  💡  💡  💡  01011111    0x5F    01111101    0x7D
#    7   7   3   💡  💡  💡                  01110000    0x70    00000111    0x07
#    8   8   7   💡  💡  💡  💡  💡  💡  💡  01111111    0x7F    01111111    0x7F
#    9   9   6   💡  💡  💡  💡      💡  💡  01111011    0x7B    01101111    0x6F
