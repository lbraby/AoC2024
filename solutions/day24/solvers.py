from aoc.utils import parsing

input_parser = parsing.split_lines

def read_input(input_data):
    wire_values = {}
    gated_wires = {}
    break_seen = False
    for line in input_data:
        if line == "":
            break_seen = True
        elif not break_seen:
            wire, value = line.split(": ")
            wire_values[wire] = int(value)
        else:
            gate, wire = line.split(" -> ")
            gated_wires[wire] = tuple(gate.split(" "))

    return wire_values, gated_wires

def perform_operation(wire1, operator, wire2, wire_values, gated_wires):
    if wire1 not in wire_values:
        wire_values[wire1] = perform_operation(*gated_wires[wire1], wire_values, gated_wires)
    if wire2 not in wire_values:
        wire_values[wire2] = perform_operation(*gated_wires[wire2], wire_values, gated_wires)

    if operator == "AND":
        return wire_values[wire1] & wire_values[wire2]
    elif operator == "OR":
        return wire_values[wire1] | wire_values[wire2]
    else:
        return wire_values[wire1] ^ wire_values[wire2]

def calculate_number(wire_values, gated_wires):
    number = 0
    for i, wire in enumerate([f"z{n:02}" for n in range(0, 46)]):
        if wire not in wire_values:
            wire_values[wire] = perform_operation(*gated_wires[wire], wire_values, gated_wires)
        
        number += wire_values[wire] << i

    return number

def part1(input_data):
    wire_values, gated_wires = read_input(input_data)
    return calculate_number(wire_values, gated_wires)


def part2(input_data): # skipped (used this for solution: https://github.com/nitekat1124/advent-of-code-2024/blob/main/solutions/day24.py)
    pass