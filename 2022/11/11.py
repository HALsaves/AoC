#!/usr/bin/env python3
"""Advent of Code"""
import csv


def main():
    """MAIN"""
    # Part 1
    print("Example 1:")
    ex1 = Monkeys()
    ex1.monkeys.append(Monkey([79, 98], lambda x: x * 19, 23, 2, 3))
    ex1.monkeys.append(Monkey([54, 65, 75, 74], lambda x: x + 6, 19, 2, 0))
    ex1.monkeys.append(Monkey([79, 60, 97], lambda x: x * x, 13, 1, 3))
    ex1.monkeys.append(Monkey([74], lambda x: x + 3, 17, 0, 1))
    ex1.do_rounds(20, lambda x: int(x / 3))
    ex1.monkey_report()

    print("\nSolution 1:")
    in1 = Monkeys()
    in1.monkeys.append(Monkey([89, 73, 66, 57, 64, 80], lambda x: x * 3, 13, 6, 2))
    in1.monkeys.append(Monkey([83, 78, 81, 55, 81, 59, 69], lambda x: x + 1, 3, 7, 4))
    in1.monkeys.append(Monkey([76, 91, 58, 85], lambda x: x * 13, 7, 1, 4))
    in1.monkeys.append(Monkey([71, 72, 74, 76, 68], lambda x: x * x, 2, 6, 0))
    in1.monkeys.append(Monkey([98, 85, 84], lambda x: x + 7, 19, 5, 7))
    in1.monkeys.append(Monkey([78], lambda x: x + 8, 5, 3, 0))
    in1.monkeys.append(Monkey([86, 70, 60, 88, 88, 78, 74, 83], lambda x: x + 4, 11, 1, 2))
    in1.monkeys.append(Monkey([81, 58], lambda x: x + 5, 17, 3, 5))
    in1.do_rounds(20, lambda x: int(x / 3))
    in1.monkey_report()

    # Part 2
    print("\nExample 2:")
    ex2 = Monkeys()
    ex2.monkeys.append(Monkey([79, 98], lambda x: x * 19, 23, 2, 3))
    ex2.monkeys.append(Monkey([54, 65, 75, 74], lambda x: x + 6, 19, 2, 0))
    ex2.monkeys.append(Monkey([79, 60, 97], lambda x: x * x, 13, 1, 3))
    ex2.monkeys.append(Monkey([74], lambda x: x + 3, 17, 0, 1))
    factor = ex2.monkeys_factor()
    ex2.do_rounds(10000, lambda x: x % factor)
    ex2.monkey_report()

    print("\nSolution 2:")
    in2 = Monkeys()
    in2.monkeys.append(Monkey([89, 73, 66, 57, 64, 80], lambda x: x * 3, 13, 6, 2))
    in2.monkeys.append(Monkey([83, 78, 81, 55, 81, 59, 69], lambda x: x + 1, 3, 7, 4))
    in2.monkeys.append(Monkey([76, 91, 58, 85], lambda x: x * 13, 7, 1, 4))
    in2.monkeys.append(Monkey([71, 72, 74, 76, 68], lambda x: x * x, 2, 6, 0))
    in2.monkeys.append(Monkey([98, 85, 84], lambda x: x + 7, 19, 5, 7))
    in2.monkeys.append(Monkey([78], lambda x: x + 8, 5, 3, 0))
    in2.monkeys.append(Monkey([86, 70, 60, 88, 88, 78, 74, 83], lambda x: x + 4, 11, 1, 2))
    in2.monkeys.append(Monkey([81, 58], lambda x: x + 5, 17, 3, 5))
    factor = in2.monkeys_factor()
    in2.do_rounds(10000, lambda x: x % factor)
    in2.monkey_report()


class Monkeys:
    def __init__(self):
        self.monkeys = []

    def do_rounds(self, num, worry):
        for _ in range(0, num):
            for monkey in self.monkeys:
                monkey.round(self.monkeys, worry)

    def monkey_report(self):
        handled = sorted([self.monkeys[i].handled for i in range(0, len(self.monkeys))])
        print(handled[-1] * handled[-2])

    def monkeys_factor(self):
        factor = 1
        for i in range(0, len(self.monkeys)):
            factor *= self.monkeys[i].dev_by
        return factor


class Monkey:
    def __init__(self, items, op, div_by, if_true, if_false):
        self.items = items
        self.op = op
        self.dev_by = div_by
        self.if_true = if_true
        self.if_false = if_false
        self.handled = 0

    def round(self, monkeys, worry):
        for _ in range(0, len(self.items)):
            item = self.items.pop(0)
            self.handled += 1
            item = self.op(item)
            item = worry(item)
            if item % self.dev_by == 0:
                monkeys[self.if_true].items.append(item)
            else:
                monkeys[self.if_false].items.append(item)


def read_in_data(data_file):
    """Read in the data"""
    raw_data = []
    with open(data_file, encoding="utf-8", mode="r") as input_file:
        reader = csv.reader(input_file, delimiter=" ")
        for row in reader:
            raw_data.append(row)
            # raw_data.append([int(x) for x in row])
            # raw_data.append(row[0]) # if single element
    final_data = alter_data(raw_data)
    return final_data


def alter_data(raw_data):
    """Alter the data to fit the problem"""
    final_data = raw_data
    return final_data


if __name__ == "__main__":
    main()
