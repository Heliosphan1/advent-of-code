# Advent of Code - 2023 - day 1

with open("input.txt") as input_file:
    input = input_file.read()

input = input.split('\n')

def solve_part_one(input):
    total = 0
    for line in input:
        digits = [ch for ch in line if ch.isdigit()]
        if digits:
            total += int(f'{digits[0]}{digits[-1]}')
            
    print(total)
    return total

def solve_part_two(input):
    numbers = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    prefixes = set()
    for k in numbers:
        for i in range(len(k) - 1):
            prefixes.add(k[:i+1])
                    
    total = 0
    
    for line in input:
        digits = []
        text_digit = ''
        for ch in line:
            text_digit += ch
            if ch.isdigit():
                digits.append(ch)
                text_digit = ''
            elif text_digit in numbers:
                digits.append(numbers[text_digit])
                text_digit = ch
            elif text_digit not in prefixes:
                if text_digit[-2:] in prefixes:
                    text_digit = text_digit[-2:]
                elif text_digit[-1] in prefixes:
                    text_digit = text_digit[-1]
                else:
                    text_digit = ''
        
        if digits:
            total += int(f'{digits[0]}{digits[-1]}')
    print(total)
    return total   

solve_part_one(input)
solve_part_two(input)
