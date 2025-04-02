from aoc.utils import parsing

input_parser = parsing.split_lines

def parse_input(input_data):
    warehouse = []
    movements = ""
    newline_encountered = False
    for line in input_data:
        if line == "":
            newline_encountered = True
        elif not newline_encountered:
            warehouse.append(list(line))
        else:
            movements += line
    
    return warehouse, movements

def locate_robot(warehouse):
    for y in range(len(warehouse)):
        for x in range(len(warehouse[0])):
            if warehouse[y][x] == "@":
                return (x, y)

def move_robot(warehouse, x, y, movement):
    match movement:
        case ">":
            if warehouse[y][x+1] == "." or (warehouse[y][x+1] == "O" and move_robot(warehouse, x+1, y, movement)[0] > x+1):
                warehouse[y][x+1] = warehouse[y][x]
                warehouse[y][x] = "."
                x += 1
        case "v":
            if warehouse[y+1][x] == "." or (warehouse[y+1][x] == "O" and move_robot(warehouse, x, y+1, movement)[1] > y+1):
                warehouse[y+1][x] = warehouse[y][x]
                warehouse[y][x] = "."
                y += 1
        case "<":
            if warehouse[y][x-1] == "." or (warehouse[y][x-1] == "O" and move_robot(warehouse, x-1, y, movement)[0] < x-1):
                warehouse[y][x-1] = warehouse[y][x]
                warehouse[y][x] = "."
                x -= 1
        case "^":
            if warehouse[y-1][x] == "." or (warehouse[y-1][x] == "O" and move_robot(warehouse, x, y-1, movement)[1] < y-1):
                warehouse[y-1][x] = warehouse[y][x]
                warehouse[y][x] = "."
                y -= 1

    return (x, y)

def calculate_gps_sum(warehouse, box_char="O"):
    sum = 0
    for y in range(len(warehouse)):
        for x in range(len(warehouse[0])):
            if warehouse[y][x] == box_char:
                sum += y*100 + x
    
    return sum

def part1(input_data):
    warehouse, movements = parse_input(input_data)
    
    x_pos, y_pos = locate_robot(warehouse)

    for movement in movements:
        x_pos, y_pos = move_robot(warehouse, x_pos, y_pos, movement)

    return calculate_gps_sum(warehouse)


# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣤⣤⣤⣤⣤⣤⣤⣴⣿⡇⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⣿⠿⠿⠟⠿⠿⠿⠛⠿⠿⢿⣿⣿⣿⣷⣽⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⠿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠿⠋⠁⠀⠀⠀⣷⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡆⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠘⠁⠀⠀⠀⠀⠀⠀⣿⣿⣿⣾⣿⣷⣶⣶⣤⣄⠀⠀⠀⠀⠀⠀⣿⡇⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡤⠀⠀⠀⠀⣿⡇⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣿⡇⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⢹⡇⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⣀⣿⡇⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣀⣿⣿⢷⡄
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣾⣿⣿⣭⣽⡇
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢽⣶⣿⡇
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⡏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⡆⠈⠙⠛⢿⡿⠟⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⣿⣿⣿⣯⣉⣉⣹⢿⢿⣯⣼⣧⠀⠻⣿⣾⡇⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⡿⣸⡎⢿⣿⣿⣆⠀⠀⣿⡇⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⡡⢴⣿⣿⣿⡆⠀⣿⠁⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣉⣿⣿⣿⣿⣿⣿⣿⣴⣿⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀
# ⣤⣤⣤⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀
# ⠈⠙⠛⠛⠻⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠛⠿⠿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⠛⠋⠁⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
################################################
# ⠀⠀⠀⠀⠀⠀     UGLY CODE LIES BELOW             #
################################################

def parse_input_pt2(input_data):
    warehouse = []
    movements = ""
    newline_encountered = False
    for line in input_data:
        if line == "":
            newline_encountered = True
        elif not newline_encountered:
            row = []
            for char in line:
                if char == "#" or char == ".": row += [char]*2
                elif char == "O": row += "[]"
                else: row += "@."
            warehouse.append(row)
        else:
            movements += line
    
    return warehouse, movements

def move_robot_pt2(warehouse, object_coords, movement):
    next_object_coords = set()

    if not object_coords: # no obstacles
        return 1

    match movement:
        case ">":
            x, y = object_coords[0]
            if warehouse[y][x] == "#":
                return 0
            elif warehouse[y][x] == ".":
                return 1
            else:
                mov = move_robot_pt2(warehouse, [(x+1, y)], movement)
                tile = warehouse[y][x]
                warehouse[y][x] = "."
                warehouse[y][x+mov] = tile
                if tile == "@":
                    return (x+mov, y)
                else:
                    return mov
        case "v":
            new_members = []
            for x, y in object_coords:
                if warehouse[y][x] == "#":
                    return 0
                elif warehouse[y][x] == "@":
                    mov = move_robot_pt2(warehouse, [(x, y+1)], movement)
                    warehouse[y][x] = "."
                    warehouse[y+mov][x] = "@"
                    return (x, y+mov)
                elif warehouse[y][x] == "[":
                   new_members.append((x+1, y))
                   next_object_coords.add((x, y+1))
                   next_object_coords.add((x+1, y+1))
                elif warehouse[y][x] == "]":
                    new_members.append((x-1, y))
                    next_object_coords.add((x, y+1))
                    next_object_coords.add((x-1, y+1))
            object_coords += new_members
                
            if move_robot_pt2(warehouse, list(next_object_coords), movement):
                for x, y in list(set(object_coords)):
                    if warehouse[y][x] == ".": continue
                    warehouse[y+1][x] = warehouse[y][x]
                    warehouse[y][x] = "."
                return 1
            else:
                return 0
        case "<":
            x, y = object_coords[0]
            if warehouse[y][x] == "#":
                return 0
            elif warehouse[y][x] == ".":
                return 1
            else:
                mov = move_robot_pt2(warehouse, [(x-1, y)], movement)
                tile = warehouse[y][x]
                warehouse[y][x] = "."
                warehouse[y][x-mov] = tile
                if tile == "@":
                    return (x-mov, y)
                else:
                    return mov
        case "^":
            new_members = []
            for x, y in object_coords:
                if warehouse[y][x] == "#":
                    return 0
                elif warehouse[y][x] == "@":
                    mov = move_robot_pt2(warehouse, [(x, y-1)], movement)
                    warehouse[y][x] = "."
                    warehouse[y-mov][x] = "@"
                    return (x, y-mov)
                elif warehouse[y][x] == "[":
                   new_members.append((x+1, y))
                   next_object_coords.add((x, y-1))
                   next_object_coords.add((x+1, y-1))
                elif warehouse[y][x] == "]":
                    new_members.append((x-1, y))
                    next_object_coords.add((x, y-1))
                    next_object_coords.add((x-1, y-1))
            object_coords += new_members
                
            if move_robot_pt2(warehouse, list(next_object_coords), movement):
                for x, y in list(set(object_coords)):
                    if warehouse[y][x] == ".": continue
                    warehouse[y-1][x] = warehouse[y][x]
                    warehouse[y][x] = "."
                return 1
            else:
                return 0

def part2(input_data):
    warehouse, movements = parse_input_pt2(input_data)
    
    x_pos, y_pos = locate_robot(warehouse)

    for movement in movements:
        x_pos, y_pos = move_robot_pt2(warehouse, [(x_pos, y_pos)], movement)
    
    return calculate_gps_sum(warehouse, box_char="[")
