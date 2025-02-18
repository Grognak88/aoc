import re

with open("input.txt") as file:
    data = file.read().split("\n")

list_of_positions = []
grid = [[0 for _ in range(101)] for _ in range(103)]

for line in data:
    p = r"([-+]?[0-9]+)"
    match = re.findall(p, line)
    bot = {"pos": (int(match[0]), int(match[1])), "velocity": (int(match[2]), int(match[3]))}
    grid[bot['pos'][1]][bot['pos'][0]] += 1
    list_of_positions.append(bot)

def add_tuples(tup1, tup2):
    return tup1[0]+tup2[0], tup1[1]+tup2[1]

def symbol(num):
    return 0 if num else 1
     
def print_grid(iter):
    import matplotlib.pyplot as plt

    plot = plt.imshow(grid, cmap='hot', interpolation='nearest')
    plt.savefig(f"{iter}.png")
    plt.clf()
    


def simulate_step(test, iter):
    grid_length_x = 11 if test else 101
    grid_length_y = 7 if test else 103
    
    for bot in list_of_positions:
        (old_x, old_y) = bot['pos']
        grid[old_y][old_x] -= 1
        (x, y) = add_tuples(bot['pos'], bot['velocity'])
        
        if x < 0:
            x = (grid_length_x) + x
        if x >= grid_length_x:
            x = x - (grid_length_x)
        if y >= grid_length_y:
            y = y - (grid_length_y)
        if y < 0:
            y = (grid_length_y) + y
        
        grid[y][x] += 1
        bot['pos'] = (x, y)

    print_grid(iter)

for i in range(0, 10000):
    simulate_step(False, i+1)
    

quadrant_1 = set([(x, y) for x in range(0, 101 // 2) for y in range(0, 103 // 2)])
quadrant_2 = set([(x, y) for x in range(0, 101 // 2) for y in range(103 // 2 + 1, 103)])
quadrant_3 = set([(x, y) for x in range(101 // 2 + 1, 101) for y in range(0, 103 // 2)])
quadrant_4 = set([(x, y) for x in range(101 // 2 + 1, 101) for y in range(103 // 2 + 1, 103)])


count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0

for bot in list_of_positions:
    if bot['pos'] in quadrant_1:
        count_1 += 1
    if bot['pos'] in quadrant_2:
        count_2 += 1
    if bot['pos'] in quadrant_3:
        count_3 += 1
    if bot['pos'] in quadrant_4:
        count_4 += 1 

print(count_1*count_4*count_2*count_3)