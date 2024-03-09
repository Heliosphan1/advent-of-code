import os

def remove_tags(line: str) -> str:
    start = None
    new_line = []
    for ch in line:
        if ch == '<':
            start = ch
        if not start:
            new_line.append(ch)
        if ch == '>':
            start = None
    return ''.join(new_line)


def main():
    for item in os.listdir():
        if item.startswith('20'):
            for l2_item in os.listdir(item):
                desc = os.path.join(item, l2_item, 'description.html')
                new_desc = os.path.join(item, l2_item, 'description.txt')
                try:
                    with open(desc, 'r') as in_file, open(new_desc, 'w') as out_file:
                        line = in_file.readline()
                        header_end = line.find('</h2>')
                        line = line[:header_end + 5] + '\n' + line[header_end + 5:]
                        line = remove_tags(line)
                        out_file.write(line)
                        for line in in_file.readlines():
                            out_file.write(remove_tags(line))
                    os.remove(desc)
                except FileNotFoundError:
                    continue
                


if __name__ == '__main__':
    main()
