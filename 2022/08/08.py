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
    ex_data = read_in_data("./ex")
    my_data = read_in_data("./in")
    print("\nExample 2:")
    part2(ex_data)
    print("\nSolution 2:")
    part2(my_data)


def part1(data):
    """part 1"""
    visible = determine_visible(data)
    count = 0
    for row in visible:
        for i in row:
            if i > 0:
                count += 1
    print(count)


def determine_visible(data):
    for i in range(1, len(data) - 1):
        for j in range(1, len(data) - 1):
            data[i][j] = -1 * data[i][j]
    for i in range(1, len(data) - 1):
        maxh = data[i][0]
        maxv = data[0][i]
        for j in range(1, len(data) - 1):
            if abs(data[i][j]) > maxh:
                data[i][j] = abs(data[i][j])
                maxh = data[i][j]
            if abs(data[j][i]) > maxv:
                data[j][i] = abs(data[j][i])
                maxv = data[j][i]
        maxh = data[i][-1]
        maxv = data[-1][i]
        for j in range(len(data) - 2, 0, -1):
            if abs(data[i][j]) > maxh:
                data[i][j] = abs(data[i][j])
                maxh = data[i][j]
            if abs(data[j][i]) > maxv:
                data[j][i] = abs(data[j][i])
                maxv = data[j][i]
    return data


def part2(data):
    """part 2"""
    best = 0
    for i in range(1, len(data) - 1):
        for j in range(1, len(data) - 1):
            tree = tree_score(data, i, j)
            if tree > best:
                best = tree
    print(best)


def tree_score(data, i, j):
    """Calculate each trees view score"""
    height = data[i][j]
    product = 1
    # E
    score = 0
    for x in range(j + 1, len(data)):
        score += 1
        if data[i][x] >= height:
            break
    product *= score
    # W
    score = 0
    for x in range(j - 1, -1, -1):
        score += 1
        if data[i][x] >= height:
            break
    product *= score
    # S
    score = 0
    for y in range(i + 1, len(data)):
        score += 1
        if data[y][j] >= height:
            break
    product *= score
    # N
    score = 0
    for y in range(i - 1, -1, -1):
        score += 1
        if data[y][j] >= height:
            break
    product *= score
    return product


def read_in_data(data_file):
    """Read in the data"""
    raw_data = []
    with open(data_file, encoding="utf-8", mode="r") as input_file:
        reader = csv.reader(input_file, delimiter=" ")
        for row in reader:
            raw_data.append([int(i) + 1 for i in list(row[0])])  # if single element
    final_data = alter_data(raw_data)
    return final_data


def alter_data(raw_data):
    """Alter the data to fit the problem"""
    final_data = raw_data
    return final_data


if __name__ == "__main__":
    main()
