from aoc.utils import parsing

import heapq
from collections import defaultdict

input_parser = parsing.split_lines

# find path with lowest score (Dijkstra's Algorithm)
# move forward = 1 point, 90 degree turn = 1000 points

def add_distances(i, j, maze, distances):
    # rotations
    distances[(i, j, "N")][(i, j, "E")] = 1000
    distances[(i, j, "N")][(i, j, "W")] = 1000
    distances[(i, j, "E")][(i, j, "S")] = 1000
    distances[(i, j, "E")][(i, j, "N")] = 1000
    distances[(i, j, "S")][(i, j, "E")] = 1000
    distances[(i, j, "S")][(i, j, "W")] = 1000
    distances[(i, j, "W")][(i, j, "S")] = 1000
    distances[(i, j, "W")][(i, j, "N")] = 1000

    # movements
    if maze[i][j+1] != "#":
        distances[(i, j, "E")][(i, j+1, "E")] = 1
    if maze[i][j-1] != "#":
        distances[(i, j, "W")][(i, j-1, "W")] = 1
    if maze[i+1][j] != "#":
        distances[(i, j, "S")][(i+1, j, "S")] = 1
    if maze[i-1][j] != "#":
        distances[(i, j, "N")][(i-1, j, "N")] = 1

def setup_algorithm(maze):
    distances = defaultdict(dict)
    start = None
    end = None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "E":
                end = set([(i, j, "N"), (i, j, "E"), (i, j, "S"), (i, j, "W")])
            elif maze[i][j] == "S":
                start = (i, j, "E")

            if maze[i][j] != "#":
                add_distances(i, j, maze, distances)

    return start, end, distances

def run_dijkstras(start, graph):
    frontier = []
    visited = {}

    heapq.heappush(frontier, (0, start, start))
    while frontier:
        distance, target, source = heapq.heappop(frontier)

        if target in visited:
            continue

        visited[target] = (source, distance)

        for neighbor, weight in graph[target].items():
            heapq.heappush(frontier, (
                weight + distance, neighbor, target
            ))
    
    return visited

def part1(input_data):
    start, end, graph = setup_algorithm(input_data)
    visited = run_dijkstras(start, graph)

    lowest_score = float("inf")
    for end_orientation in end:
        if visited[end_orientation][1] < lowest_score: 
            lowest_score = visited[end_orientation][1]
    
    return lowest_score

def run_dijkstras_all_paths(start, graph):
    frontier = []
    visited = {}

    heapq.heappush(frontier, (0, start, start))
    while frontier:
        distance, target, source = heapq.heappop(frontier)

        if target not in visited:
            visited[target] = [(source, distance)]
        else:
            if distance == visited[target][0][1]:
                visited[target].append((source, distance))
            continue

        for neighbor, weight in graph[target].items():
            heapq.heappush(frontier, (
                weight + distance, neighbor, target
            ))
    
    return visited

def part2(input_data):
    start, end, graph = setup_algorithm(input_data)
    visited = run_dijkstras_all_paths(start, graph)
    # print(visited)

    shortest_paths_nodes = set()
    nodes_list = list(end)
    while nodes_list:
        source = nodes_list.pop()
        nodes_list += [item[0] for item in visited[source] if item[0] not in shortest_paths_nodes]
        shortest_paths_nodes.add(source)

    shortest_paths_nodes = set([node[:2] for node in shortest_paths_nodes])

    return len(shortest_paths_nodes)
