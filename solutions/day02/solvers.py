from aoc.utils import parsing

input_parser = parsing.split_lines

def is_safe(levels):
    increasing = 1 if levels[0] < levels[1] else -1
    for i in range(0, len(levels) - 1):
        diff = levels[i + 1] - levels[i]

        if (abs(diff) > 3 or abs(diff) == 0) or diff * increasing < 0: # increase/decrease not gradual
            return 0
        
    return 1

def part1(input_data):
    safe_reports = 0

    for line in input_data:
        levels = list(map(int, line.strip().split()))

        safe_reports += is_safe(levels)
    
    return safe_reports


def part2(input_data):
    safe_reports = 0

    for line in input_data:
        levels = list(map(int, line.strip().split()))
        print(levels)
        if is_safe(levels):
            safe_reports += 1
        else:
            happened = False
            for i in range(len(levels)):
                tolerated_levels = levels[:i] + levels[i + 1:]
                if is_safe(tolerated_levels):
                    safe_reports += 1
                    happened = True
                    break
            if not happened: print("failed")
    
    return safe_reports