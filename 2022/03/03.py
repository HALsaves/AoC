#!/usr/bin/env python3
"""Advent of Code"""
import csv
from pprint import pprint


def main():
    """MAIN"""
    ex_data = read_in_data("./ex")
    my_data = read_in_data("./in")

    # Part 1
    print("Example 1:")
    # pprint(ex_data)
    part1(ex_data)
    print("\nSolution 1:")
    part1(my_data)

    # Part 2
    print("\nExample 2:")
    part2(ex_data)
    print("\nSolution 2:")
    part2(my_data)


def part1(data):
    """part 1"""
    sum = 0
    for sack in data:
        half = int(len(sack) / 2)
        c1 = sack[0:half]
        c2 = sack[(half * -1) :]
        # print(sack, c1, c2)
        common = [i for i in c1 if i in c2]
        # print(common[0], ord(common[0]))
        sum += letter_to_val(common[0])
    print(sum)


def part2(data):
    """part 2"""
    data2 = alter_data(data)
    # print(data2)
    sum = 0
    for sack in data2:
        common = [i for i in sack[0] if i in sack[1]]
        common = [i for i in sack[2] if i in common]
        # print(common[0], ord(common[0]))
        sum += letter_to_val(common[0])
    print(sum)


def letter_to_val(let):
    if let.islower():
        return ord(let) - 96
    elif let.isupper():
        return ord(let) - 38


def read_in_data(data_file):
    """Read in the data"""
    raw_data = []
    with open(data_file, encoding="utf-8", mode="r") as input_file:
        reader = csv.reader(input_file, delimiter=" ")
        for row in reader:
            # raw_data.append(row)
            # raw_data.append([int(x) for x in row])
            raw_data.append(row[0])  # if single element
    # final_data = alter_data(raw_data)
    return raw_data


def alter_data(raw_data):
    """Alter the data to fit the problem"""
    final_data = []
    arr = []
    for i in raw_data:
        arr.append(i)
        if len(arr) == 3:
            final_data.append(arr)
            arr = []
    return final_data


if __name__ == "__main__":
    main()
