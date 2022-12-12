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
    clock = 1
    regx = 1
    vals = [1]
    for cmd, arg in data:
        vals.append(regx)
        if cmd == "addx":
            vals.append(regx)
            regx += arg
    print([i * vals[i] for i in range(20, 221, 40)])
    print(sum([i * vals[i] for i in range(20, 221, 40)]))


def part2(data):
    """part 2"""
    clock = 1
    regx = 1
    vals = [1]
    for cmd, arg in data:
        vals.append(regx)
        if cmd == "addx":
            vals.append(regx)
            regx += arg
    for j in range(1, 241, 40):
        row = ""
        for clock in range(j, j + 40):
            if clock - j in [vals[clock] - 1, vals[clock], vals[clock] + 1]:
                row += "#"
            else:
                row += "."
        print(row, len(row))


def read_in_data(data_file):
    """Read in the data"""
    raw_data = []
    with open(data_file, encoding="utf-8", mode="r") as input_file:
        reader = csv.reader(input_file, delimiter=" ")
        for row in reader:
            if len(row) == 1:
                row.append(0)
            raw_data.append([row[0], int(row[1])])
    return raw_data


if __name__ == "__main__":
    main()
