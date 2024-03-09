# Advent of Code - 2023 - day 6

import math


with open("input.txt") as input_file:
    input = input_file.read()


input = input.strip('\n').split('\n')

def solve_part_one(input: list[str]):
    times = input[0].split(':')[-1].strip().split(' ')
    times = [int(time.strip()) for time in times if time]
    records = input[1].split(':')[-1].strip().split(' ')
    records = [int(record.strip()) for record in records if record]

    res = 1
    for time, record in zip(times, records):
        d = time ** 2 - 4 * record 
        if d < 0:
            continue
        x1, x2 = (time - math.sqrt(d))/2, (time + math.sqrt(d))/2
        x1 = max(x1, 0)
        if x1 == math.ceil(x1):
            bot = x1 + 1
        else:
            bot = math.ceil(x1)

        if x2 == math.floor(x2):
            top = x2 - 1
        else:
            top = math.floor(x2)
        res *= int(top - bot + 1)
    
    print(res)
    return res

solve_part_one(input)

def solve_part_two(input: list[str]):
    times = input[0].split(':')[-1].strip().split(' ')
    time = int(''.join(times).strip())
    records = input[1].split(':')[-1].strip().split(' ')
    record = int(''.join(records).strip())

    d = time ** 2 - 4 * record 
    if d < 0:
        print(0)
        return 0
    x1, x2 = (time - math.sqrt(d))/2, (time + math.sqrt(d))/2
    x1 = max(x1, 0)
    if x1 == math.ceil(x1):
        bot = x1 + 1
    else:
        bot = math.ceil(x1)

    if x2 == math.floor(x2):
        top = x2 - 1
    else:
        top = math.floor(x2)
    res = int(top - bot + 1)
    
    print(res)
    return res

solve_part_two(input)
   
"""
max_time
record
Hold for x

distance = x*(max_time - x) has to be > record
-x^2 + x*max_time - record > 0

D = 4*record - max_time^2

x1, x2 = (-max_time +/- sqrt(4*record - max_time^2)) / (-2)

x1, x2 = max(x1, x2), min(x1, x2)
if x1 == math.floor(x1):
    top = x1 - 1
else:
    top = math.floor(x1)
    
if x2 == math.ceil(x2):
    bot = x2 + 1
else:
    bot = math.ceil(x2)
res = top - bot + 1
"""