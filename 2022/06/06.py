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
    pprint(ex_data)
    part1(ex_data, 4)
    print("\nSolution 1:")
    part1(my_data, 4)

    # Part 2
    print("\nExample 2:")
    part1(ex_data, 14)
    print("\nSolution 2:")
    part1(my_data, 14)


def part1(data, win_size):
    """part 1"""
    for row in data:
        for i in range(len(row) - win_size):
            if len(set(row[i : i + win_size])) == win_size:
                print(i + win_size)
                break
        # print([i for i in range(len(row-4)) if [j for j in row[i:i+4] if j not


def part2(data):
    """part 2"""
    print(len(data))


def read_in_data(data_file):
    """Read in the data"""
    raw_data = []
    with open(data_file, encoding="utf-8", mode="r") as input_file:
        reader = csv.reader(input_file, delimiter=" ")
        for row in reader:
            # raw_data.append(row)
            # raw_data.append([int(x) for x in row])
            raw_data.append(row[0])  # if single element
    final_data = alter_data(raw_data)
    return final_data


def alter_data(raw_data):
    """Alter the data to fit the problem"""
    final_data = raw_data
    return final_data


if __name__ == "__main__":
    main()
