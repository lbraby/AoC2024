from aoc.utils import parsing
import time, math, re, os

input_parser = parsing.split_lines

#################    NOTES    #################
# input is list of robot positions with velocities
# - robots wrap around edges of map
# map is 101 tiles wide, 103 tiles tall
# calculate number of robots in each quadrant after 100s

seconds = 100
width = 101
height = 103

def end_quadrant(position, velocity):
    end_position = ((position[0]+velocity[0]*seconds) % width, (position[1]+velocity[1]*seconds) % height)
    if end_position[0] > width // 2 and end_position[1] > height // 2:
        return 0
    elif end_position[0] > width // 2 and end_position[1] < height // 2:
        return 1
    elif end_position[0] < width // 2 and end_position[1] > height // 2:
        return 2
    elif end_position[0] < width // 2 and end_position[1] < height // 2:
        return 3
    else:
        return 4 # not in quadrant

def parse_line(line):
    pattern = "p=(\d+),(\d+) v=(-?\d+),(-?\d+)"
    match = re.search(pattern, line)
    return (int(match[1]), int(match[2])), (int(match[3]), int(match[4]))

def part1(input_data):
    quadrants = [0]*5

    for line in input_data:
        position, velocity = parse_line(line)
        quadrants[end_quadrant(position, velocity)] += 1

    return math.prod(quadrants[:4])

def print_grid(grid, seconds):
    time.sleep(1)
    os.system('cls')
    for line in grid:
        print("".join(line))
    print(f"seconds: {seconds}")

def check_tree(grid):
    blob_diam = 7
    for y in range(height-blob_diam):
        for x in range(width-blob_diam):
            if grid[y][x] == "*":
                good_blob = True
                for i in range(blob_diam**2):
                    if grid[y+i//blob_diam][x+i%blob_diam] != "*":
                        good_blob = False
                        break
                if good_blob: 
                    return True

    return False

def part2(input_data):
    robots = [parse_line(line) for line in input_data]
    seconds = 0
    while True:
        grid = [["."]*width for i in range(height)]
        for robot in robots:
            position, velocity = robot
            pos = ((position[0]+velocity[0]*seconds) % width, (position[1]+velocity[1]*seconds) % height)
            grid[pos[1]][pos[0]] = '*'
        if check_tree(grid):
            print_grid(grid, seconds)
            break

        seconds += 1
    
    return seconds
