# Advent of Code - 2023 - day 5


def solve_part_one(input: str):
    with open(input) as input_file:
        data = list(map(int, input_file.readline().rstrip('\n').split(': ')[-1].split(' ')))
        after_map = [0] * len(data)
        mapped = [False] * len(data)
        input_file.readline()
        while True:
            line = input_file.readline()
            if 'map' in line:
                line = input_file.readline()
                while line != '\n':
                    if not line:
                        break
                    dest_start, source_start, range_len = list(map(int, line.rstrip('\n').split(' ')))
                    line = input_file.readline()
                    for i, item in enumerate(data):
                        if (not mapped[i]) and (source_start <= item < source_start + range_len):
                            after_map[i] = dest_start + (item - source_start)
                            mapped[i] = True
                for i, item in enumerate(data):
                    if not mapped[i]:
                        after_map[i] = item
                data = after_map.copy()
                mapped = [False] * len(data)
                after_map = [0] * len(data)
                if not line:
                    break
    print(data)
    print(min(data))
    return min(data)

def solve_part_two(input: str):
    with open(input) as input_file:
        data = list(map(int, input_file.readline().rstrip('\n').split(': ')[-1].split(' ')))


    return min(data)

solve_part_one('input.txt')

