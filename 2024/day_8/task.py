from collections import defaultdict
from itertools import combinations
from math import gcd

grid_locations = set()

data_grid = defaultdict(set)

with open("input.txt") as file:
    data = file.read().split("\n")
    data = [list(line) for line in data]


for y, line in enumerate(data):
    for x, val in enumerate(line):
        grid_locations.add((x + y * 1j))
        data_grid[val].add((x + y * 1j))

data_grid.pop(".", None)


def find_antinodes(find_lines):
    found = set()
    for _, val in data_grid.items():
        found |= calculate_locations_for_symbol(val, find_lines)
    return found


def calculate_locations_for_symbol(set_of_locations, find_lines):
    found = set()
    combinations_points = list(
        list(comb) for comb in combinations(list(set_of_locations), 2)
    )
    reversed_point = [combs[::-1] for combs in combinations_points]
    combinations_points.extend(reversed_point)
    for combination in combinations_points:
        for i, a in enumerate(combination):
            if i < len(combination) - 1:
                b = combination[i + 1]
                direction = a - b

                if find_lines:
                    greates_common_divisor = gcd(
                        int(direction.real), int(direction.imag)
                    )
                    factorized_dir = direction / greates_common_divisor
                    point = a
                    while point in grid_locations:
                        found.add(point)
                        point = point + factorized_dir
                else:
                    location = a + direction

                    if location in grid_locations:
                        found.add(location)
    return found


COUNT_ANTINODES = len(find_antinodes(False))

print(COUNT_ANTINODES)

COUNT_ANTINODES_LINE = len(find_antinodes(True))

print(COUNT_ANTINODES_LINE)
