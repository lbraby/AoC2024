from aoc.utils import parsing

input_parser = parsing.split_lines

def hike(level, x, y, trailends, levels):
    if level == 9:
        trailends.append((x, y))
        return
    
    else:
        if levels[y+1][x] == level+1: hike(level+1, x, y+1, trailends, levels)
        if levels[y-1][x] == level+1: hike(level+1, x, y-1, trailends, levels)
        if levels[y][x+1] == level+1: hike(level+1, x+1, y, trailends, levels)
        if levels[y][x-1] == level+1: hike(level+1, x-1, y, trailends, levels)


def part1(input_data):
    levels = [[-1]*(len(input_data[0])+2)] + [[-1] + [int(num) for num in line] + [-1] for line in input_data] + [[-1]*(len(input_data[0])+2)]
    sum = 0
    for r in range(1, len(levels)-1):
        for c in range(1, len(levels[r])-1):
            if levels[r][c] == 0: # trailhead
                trailends = []
                hike(0, c, r, trailends, levels)
                sum += len(set(trailends))

    return sum

def part2(input_data):
    levels = [[-1]*(len(input_data[0])+2)] + [[-1] + [int(num) for num in line] + [-1] for line in input_data] + [[-1]*(len(input_data[0])+2)]
    sum = 0
    for r in range(1, len(levels)-1):
        for c in range(1, len(levels[r])-1):
            if levels[r][c] == 0: # trailhead
                trailends = []
                hike(0, c, r, trailends, levels)
                sum += len(trailends)

    return sum
