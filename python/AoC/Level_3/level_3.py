import re


def read_file(file):
    with open(file, 'r') as f:
        return f.read()

def to_array(input):
    rows = input.strip().split('\n')
    char_matrix = [list(row) for row in rows]
    return char_matrix

def part_1(array):
    max_x=len(array)
    max_y=len(array[0])
    summe=0
    for x, row in enumerate(array):
        for y, c in enumerate(row):
            if not (c.isdigit() or c == '.'):
                numbers=list()
                for i in range(-1,2):
                    for j in range(-1,2):
                        if 0 <= x + i and x + i < max_x and 0 <= y + i and y + i < max_y:
                            if (re.search("[0-9]+", array[x + i][y + j])):
                                print()
                summe+=sum(numbers)

file_path = '.\level_3_test'
print(part_1(to_array(read_file(file_path))))
