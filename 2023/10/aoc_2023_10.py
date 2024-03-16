# Advent of Code - 2023 - day 10
   

field = []
with open("input.txt") as input_file:
    for i, line in enumerate(input_file.readlines()):
        pos = line.find('S')
        if pos >= 0:
            start = (pos, i)
        field.append(line.strip('\n'))

dim_x = len(field[0]) - 1
dim_y = len(field) - 1

pipe_path = {
    (1, 0): {
        'J': (0, -1),
        '7': (0, 1),
        '-': (1, 0)
    },
    (-1, 0): {
        'F': (0, 1),
        'L': (0, -1),
        '-': (-1, 0)
    },
    (0, 1): {
        'J': (-1, 0),
        'L': (1, 0),
        '|': (0, 1) 
    },
    (0, -1): {
        'F': (1, 0),
        '7': (-1, 0),
        '|': (0, -1)
    }
}

def search_first(node):
    x, y = node
    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        x1, y1 = x + dx, y + dy
        if (0 <= x1 <= dim_x) and (0 <= y1 <= dim_y) and (field[y1][x1] in pipe_path[(dx, dy)]):
                return (x1, y1)
            
def search_next(node, prev_node):
    x, y = node
    x0, y0 = prev_node
    dx, dy = x - x0, y - y0
    dx1, dy1 = pipe_path[(dx, dy)][field[y][x]]
    return (x + dx1, y + dy1)

steps = 1
on_path = set(start)
prev_node = start
node = search_first(start)
while True:
    on_path.add(node)
    next_node = search_next(node, prev_node)
    if field[next_node[1]][next_node[0]] == 'S':
        break
    else:
        steps += 1
        prev_node = node
        node = next_node
        
part1_ans = steps//2 + steps % 2 
print(steps//2 + steps % 2)
