from aoc.utils import parsing
from collections import Counter

input_parser = parsing.split_lines

def parse_input(input_data):
    list1 = []
    list2 = []
    for line in input_data:
        left_val, right_val = line.strip().split()
        list1.append(int(left_val))
        list2.append(int(right_val))

    return sorted(list1), sorted(list2)

def part1(input_data):
    list1, list2 = parse_input(input_data)

    return sum([abs(left_val - right_val) for left_val, right_val in zip(list1, list2)])


def part2(input_data):
    list1, list2 = parse_input(input_data)

    list2_counts = Counter(list2)

    return sum([list2_counts[val]*val for val in list1])
