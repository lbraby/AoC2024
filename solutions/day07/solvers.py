from aoc.utils import parsing

input_parser = parsing.split_lines

def test_equation(test_val, current_val, equation):
    if current_val > test_val:
        return 0
    
    if len(equation) == 0:
        if current_val == test_val: return 1
        else: return 0
    
    if test_equation(test_val, current_val+equation[0], equation[1:]) or test_equation(test_val, current_val*equation[0], equation[1:]):
        return 1

def part1(input_data):
    sum = 0
    for line in input_data:
        test_value = int(line.split(":")[0])
        equation = [int(val) for val in line.split(":")[1].split()]
        
        if test_equation(test_value, equation[0], equation[1:]):
            sum += test_value
    
    return sum


def test_equation2(test_val, current_val, equation):
    if current_val > test_val:
        return 0
    
    if len(equation) == 0:
        if current_val == test_val: return 1
        else: return 0
    
    if test_equation2(test_val, current_val+equation[0], equation[1:]) or test_equation2(test_val, current_val*equation[0], equation[1:]) or test_equation2(test_val, int(str(current_val)+str(equation[0])), equation[1:]):
        return 1

def part2(input_data):
    sum = 0
    for line in input_data:
        test_value = int(line.split(":")[0])
        equation = [int(val) for val in line.split(":")[1].split()]
        
        if test_equation2(test_value, equation[0], equation[1:]):
            sum += test_value
    
    return sum
