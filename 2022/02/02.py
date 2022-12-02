#!/usr/bin/env python3
"""Advent of Code"""
import csv
from pprint import pprint


def main():
    """MAIN"""
    ex_data = read_in_data("./ex")
    my_data = read_in_data("./in")

    score = {"X": 1, "Y": 2, "Z": 3, "A": 1, "B": 2, "C": 3}
    wins = {"A": "Y", "B": "Z", "C": "X"}
    draws = {"A": "X", "B": "Y", "C": "Z"}

    # Part 1
    print("Example 1:")
    print(part1(ex_data, score, wins, draws))
    print("\nSolution 1:")
    print(part1(my_data, score, wins, draws))

    # Part 2
    print("\nExample 2:")
    print(part2(ex_data, score))
    print("\nSolution 2:")
    print(part2(my_data, score))


def part1(data, score_map, wins, draws):
    """part 1"""
    score = 0
    for play, response in data:
        score += score_map[response]
        if wins[play] == response:
            score += 6
        elif draws[play] == response:
            score += 3
    return score


def part2(data, score_map):
    """part 2"""
    score = 0
    for play, outcome in data:
        if outcome == "X":
            score += ((score_map[play] + 1) % 3) + 1
        if outcome == "Y":
            score += score_map[play] + 3
        if outcome == "Z":
            score += ((score_map[play] % 3) + 1) + 6
    return score


def read_in_data(data_file):
    """Read in the data"""
    raw_data = []
    with open(data_file, encoding="utf-8", mode="r") as input_file:
        reader = csv.reader(input_file, delimiter=" ")
        for row in reader:
            raw_data.append(row)
    return raw_data


if __name__ == "__main__":
    main()
