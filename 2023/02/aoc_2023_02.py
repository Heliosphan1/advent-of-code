# Advent of Code - 2023 - day 2
import math

with open("input.txt") as input_file:
    input = input_file.read()
    
input = input.split('\n')

def solve_part_one(input: list[str]):
    limit = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    possible = 0
    for line in input:
        game, draws = line.split(':')
        game_id = int(game.split(' ')[-1])
        for draw in draws.split(';'):
            draw = draw.strip()
            for cubes in draw.split(', '):
                number, color = cubes.split(' ')
                if int(number) > limit[color]:
                    break
            else:
                continue
            break
        else:
            possible += game_id
    print(possible)
    return possible

def solve_part_two(input: list[str]):

    res = 0
    for line in input:
        game, draws = line.split(':')
        min_cubes = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        for draw in draws.split(';'):
            draw = draw.strip()
            for cubes in draw.split(', '):
                number, color = cubes.split(' ')
                min_cubes[color] = max(min_cubes[color], int(number))
        res += math.prod(min_cubes.values())
                
    print(res)
    return res


solve_part_one(input)
solve_part_two(input)