from aoc.utils import parsing

from collections import defaultdict

input_parser = parsing.split_lines

def parse_input(input_data):
    towels = input_data[0].split(", ")
    designs = input_data[2:]
    return towels, designs

memoiry = {}

def count_possible(design, towels):
    if design == "":
        return 1
    
    count = 0
    for towel in towels:
        if design.startswith(towel):
            if design[len(towel):] not in memoiry:
                memoiry[design[len(towel):]] = count_possible(design[len(towel):], towels)
            count += memoiry[design[len(towel):]]
        
    return count

def part1(input_data):
    towels, designs = parse_input(input_data)
    return sum([count_possible(design, towels) > 0 for design in designs])
    
def part2(input_data):
    towels, designs = parse_input(input_data)
    return sum([count_possible(design, towels) for design in designs])
