# Advent of Code - 2023 - day 9

def extrapolate(arr: list[int], reverse: bool = False) -> int:
    done = False
    if reverse:
        last_diffs = [arr[0]]
    else:
        last_diffs = [arr[-1]]
    c_seq = []
    p_seq = arr
    while not done:
        if len(p_seq) == 1:
            last_diffs.append(p_seq[0])
            done = True
        else:
            done = True
            diff = p_seq[1] - p_seq[0]
            for i in range(1, len(p_seq)):
                new_diff = p_seq[i] - p_seq[i-1]
                c_seq.append(new_diff)
                done = new_diff == diff
            if reverse:
                last_diffs.append(c_seq[0])
            else:
                last_diffs.append(c_seq[-1])
            p_seq = list(c_seq)
            c_seq = []

    if reverse:
        res = 0
        for i, x in enumerate(last_diffs):
            if not (i % 2):
                res += x
            else:
                res -= x
    else:
        res = sum(last_diffs)
    return res

def solve_part_one():
    with open("input.txt") as input_file:
        res = 0
        for line in input_file.readlines():
            arr = list(map(int, line.split(' ')))
            res += extrapolate(arr, reverse=False)
        print(res)
    return res

def solve_part_two():
    with open("input.txt") as input_file:
        res = 0
        for line in input_file.readlines():
            arr = list(map(int, line.split(' ')))
            res += extrapolate(arr, reverse=True)
        print(res)
    return res

solve_part_two()
