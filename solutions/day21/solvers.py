from aoc.utils import parsing

import re

input_parser = parsing.split_lines

def assemble_movements(keypad):
    positions = {}
    for y in range(len(keypad)):
        for x in range(len(keypad[0])):
            positions[keypad[y][x]] = (x, y)

    movements = {}
    for key1, key1_pos in positions.items():
        if key1 == "": continue
        for key2, key2_pos in positions.items():
            if key2 == "": continue
            # lateral movement
            x_dist = key2_pos[0] - key1_pos[0]
            if x_dist < 0: lateral = ["<"] * (-1*x_dist)
            else: lateral = [">"] * x_dist

            # vertical movement
            y_dist = key2_pos[1] - key1_pos[1]
            if y_dist < 0: vertical = ["^"] * (-1*y_dist)
            else: vertical = ["v"] * y_dist

            if key1_pos[0] == positions[""][0] and key2_pos[1] == positions[""][1]:
                movements[(key1, key2)] = lateral + vertical + ["A"]
            elif key1_pos[1] == positions[""][1] and key2_pos[0] == positions[""][0]:
                movements[(key1, key2)] = vertical + lateral + ["A"]
            elif x_dist < 0: # prefer full left
                movements[(key1, key2)] = lateral + vertical + ["A"]
            else:
                movements[(key1, key2)] = vertical + lateral + ["A"]

    return movements

numeric_keypad = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["", "0", "A"]]
directional_keypad = [["", "^", "A"], ["<", "v", ">"]]

numeric_movements = assemble_movements(numeric_keypad)
directional_movements = assemble_movements(directional_keypad)

def part1(input_data):
    complexity_sum = 0
    for code in input_data:
        # numeric keypad robot
        input_tape = ["A"] + list(code)
        output_tape = []
        for i in range(len(input_tape) - 1):
            output_tape += numeric_movements[(input_tape[i], input_tape[i+1])]

        # 2 directional keypad robots
        for _ in range(2):
            input_tape = ["A"] + output_tape
            output_tape.clear()
            for i in range(len(input_tape) - 1):
                output_tape += directional_movements[(input_tape[i], input_tape[i+1])]

        complexity_sum += len(output_tape) * int("".join([char for char in code if char.isdigit()]))
        
    return complexity_sum

from functools import cache

@cache
def complexity(src, dst, depth):
    if depth == 0:
        return 1
    
    complexity_sum = 0
    path = ["A"] + directional_movements[(src, dst)]
    for i in range(len(path) - 1):
        complexity_sum += complexity(path[i], path[i+1], depth-1)

    return complexity_sum


def part2(input_data):
    complexity_sum = 0
    for code in input_data:
        # numeric keypad robot
        input_tape = ["A"] + list(code)
        output_tape = []
        for i in range(len(input_tape) - 1):
            output_tape += numeric_movements[(input_tape[i], input_tape[i+1])]

        # 25 directional keypad robots
        directional_tape = ["A"] + output_tape
        length = 0
        for i in range(len(directional_tape) - 1):
            length += complexity(directional_tape[i], directional_tape[i+1], 25)
        
        numeric = int("".join([char for char in code if char.isdigit()]))
        print(code, length)
        complexity_sum += length * numeric
    return complexity_sum
