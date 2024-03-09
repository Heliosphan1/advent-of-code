# Advent of Code - 2023 - day 4

with open("input.txt") as input_file:
    input = input_file.read()
    
input = input.strip('\n')
input = input.split('\n')

def solve_part_one(input: list[str]):
    points = 0
    for line in input:
        count = 0
        winning_numbers, own_numbers = line.split(': ')[-1].split(' | ')
        winning_numbers = set(winning_numbers.split(' '))
        own_numbers = own_numbers.split(' ')
        for number in own_numbers:
            if number and (number in winning_numbers):
                count += 1
        if count > 0:
            points += 2**(count-1)

    print(points)
    return points

def solve_part_two(input: list[str]):
    total_cards = [1] * len(input)
    for i, line in enumerate(input):
        count = 0
        winning_numbers, own_numbers = line.split(': ')[-1].split(' | ')
        winning_numbers = set(winning_numbers.split(' '))
        own_numbers = own_numbers.split(' ')
        for number in own_numbers:
            if number and (number in winning_numbers):
                count += 1
                total_cards[i+count] += total_cards[i]
    
    print(sum(total_cards))
    return (sum(total_cards))

solve_part_two(input)
