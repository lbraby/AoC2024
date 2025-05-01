from aoc.utils import parsing

input_parser = parsing.split_lines

# there is only one path through the maze without cheating
# therefore, we can find the distance of each point to the start and end

def unhacked_path(map):
    def find_start(map):
        for i in range(len(map)):
            for j in range(len(map[0])):
                if map[i][j] == "S":
                    return (i, j)
    
    path = [find_start(map)]
    src_y, src_x = None, None
    while map[path[-1][0]][path[-1][1]] != "E":
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dst_y, dst_x = path[-1][0] + i, path[-1][1] + j
            if map[dst_y][dst_x] != "#" and (dst_y, dst_x) != (src_y, src_x):
                src_y, src_x = path[-1]
                path.append((dst_y, dst_x))
                break
    
    return path

def part1(input_data):
    path = unhacked_path(input_data)
    distances = {} # node: (dst_to_start, dst_to_end)
    path_length = len(path)
    for i in range(path_length):
        distances[path[i]] = (1 + i, path_length - i)

    cheats = 0
    for y, x in path:
        for i, j in [(0, 2), (0, -2), (2, 0), (-2, 0)]:
            jmp_y, jmp_x = y+i, x+j
            if jmp_y > 0 and jmp_y < len(input_data) and jmp_x > 0 and jmp_x < len(input_data[0]):
                if input_data[jmp_y][jmp_x] != "#" and distances[(y, x)][0] + distances[(jmp_y, jmp_x)][1] + 1 <= path_length - 100:
                    cheats += 1

    return cheats

def part2(input_data):
    path = unhacked_path(input_data)
    distances = {} # node: (dst_to_start, dst_to_end)
    path_length = len(path)
    for i in range(path_length):
        distances[path[i]] = (1 + i, path_length - i)

    cheats = 0
    for i in range(len(path)):
        for j in range(i+101, len(path)):
            y, x = path[i]
            jmp_y, jmp_x = path[j]
            cheat_length = abs(jmp_y - y) + abs(jmp_x - x)
            if cheat_length <= 20 and distances[(y, x)][0] + distances[(jmp_y, jmp_x)][1] + cheat_length - 1 <= path_length - 100:
                cheats += 1

    return cheats
