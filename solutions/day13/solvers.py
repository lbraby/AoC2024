from aoc.utils import parsing
import re

input_parser = parsing.split_lines

def calculate_min_tokens(x_eq, y_eq, part2=False):
    if part2:
        x_eq[2] += 10000000000000
        y_eq[2] += 10000000000000

    scale = y_eq[0]/x_eq[0]
    b_clicks = round( (y_eq[2] - x_eq[2]*scale) / (y_eq[1] - x_eq[1]*scale) )
    a_clicks = round((x_eq[2] - x_eq[1]*b_clicks) / x_eq[0])

    if (not part2 and (b_clicks > 100 or a_clicks > 100)) or (a_clicks*x_eq[0] + b_clicks*x_eq[1] != x_eq[2]) or (a_clicks*y_eq[0] + b_clicks*y_eq[1] != y_eq[2]):
        return 0
    
    return 3*a_clicks + b_clicks

# 3 tokens for each A press, 1 token for each B press
# 100 presses is max for each button
def part1(input_data):
    tokens = 0
    for i, line in enumerate(input_data):
        match i % 4:
            case 0:
                a_mov = list(map(int, re.findall("\d+", line)))
            case 1:
                b_mov = list(map(int, re.findall("\d+", line)))
            case 2:
                prize = list(map(int, re.findall("\d+", line)))
            case 3:
                # tokens += calculate_min_tokens(a_mov, b_mov, prize)
                tokens += calculate_min_tokens([a_mov[0], b_mov[0], prize[0]], [a_mov[1], b_mov[1], prize[1]])
    
    return tokens

def part2(input_data):
    tokens = 0
    for i, line in enumerate(input_data):
        match i % 4:
            case 0:
                a_mov = list(map(int, re.findall("\d+", line)))
            case 1:
                b_mov = list(map(int, re.findall("\d+", line)))
            case 2:
                prize = list(map(int, re.findall("\d+", line)))
                tokens += calculate_min_tokens([a_mov[0], b_mov[0], prize[0]], [a_mov[1], b_mov[1], prize[1]], True)
            case 3:
                pass
    
    return tokens
