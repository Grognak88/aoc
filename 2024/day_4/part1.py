import numpy as np
import re

with open(("input.txt")) as file:
    data = file.read().split("\n")
    data = [list(line) for line in data]

data = np.array(data)

diag_1 = [data.diagonal(i) for i in range(len(data[0]))]

diag_1_1 = [data.diagonal(-1 * i) for i in range(len(data)) if i > 0]

data_flipped = np.flip(data, 1)

diag_2 = [data_flipped.diagonal(i) for i in range(len(data_flipped[0]))]

diag_2_1 = [data_flipped.diagonal(-1 * i) for i in range(len(data_flipped)) if i > 0]


def pull_word(line):
    new_line = ""
    for i in line:
        new_line = new_line + i
    # print(new_line)
    return new_line

def counts_xmas(line):
    pattern = r"XMAS"
    found = re.findall(pattern, line)
    found_1 = re.findall(pattern, line[::-1])
    return len(found) + len(found_1)

counts_1 = [counts_xmas(pull_word(i)) for i in diag_1]
counts_1_1 = [counts_xmas(pull_word(i)) for i in diag_1_1]
counts_2 = [counts_xmas(pull_word(i)) for i in diag_2]
counts_2_1 = [counts_xmas(pull_word(i)) for i in diag_2_1]
counts_main = [counts_xmas(pull_word(i)) for i in data]
count_of_main = [counts_xmas(pull_word(i)) for i in np.transpose(data)]

print(sum(counts_1) + sum(counts_1_1) + sum(counts_2) + sum(counts_2_1) + sum(counts_main)+ sum(count_of_main))
### part 2

# Save positions as tuple
data_as_dict = {(i, j): data[i][j] for i in range(len(data)) for j in range(len(data[0]))}

#Directions
DIRECTIONS = [((1,1),(-1,-1)),((1,-1),(-1,1))]

def add_tuples(tuple1, tuple2):
    (a,b) = tuple1
    (c,d) = tuple2
    return (a+c, b+d)

def mas_in_diag(start, in_direction):
    word = ""
    
    (dir_a,dir_b) = in_direction

    for step in range(3):
        current_pos = add_tuples(start, (dir_a * step,dir_b * step))
        if current_pos not in data_as_dict:
            return False
        word += data_as_dict[current_pos]
    
    return word == "MAS" or word == "SAM"
        

def is_xmas_cross(pos):
    # Early exit if definitive false
    if data_as_dict[pos] != "A":
        return False
    
    found_word_pairs = 0
    for (point_a, point_b) in DIRECTIONS:
        starting_position = add_tuples(pos, point_a)
        if starting_position in data_as_dict and mas_in_diag(starting_position, point_b):
            found_word_pairs += 1
            if found_word_pairs == 2:
                return True
    return False

shape_count = sum(is_xmas_cross(x) for x in data_as_dict)
print(shape_count)