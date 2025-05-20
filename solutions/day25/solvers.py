from aoc.utils import parsing

input_parser = parsing.split_lines

def parse_schematics(input_data):
    schematics = {"keys": [], "locks": []}

    for i in range(0, len(input_data), 8):
        lengths = tuple(len([input_data[j][k] for j in range(i+1, i+6) if input_data[j][k] == "#"]) for k in range(5))

        if input_data[i] == "#####": # key
           schematics["keys"].append(lengths)
        elif input_data[i] == ".....": #lock
            schematics["locks"].append(lengths)

    return schematics
def part1(input_data):
    unique_fits = 0
    schematics = parse_schematics(input_data)
    for key in schematics["keys"]:
        for lock in schematics["locks"]:
            if key[0] + lock[0] <= 5 and key[1] + lock[1] <= 5 and key[2] + lock[2] <= 5 and key[3] + lock[3] <= 5 and key[4] + lock[4] <= 5:
                unique_fits += 1

    return unique_fits

def part2(input_data):
    return "Delivered the Chronicle"
