from aoc.utils import parsing
from collections import defaultdict

input_parser = parsing.split_lines

# Stone Rules
# - 0 => 1
# - if even number of digits, split digits in half
# - else multiply num by 2024

def blink(stone, times_blinked, desired_blinks):
    if times_blinked == desired_blinks:
        return 1
    
    if stone == "0" or stone == "":
        return blink("1", times_blinked+1, desired_blinks)
    elif len(stone) % 2 == 0:
        stone1 = stone[:len(stone)//2]
        stone2 = stone[len(stone)//2:]
        return blink(stone1, times_blinked+1, desired_blinks) + blink(stone2.lstrip("0") if stone2[0] == "0" else stone2, times_blinked+1, desired_blinks)
    else:
        return blink(str(int(stone)*2024), times_blinked+1, desired_blinks)

def part1(input_data):
    stones = input_data[0].split()
    return sum([blink(stone, 0, 25) for stone in stones])

def blink_memoized(stone, blinks_remaining, past_blinks):
    if blinks_remaining == 0:
        return 1

    if (stone, blinks_remaining) in past_blinks:
        return past_blinks[(stone, blinks_remaining)]
    elif stone == "0" or stone == "":
        stones = blink_memoized("1", blinks_remaining-1, past_blinks)
    elif len(stone) % 2 == 0:
        stone1 = stone[:len(stone)//2]
        stone2 = stone[len(stone)//2:].lstrip("0")
        stones = blink_memoized(stone1, blinks_remaining-1, past_blinks) + blink_memoized(stone2, blinks_remaining-1, past_blinks)
    else:
        stones = blink_memoized(str(int(stone)*2024), blinks_remaining-1, past_blinks)
    
    past_blinks[(stone, blinks_remaining)] = stones # remember for later use
    return stones

def part2(input_data):
    stones = input_data[0].split()
    past_blinks = {}
    return sum([blink_memoized(stone, 75, past_blinks) for stone in stones])
