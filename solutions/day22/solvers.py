from aoc.utils import parsing

from collections import defaultdict

input_parser = parsing.split_lines

def evolve_number(number):
    number = ((number * 64) ^ number) % 16777216
    number = ((number // 32) ^ number) % 16777216
    number =  ((number * 2048) ^ number) % 16777216
    return number

def part1(input_data):
    sum_2000ths = 0

    for number in map(int, input_data):
        secret = number
        for _ in range(2000):
            secret = evolve_number(secret)

        sum_2000ths += secret

    return sum_2000ths

def calculate_sales(number, generations, banana_map):
    changes = [None] * generations
    prices = [None] * generations
    prices[0] = number % 10

    seen_sequences = set()
    for i in range(1, generations):
        number = evolve_number(number)
        prices[i] = number % 10
        changes[i] = prices[i] - prices[i-1]
        if i > 3:
            sequence = tuple(changes[i-3:i+1])
            if sequence not in seen_sequences:
                seen_sequences.add(sequence)
                banana_map[sequence] += prices[i]

def part2(input_data):
    banana_map = defaultdict(int)
    for number in map(int, input_data):
        calculate_sales(number, 2001, banana_map)

    return max(banana_map.values())
