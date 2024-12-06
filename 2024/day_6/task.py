import math

with open("/home/onyxia/work/aoc/2024/day_6/input.txt") as file:
    data = file.read().split("\n")
    data = [list(line) for line in data]

# Save positions as tuple
data_as_dict = {i+j*1j: data[i][j] for i in range(len(data)) for j in range(len(data[0]))}


starting_point = 0

for point, marking in data_as_dict.items():
    if marking == "^":
        starting_point = point

def walk(kart):
    position, direction, seen = starting_point, -1, set()
    while position in kart and (position,direction) not in seen:
        seen.add((position,direction))
        if kart.get(position+direction) == "#":
            direction *= -1j
        else:
            position += direction
    return {pos for pos, _ in seen}, (position, direction) in seen

# print(list(dict.fromkeys(traversed_points)))

path,_ = walk(data_as_dict)
print(len(path), sum(walk(data_as_dict | {obs: "#"})[1] for obs in path))