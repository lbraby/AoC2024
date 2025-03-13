from aoc.utils import parsing

input_parser = parsing.split_lines

def search(input_data, i, j, plant, plot_num):
    input_data[i][j] = plot_num
    area = 1
    perimiter = 0

    if i > 0: # search N
        if input_data[i-1][j] == plant:
            res_area, res_perim = search(input_data, i-1, j, plant, plot_num)
            area += res_area; perimiter += res_perim
        elif input_data[i-1][j] == plot_num: pass
        else: perimiter += 1
    else: perimiter += 1

    if i < len(input_data) - 1: # search S
        if input_data[i+1][j] == plant:
            res_area, res_perim = search(input_data, i+1, j, plant, plot_num)
            area += res_area; perimiter += res_perim
        elif input_data[i+1][j] == plot_num: pass
        else: perimiter += 1
    else: perimiter += 1

    if j > 0: # search W
        if input_data[i][j-1] == plant:
            res_area, res_perim = search(input_data, i, j-1, plant, plot_num)
            area += res_area; perimiter += res_perim
        elif input_data[i][j-1] == plot_num: pass
        else: perimiter += 1
    else: perimiter += 1

    if j < len(input_data[0]) - 1: # search E
        if input_data[i][j+1] == plant:
            res_area, res_perim = search(input_data, i, j+1, plant, plot_num)
            area += res_area; perimiter += res_perim
        elif input_data[i][j+1] == plot_num: pass
        else: perimiter += 1
    else: perimiter += 1

    return area, perimiter

def part1(input_data):
    input_data = [list(line) for line in input_data]
    plots = {}
    plot_num = 0
    for i in range(len(input_data)):
        for j in range(len(input_data[0])):
            if not isinstance(input_data[i][j], int):
                area, perimiter = search(input_data, i, j, input_data[i][j], plot_num)
                plots[plot_num] = (area, perimiter)
                plot_num += 1

    return sum([res[0]*res[1] for res in plots.values()])


def search_corners(input_data, i, j, plant, plot_num):
    input_data[i][j] = plot_num
    group = {plant, plot_num}
    area = 1
    corners = 0

    if i > 0 and j > 0 and input_data[i-1][j] in group and input_data[i][j-1] in group and input_data[i-1][j-1] not in group:   
        corners += 1
    elif ((i > 0 and input_data[i-1][j] not in group) or i == 0) and ((j > 0 and input_data[i][j-1] not in group) or j == 0):
        corners += 1

    if i > 0 and j < len(input_data[0]) - 1 and input_data[i-1][j] in group and input_data[i][j+1] in group and input_data[i-1][j+1] not in group:
        corners += 1
    elif ((i > 0 and input_data[i-1][j] not in group) or i == 0) and ((j < len(input_data[0]) - 1 and input_data[i][j+1] not in group) or j == len(input_data[0]) - 1):
        corners += 1

    if i < len(input_data) - 1 and j > 0 and input_data[i+1][j] in group and input_data[i][j-1] in group and input_data[i+1][j-1] not in group:
        corners += 1
    elif ((i < len(input_data) - 1 and input_data[i+1][j] not in group) or i == len(input_data) - 1) and ((j > 0 and input_data[i][j-1] not in group) or j == 0):
        corners += 1

    if i < len(input_data) - 1 and j < len(input_data[0]) - 1 and input_data[i+1][j] in group and input_data[i][j+1] in group and input_data[i+1][j+1] not in group:
        corners += 1
    elif ((i < len(input_data) - 1 and input_data[i+1][j] not in group) or i == len(input_data) - 1) and ((j < len(input_data[0]) - 1 and input_data[i][j+1] not in group) or j == len(input_data[0]) - 1):
        corners += 1

    print((i, j), corners, area)

    if i > 0 and input_data[i-1][j] == plant:# search N
        res_area, res_corners = search_corners(input_data, i-1, j, plant, plot_num)
        area += res_area; corners += res_corners
    if i < len(input_data) - 1 and input_data[i+1][j] == plant: # search S
            res_area, res_corners = search_corners(input_data, i+1, j, plant, plot_num)
            area += res_area; corners += res_corners
    if j > 0 and input_data[i][j-1] == plant: # search W
            res_area, res_corners = search_corners(input_data, i, j-1, plant, plot_num)
            area += res_area; corners += res_corners
    if j < len(input_data[0]) - 1 and input_data[i][j+1] == plant: # search E
            res_area, res_corners = search_corners(input_data, i, j+1, plant, plot_num)
            area += res_area; corners += res_corners

    return area, corners


def part2(input_data):
    # important realization: # sides = # corners
    input_data = [list(line) for line in input_data]
    plots = {}
    plot_num = 0
    for i in range(len(input_data)):
        for j in range(len(input_data[0])):
            if not isinstance(input_data[i][j], int):
                area, corners = search_corners(input_data, i, j, input_data[i][j], plot_num)
                print(plot_num, corners, area)
                plots[plot_num] = (area, corners)
                plot_num += 1

    return sum([res[0]*res[1] for res in plots.values()])
