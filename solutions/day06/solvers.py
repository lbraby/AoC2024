from aoc.utils import parsing
import time
import os

input_parser = parsing.split_lines

class Guard:
    def __init__(self, input_data, start_dir=2):
        self.tiles_visited = 0
        self.march_dir = start_dir # 0: S, 1: W, 2: N, 3: E
        self.lab_map = [list(row) for row in input_data]
        for i in range(len(self.lab_map)):
            for j in range(len(self.lab_map[0])):
                if self.lab_map[i][j] == "^":
                    self.x = j
                    self.y = i
                    return None
                
    def display_map(self):
        time.sleep(0.001)
        os.system('cls')

        for row in self.lab_map:
            print("".join(row))
                
    def march(self):
        if self.lab_map[self.y][self.x] != "X":
            self.lab_map[self.y][self.x] = "X"
            self.tiles_visited += 1
        next_x = self.x if self.march_dir % 2 == 0 else self.x + self.march_dir - 2
        next_y = self.y if self.march_dir % 2 == 1 else self.y + 1 - self.march_dir

        if next_y >= len(self.lab_map) or next_y < 0 or next_x >= len(self.lab_map[0]) or next_x < 0:
            return 0
        
        if self.lab_map[next_y][next_x] == "#":
            self.march_dir = (self.march_dir + 1) % 4
        else:
            self.x = next_x
            self.y = next_y

        return 1


def part1(input_data):
    guard = Guard(input_data)
    while guard.march():
        pass

    return guard.tiles_visited


class MultidimensionalGuard:
    def __init__(self, lab_map, start_dir=2, start_pos=None, visited=None):
        self.lab_map = lab_map
        self.march_dir = start_dir # 0: S, 1: W, 2: N, 3: E
        self.attemptedObstructions = set()
        self.obstructed = False
        if start_pos != None:
            self.x = start_pos[0]
            self.y = start_pos[1]
            self.visited = visited | {(self.x, self.y, self.march_dir)}
            return None
        
        for i in range(len(self.lab_map)):
            for j in range(len(self.lab_map[0])):
                if self.lab_map[i][j] == "^":
                    self.lab_map[i][j] = "."
                    self.x = j
                    self.y = i
                    self.visited = {(self.x, self.y, self.march_dir)}
                    return None
                
    def march(self):
        next_x = self.x if self.march_dir % 2 == 0 else self.x + self.march_dir - 2
        next_y = self.y if self.march_dir % 2 == 1 else self.y + 1 - self.march_dir

        if next_y >= len(self.lab_map) or next_y < 0 or next_x >= len(self.lab_map[0]) or next_x < 0:
            return 0
        
        if (next_x, next_y, self.march_dir) in self.visited:
            self.obstructed = True
            return 0

        if self.lab_map[next_y][next_x] == "#":
            self.march_dir = (self.march_dir + 1) % 4
        else:
            self.x = next_x
            self.y = next_y
            self.visited.add((self.x, self.y, self.march_dir))

        return 1
    
    def tryObstruction(self):
        next_x = self.x if self.march_dir % 2 == 0 else self.x + self.march_dir - 2
        next_y = self.y if self.march_dir % 2 == 1 else self.y + 1 - self.march_dir

        if next_y >= len(self.lab_map) or next_y < 0 or next_x >= len(self.lab_map[0]) or next_x < 0 or self.lab_map[next_y][next_x] == "#" or (next_x, next_y) in self.attemptedObstructions:
            return 0
        
        self.lab_map[next_y][next_x] = "#"
        self.attemptedObstructions.add((next_x, next_y))
        alternateGuard = MultidimensionalGuard(self.lab_map, self.march_dir, (self.x, self.y), self.visited)
        while alternateGuard.march():
            pass
        self.lab_map[next_y][next_x] = "."

        return alternateGuard.obstructed

def part2(input_data):
    lab_map = [list(row) for row in input_data]

    guard = MultidimensionalGuard(lab_map)
    successful_obstructions = 0

    while True:
        successful_obstructions += guard.tryObstruction()
        if not guard.march():
            break

    return successful_obstructions