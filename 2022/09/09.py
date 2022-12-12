#!/usr/bin/env python3
"""Advent of Code"""
import csv
from pprint import pprint


def main():
    """MAIN"""

    # Part 1
    print("Example 1:")
    AoC("./ex", 2)
    print("\nSolution 1:")
    AoC("./in", 2)

    # Part 2
    print("\nExample 2:")
    AoC("./ex2", 10)
    print("\nSolution 2:")
    AoC("./in", 10)


class AoC:
    def __init__(self, in_file, knots):
        data = read_in_data(in_file)
        self.rope = [{"x": 0, "y": 0} for i in range(0, knots)]
        self.tails = {"0,0"}
        for move in data:
            self.move_head(move, 0)
            for knot in range(1, knots):
                self.move_tail(knot)
            self.tails.add(f"{self.rope[-1]['x']},{self.rope[-1]['y']}")
        print(len(self.tails))

    def move_head(self, move, knot):
        if move == "R":
            self.rope[knot]["x"] += 1
        elif move == "L":
            self.rope[knot]["x"] -= 1
        elif move == "U":
            self.rope[knot]["y"] += 1
        elif move == "D":
            self.rope[knot]["y"] -= 1

    def move_tail(self, knot):
        if (
            abs(self.rope[knot - 1]["x"] - self.rope[knot]["x"]) >= 2
            or abs(self.rope[knot - 1]["y"] - self.rope[knot]["y"]) >= 2
        ):
            if self.rope[knot - 1]["x"] > self.rope[knot]["x"]:
                self.rope[knot]["x"] += 1
            elif self.rope[knot - 1]["x"] < self.rope[knot]["x"]:
                self.rope[knot]["x"] -= 1
            if self.rope[knot - 1]["y"] > self.rope[knot]["y"]:
                self.rope[knot]["y"] += 1
            elif self.rope[knot - 1]["y"] < self.rope[knot]["y"]:
                self.rope[knot]["y"] -= 1


def read_in_data(data_file):
    """Read in the data"""
    rows = []
    with open(data_file, encoding="utf-8", mode="r") as input_file:
        reader = csv.reader(input_file, delimiter=" ")
        for row in reader:
            rows.extend([row[0] for i in range(0, int(row[1]))])
    return rows


if __name__ == "__main__":
    main()
