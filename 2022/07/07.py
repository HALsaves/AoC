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
    sizes = {}
    sizes["/"] = tree_sizes(data["root"], "/", sizes)
    total = 0
    for dirname, size in sizes.items():
        if size <= 100000:
            total += size
    print("total:", total)


def part2(data):
    """part 2"""
    sizes = {}
    sizes["/"] = tree_sizes(data["root"], "/", sizes)
    total = 0
    smallest = "/"
    for dirname, size in sizes.items():
        if sizes["/"] - sizes[dirname] <= 40000000 and sizes[dirname] < sizes[smallest]:
            smallest = dirname
    print("smallest:", smallest, sizes[smallest])


def tree_sizes(pwd, name, sizes):
    sizes[name] = 0
    for obj in pwd.keys():
        if isinstance(pwd[obj], dict):
            sizes[name] += tree_sizes(pwd[obj], name + obj + "/", sizes)
        elif isinstance(pwd[obj], int):
            sizes[name] += pwd[obj]
    return sizes[name]


def read_in_data(data_file):
    """Read in the data"""
    raw_data = []
    with open(data_file, encoding="utf-8", mode="r") as input_file:
        reader = csv.reader(input_file, delimiter=" ")
        for row in reader:
            raw_data.append(row)
    final_data = alter_data(raw_data)
    return final_data


def alter_data(raw_data):
    """Alter the data to fit the problem"""
    tree = {"root": {}}
    pwd = tree["root"]
    i = 0
    add_dir_items(raw_data, 1, pwd)
    return tree


def add_dir_items(rows, i, pwd):
    while i < len(rows):
        if i == len(rows):
            return i
        if rows[i][0] == "$":
            if rows[i][1] == "cd":
                if rows[i][2] == "..":
                    return i
                else:
                    pwd[rows[i][2]] = {}
                    i = add_dir_items(rows, i + 1, pwd[rows[i][2]])
        elif rows[i][0] == "dir":
            pwd[rows[i][1]] = {}
        else:
            pwd[rows[i][1]] = int(rows[i][0])
        i += 1
    return i


if __name__ == "__main__":
    main()
