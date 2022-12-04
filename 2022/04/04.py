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
    matches = 0
    for pair in data:
        if set(pair[0]).issubset(set(pair[1])):
            matches += 1
        elif set(pair[1]).issubset(set(pair[0])):
            matches += 1
    print(matches)


def part2(data):
    """part 2"""
    matches = 0
    for pair in data:
        if set(pair[0]).intersection(set(pair[1])):
            matches += 1
    print(matches)


def read_in_data(data_file):
    """Read in the data"""
    raw_data = []
    with open(data_file, encoding="utf-8", mode="r") as input_file:
        reader = csv.reader(input_file, delimiter=" ")
        for row in reader:
            raw_data.append(row[0].split(","))
    final_data = alter_data(raw_data)
    return final_data


def alter_data(raw_data):
    """Alter the data to fit the problem"""
    final_data = []
    for row in raw_data:
        elf1 = [int(i) for i in row[0].split("-")]
        elf2 = [int(i) for i in row[1].split("-")]
        final_data.append([list(range(elf1[0], elf1[1] + 1)), list(range(elf2[0], elf2[1] + 1))])
    return final_data


if __name__ == "__main__":
    main()
