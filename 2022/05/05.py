#!/usr/bin/env python3
"""Advent of Code"""
import csv
from pprint import pprint


def main():
    """MAIN"""
    ex_moves = read_in_moves("./ex2")
    in_moves = read_in_moves("./in2")
    # my_data = read_in_data("./in")

    # Part 1
    print("Example 1:")
    ex_stack = read_in_stack("./ex1")
    pprint(ex_stack)
    pprint(ex_moves)
    part1(ex_stack, ex_moves)
    print("\nSolution 1:")
    in_stack = read_in_stack("./in1")
    part1(in_stack, in_moves)

    # Part 2
    print("\nExample 2:")
    ex_stack = read_in_stack("./ex1")
    part2(ex_stack, ex_moves)
    print("\nSolution 2:")
    in_stack = read_in_stack("./in1")
    part2(in_stack, in_moves)


def part1(stacks, moves):
    """part 1"""
    for move in moves:
        for i in range(move[0]):
            stacks[move[2]].append(stacks[move[1]].pop())
    out = ""
    pprint(out.join([i[-1] for i in stacks]))


def part2(stacks, moves):
    """part 1"""
    for move in moves:
        stacks[move[2]].extend(stacks[move[1]][(-1 * move[0]) :])
        for i in range(move[0]):
            stacks[move[1]].pop()
    out = ""
    pprint(out.join([i[-1] for i in stacks]))


def read_in_stack(data_file):
    """Read in the data"""
    raw_data = []
    stack = []
    with open(data_file, encoding="utf-8", mode="r") as input_file:
        lines = input_file.readlines()
        num_stacks = int(len(lines[0]) / 4)
        stacks = [[] for i in range(num_stacks)]
        for line in lines:
            i = 1
            for j in range(num_stacks):
                if line[i] != " ":
                    stacks[j].insert(0, line[i])
                i += 4
    return stacks


def read_in_moves(data_file):
    """Read in the data"""
    raw_data = []
    with open(data_file, encoding="utf-8", mode="r") as input_file:
        reader = csv.reader(input_file, delimiter=" ")
        for row in reader:
            raw_data.append([int(row[1]), int(row[3]) - 1, int(row[5]) - 1])
            # raw_data.append([int(x) for x in row if ])
            # raw_data.append(row[0]) # if single element
    return raw_data


if __name__ == "__main__":
    main()
