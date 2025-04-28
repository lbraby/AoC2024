from aoc.utils import parsing

import heapq

input_parser = parsing.split_lines

def find_path(visited):
    path = [(70, 70)]

    node = (70, 70)
    while True:
        node = visited[node]
        path.append(node)
        if node == (0, 0):
            break

    return path[::-1]

def run_dijkstras(bytes, blocks_fallen):
    frontier = []
    visited = {}
    barriers = set(bytes[:blocks_fallen])

    heapq.heappush(frontier, (0, (0, 0), (0, 0)))
    while frontier:
        distance, target, source = heapq.heappop(frontier)

        if target in visited:
            continue

        visited[target] = source
        if target == (70, 70):
            return distance, find_path(visited)

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor = (target[0] + dx, target[1] + dy)
            if neighbor[0] < 0 or neighbor[0] > 70 or neighbor[1] < 0 or neighbor[1] > 70 or neighbor in barriers:
                continue

            heapq.heappush(frontier, (
                distance + 1, neighbor, target
            ))

    return None, None

def parse_input(input_data):
    bytes = [tuple(map(int, line.split(","))) for line in input_data]
    return bytes

def part1(input_data):
    bytes = parse_input(input_data)
    shortest_distance, shortest_path = run_dijkstras(bytes, 1024)
    return shortest_distance

def print_map(bytes, bytes_fallen, path_members):
    map = [['_']*71 for i in range(71)]

    for coordinate in bytes[:bytes_fallen]:
        map[coordinate[1]][coordinate[0]] = '.'
    
    for coordinate in path_members:
        map[coordinate[1]][coordinate[0]] = 'X'

    for i in range(len(map)):
        print("".join(map[i]))

def part2(input_data):
    bytes = parse_input(input_data)
    prev_bytes_fallen = 0
    bytes_fallen = 0

    while True:
        shortest_distance, shortest_path = run_dijkstras(bytes, bytes_fallen)
        if shortest_distance == None:
            left = prev_bytes_fallen
            right = bytes_fallen
            while left < right:
                mid = (left + right) // 2
                if run_dijkstras(bytes, mid)[0]:
                    left = mid + 1
                else:
                    bytes_fallen = mid
                    right = mid - 1

            return bytes[bytes_fallen-1]
        
        shortest_path_set = set(shortest_path)
        prev_bytes_fallen = bytes_fallen
        bytes_fallen = min([i for i in range(bytes_fallen+1, len(bytes)) if bytes[i] in shortest_path_set])

