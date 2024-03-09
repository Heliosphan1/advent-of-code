# Advent of Code - 2023 - day 8
import asyncio

def solve_part_one():
    with open("input.txt") as input_file:
        path = input_file.readline().strip('\n')
        input_file.readline()
        
        route_map = dict() 
        for line in input_file.readlines():
            start, end = line.strip('\n').split(' = ')
            l, r = end.strip('()').split(', ')
            route_map[start] = (l, r)
        pos = 'AAA'
        steps = 0
        while pos != 'ZZZ':
            for direction in path:
                pos = route_map[pos][direction == 'R']
                steps += 1
                if pos == 'ZZZ':
                    print(steps)
                    return steps


def solve_part_two():
    with open("input.txt") as input_file:
        path = input_file.readline().strip('\n')
        input_file.readline()
        
        route_map = dict() 
        for line in input_file.readlines():
            start, end = line.strip('\n').split(' = ')
            l, r = end.strip('()').split(', ')
            route_map[start] = (l, r)
        nodes = []
        steps = 0

    for node in route_map:
        if node.endswith('A'):
            nodes.append(node)
    
    print(len(path))

    # done = False
    # while not done:
    #     for direction in path:
    #         done = True
    #         for i, node in enumerate(nodes):
    #             nodes[i] = route_map[node][direction == 'R']
    #             if not nodes[i].endswith('Z'):
    #                 done = False
    #         steps += 1
    #         if done:
    #             print(steps)
    #             return steps
    
 
        
        
solve_part_two()

