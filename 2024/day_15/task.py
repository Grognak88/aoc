from math import ceil
from collections import defaultdict


with open("test.txt") as file:
    [map, moves] = file.read().split("\n\n")
    map = map.split("\n")
    dim_y = len(map) - 1
    dim_x = len(map[0]) - 1
    map_dict = defaultdict(set)
    for y, line in enumerate(map):
        for x, val in enumerate(line):
            map_dict[val].add((x+y*1j))
    moves = moves.replace('\n', '')


position_rob = map_dict['@'].pop()

MOVE_UP = (0-1j)
MOVE_DOWN = (0+1j)
MOVE_LEFT = (-1+0j)
MOVE_RIGHT = (1+0j)


for move in moves:
    match move:
        case "^":
            
        case "v":
            
        case "<":
            
        case ">":
            
print(position_rob)