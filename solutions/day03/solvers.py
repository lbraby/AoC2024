from aoc.utils import parsing
import re

input_parser = parsing.split_lines


def part1(input_data):
    sum_mults = 0
    for line in input_data:
        pattern = "mul\([0-9]{1,3},[0-9]{1,3}\)"
        matches = re.findall(pattern, line)
        for match in matches:
            nums = list(map(int, match.split("(")[1].split(")")[0].split(",")))
            sum_mults += nums[0] * nums[1]

    return sum_mults

def part2(input_data):
    sum_mults = 0
    enabled = True
    for line in input_data:
        pattern = "mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)"
        matches = re.findall(pattern, line)
        
        for match in matches:
            if match == "do()":
                enabled = True
                continue
            elif match == "don't()":
                enabled = False
                continue

            if enabled:
                nums = list(map(int, match.split("(")[1].split(")")[0].split(",")))
                sum_mults += nums[0] * nums[1]

    return sum_mults
