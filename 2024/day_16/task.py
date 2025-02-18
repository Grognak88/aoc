import numpy as np
from dataclasses import dataclass, field
from typing import Any
import heapq

#filename = 'test2.txt'
filename = 'input.txt'

with open(filename) as fin:
    data = fin.readlines()

start_loc = np.array([0,0])
end_loc = start_loc

dirs = [np.array([0, 1]), np.array([1, 0]), np.array([0, -1]), np.array([-1, 0])]

np.set_printoptions(edgeitems=30, linewidth=100000)

visited = set()

for ridx, line in enumerate(data):
    for cidx, c in enumerate(line.strip()):
        match c:
            case '#':
                visited.add((0, ridx, cidx))
                visited.add((1, ridx, cidx))
                visited.add((2, ridx, cidx))
                visited.add((3, ridx, cidx))
            case '.':
                pass
            case 'S':
                start_loc = np.array([ridx, cidx])
            case 'E':
                end_loc = np.array([ridx, cidx])

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)
    path: Any=field(compare=False) # New field for part 2

curheap = [PrioritizedItem(cost, np.array([idx, start_loc[0], start_loc[1]]), [(start_loc[0], start_loc[1])]) for idx, cost in enumerate([0, 1000, 2000, 1000])] # Modified in part 2 to add initial path
heapq.heapify(curheap)

final = np.inf
tiles_on_path = set()
while len(curheap) > 0:
    cur_loc = heapq.heappop(curheap)
    visited.add((cur_loc.item[0], cur_loc.item[1], cur_loc.item[2]))
    if all(cur_loc.item[1:] == end_loc):
        final = cur_loc.priority
        # Part 1 solution originally exited here after finding first path to the end
        # Part 2 needs all solutions, so don't break--just add the traveled path to the set
        for tile in cur_loc.path:
            tiles_on_path.add(tile)
    # This conditional allows us to exit as soon as we pull a route that is longer than the shortest route from the queue, ending part 2
    if final < cur_loc.priority:
        break
    for dir, dir_idx, cost in zip(dirs, range(len(dirs)), np.roll(np.array([0, 1000, 2000, 1000]), cur_loc.item[0])):
        next_loc = cur_loc.item[1:] + dir
        if (dir_idx, next_loc[0], next_loc[1]) not in visited:
            # Below modified in part 2 to track traveled path
            new_path = cur_loc.path.copy()
            new_path.append((next_loc[0], next_loc[1]))
            heapq.heappush(curheap, PrioritizedItem(cur_loc.priority + cost + 1, np.array([dir_idx, next_loc[0], next_loc[1]]), new_path))

print(final)
print(len(tiles_on_path))