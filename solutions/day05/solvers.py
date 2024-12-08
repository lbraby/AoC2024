from aoc.utils import parsing

input_parser = parsing.split_lines

def process_input(input_data):
    followers_map = {}
    for i in range(len(input_data)):
        if input_data[i] == "": break # end of section

        nums = list(map(int, input_data[i].split("|")))
        if nums[0] in followers_map:
            followers_map[nums[0]].add(nums[1])
        else:
            followers_map[nums[0]] = {nums[1]}
    return followers_map, [list(map(int, update.split(","))) for update in input_data[i+1:]]

def is_valid(update, followers_map):
    seen = {update[0]}
    for page in update[1:]:
        if not seen.isdisjoint(followers_map.get(page, set())):
            return False
        seen.add(page)
        
    return True

def part1(input_data):
    followers_map, updates = process_input(input_data)
    return sum([update[len(update)//2] if is_valid(update, followers_map) else 0 for update in updates])


def merge(left_pages, right_pages, followers_map):
    left_i = right_i = 0

    pages_v2 = []
    while left_i < len(left_pages) and right_i < len(right_pages):
        if right_pages[right_i] in followers_map.get(left_pages[left_i], set()): # right follows left
            pages_v2.append(left_pages[left_i])
            left_i += 1
        else:
            pages_v2.append(right_pages[right_i])
            right_i += 1

    return pages_v2 + left_pages[left_i:] + right_pages[right_i:]

def merge_sort(pages, followers_map):
    if len(pages) > 1:
        med = len(pages) // 2
        left = merge_sort(pages[:med], followers_map)
        right = merge_sort(pages[med:], followers_map)
        pages = merge(left, right, followers_map)
    
    return pages

def part2(input_data):
    sum_invalid_med_vals = 0
    followers_map, updates = process_input(input_data)
    for update in updates:
        if is_valid(update, followers_map):
            continue

        update_v2 = merge_sort(update, followers_map)
        sum_invalid_med_vals += update_v2[len(update_v2)//2]

    return sum_invalid_med_vals
