from aoc.utils import parsing
from collections import defaultdict

input_parser = parsing.split_lines

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, obj):
        if not isinstance(obj, Point):
            raise TypeError(f"Cannot add Point with {type(obj).__name__}")
        return Point(self.x + obj.x, self.y + obj.y)
    
    def __sub__(self, obj):
        if not isinstance(obj, Point):
            raise TypeError(f"Cannot add Point with {type(obj).__name__}")
        return Point(self.x - obj.x, self.y - obj.y)

def locate_anodes(input_data, nodes):
    anodes = set()
    width, height = len(input_data[0]), len(input_data)
    for n_type in nodes:
        for i in range(len(nodes[n_type]) - 1):
            for j in range(i+1, len(nodes[n_type])):
                p1 = Point(nodes[n_type][i][0], nodes[n_type][i][1])
                p2 = Point(nodes[n_type][j][0], nodes[n_type][j][1])
                
                anode1 = p1+p1-p2
                if anode1.x >= 0 and anode1.x < width and anode1.y >= 0 and anode1.y < height: 
                    anodes.add(str(anode1))
                anode2 = p2+p2-p1
                if anode2.x >= 0 and anode2.x < width and anode2.y >= 0 and anode2.y < height:
                    anodes.add(str(anode2))
    
    return anodes
                
def part1(input_data):
    nodes = defaultdict(list)
    for i in range(len(input_data)):
        for j in range(len(input_data[0])):
            if input_data[i][j] != ".":
                nodes[input_data[i][j]].append((i,j))

    anodes = locate_anodes(input_data, nodes)
    return len(anodes)

def locate_anodes_v2(input_data, nodes):
    anodes = set()
    width, height = len(input_data[0]), len(input_data)
    for n_type in nodes:
        for i in range(len(nodes[n_type]) - 1):
            for j in range(i+1, len(nodes[n_type])):
                p1 = Point(nodes[n_type][i][0], nodes[n_type][i][1])
                p2 = Point(nodes[n_type][j][0], nodes[n_type][j][1])
                
                anode1 = p1
                while True:
                    if anode1.x >= 0 and anode1.x < width and anode1.y >= 0 and anode1.y < height: 
                        anodes.add(str(anode1))
                    else: break

                    anode1 += p1-p2
                
                anode2 = p2
                while True:
                    if anode2.x >= 0 and anode2.x < width and anode2.y >= 0 and anode2.y < height: 
                        anodes.add(str(anode2))
                    else: break

                    anode2 += p2-p1
    
    return anodes

def part2(input_data):
    nodes = defaultdict(list)
    for i in range(len(input_data)):
        for j in range(len(input_data[0])):
            if input_data[i][j] != ".":
                nodes[input_data[i][j]].append((i,j))

    anodes = locate_anodes_v2(input_data, nodes)
    return len(anodes)
