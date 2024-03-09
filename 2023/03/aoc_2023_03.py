# Advent of Code - 2023 - day 3

from collections import defaultdict

with open("input.txt") as input_file:
    input = input_file.read()
    
input = input.strip(' \n')

input = input.split('\n')

def solve_part_one(input: list[str]):
    res = 0
    for i, line in enumerate(input):
        current = ''
        for j, ch in enumerate(line):
            if ch.isdigit() and j < len(line) - 1:
                current += ch
                continue
            if j == len(line) - 1 and ch.isdigit():
                current += ch
                j += 1
            if current:
                start = j - len(current) - 1
                relevant = False
                if (j < len(line) and line[j] != '.') or (start >= 0 and line[start] != '.'):
                    relevant = True
                else:           
                    for k in range(max(0, start), min(j+1, len(line))):
                        if i - 1 >= 0:
                            if input[i-1][k] != '.' and not input[i-1][k].isdigit():
                                relevant = True
                                break
                        if i + 1 <= len(input) - 1:
                            if input[i+1][k] != '.' and not input[i+1][k].isdigit():
                                relevant = True
                                break
                
                if relevant:
                    res += int(current)
                current = ''
    print(res)
    return res

def solve_part_two(input: list[str]):
    res = 0
    star_locations = {}
    for i, line in enumerate(input):
        current = ''
        for j, ch in enumerate(line):
            if ch.isdigit() and j < len(line) - 1:
                current += ch
                continue
            if j == len(line) - 1 and ch.isdigit():
                current += ch
                j += 1
            if current:
                start = j - len(current) - 1
                current = int(current)
                if (j < len(line) and line[j] == '*'):
                    if (i, j) in star_locations:
                        star_locations[(i, j)][0] += 1
                        star_locations[(i, j)][1] *= current
                    else:
                        star_locations[(i, j)] = [1, current]
                if (start >= 0 and line[start] == '*'):
                    if (i, start) in star_locations:
                        star_locations[(i, start)][0] += 1
                        star_locations[(i, start)][1] *= current
                    else:
                        star_locations[(i, start)] = [1, current]
                for k in range(max(0, start), min(j+1, len(line))):
                    if i - 1 >= 0:
                        if input[i-1][k] == '*':
                            if (i-1, k) in star_locations:
                                star_locations[(i-1, k)][0] += 1
                                star_locations[(i-1, k)][1] *= current
                            else:
                                star_locations[(i-1, k)] = [1, current]
                    if i + 1 <= len(input) - 1:
                        if input[i+1][k] == '*':
                            if (i+1, k) in star_locations:
                                star_locations[(i+1, k)][0] += 1
                                star_locations[(i+1, k)][1] *= current
                            else:
                                star_locations[(i+1, k)] = [1, current]
                current = ''
    for count, product in star_locations.values():
        if count == 2:
            res += product
    
    print(res)
    return(res)



solve_part_two(input)