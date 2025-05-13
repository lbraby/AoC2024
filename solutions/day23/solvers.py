from aoc.utils import parsing

input_parser = parsing.split_lines

from collections import defaultdict

def assemble_graph(input_data):
    graph = defaultdict(set)
    for line in input_data:
        computer1, computer2 = line.split("-")
        graph[computer1].add(computer2)
        graph[computer2].add(computer1)

    return graph

def part1(input_data):
    # Count the number of cliques of size 3 containing 1+ computer starting with "t"
    graph = assemble_graph(input_data)

    clusters = set()
    seen1 = set()
    for computer1 in graph:
        if computer1[0] != "t": # only look for computers starting with t
            continue
        
        computer1_targets = graph[computer1] - seen1
        seen2 = set()
        for computer2 in computer1_targets:
            computer2_targets = graph[computer2] - seen1 - seen2
            for computer3 in (computer1_targets & computer2_targets):
                clusters.add((computer1, computer2, computer3))
            seen2.add(computer2)

        seen1.add(computer1)

    return len(clusters)

def form_clique(curr_clique, clique_targets, seen1, graph):
    seen2 = set()
    largest_clique = curr_clique
    for target in (clique_targets):
        if not curr_clique - graph[target]: # check if target connected to each computer in curr_clique
            new_clique = form_clique(curr_clique | {target}, graph[target] - seen1 - seen2, seen1|seen2, graph)
            if len(new_clique) > len(largest_clique):
                largest_clique = new_clique

        seen2.add(target)

    return largest_clique


def part2(input_data):
    # Find the largest clique
    graph = assemble_graph(input_data)

    largest_clique = set()
    seen = set()
    for computer in graph:
        clique = form_clique({computer}, graph[computer] - seen, seen, graph)
        if len(clique) > len(largest_clique):
            largest_clique = clique
        seen.add(computer)

    return ",".join(sorted(list(largest_clique)))