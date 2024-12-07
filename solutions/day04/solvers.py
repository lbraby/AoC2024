from aoc.utils import parsing

input_parser = parsing.split_lines

def part1(input):
    width = len(input[0])
    height = len(input)
    xmases_found = 0
    for i in range(len(input)):
        for j in range(len(input[0])):
            # Xs or Ss trigger search of neighbors
            if input[i][j] not in "XS":
                continue

            amxmas = "MAS" if input[i][j] == "X" else "AMX"
            if j < height-3 and input[i][j+1:j+4] == amxmas:
                xmases_found += 1
            if i < width-3 and j < height-3 and input[i+1][j+1] + input[i+2][j+2] + input[i+3][j+3] == amxmas:
                xmases_found += 1
            if i < width-3 and input[i+1][j] + input[i+2][j] + input[i+3][j] == amxmas:
                xmases_found += 1
            if i > 2 and j < height-3 and input[i-1][j+1] + input[i-2][j+2] + input[i-3][j+3] == amxmas:
                xmases_found += 1

    return xmases_found


def part2(input):
    width = len(input[0])
    height = len(input)
    xmases_found = 0
    for i in range(1, len(input)-1):
        for j in range(1, len(input[0])-1):
            # A triggers search for MAS X
            
            if input[i][j] != "A" or set(input[i-1][j-1] + input[i+1][j+1]) != set("MS") or set(input[i+1][j-1] + input[i-1][j+1]) != set("MS"):
                continue

            xmases_found += 1

    return xmases_found
