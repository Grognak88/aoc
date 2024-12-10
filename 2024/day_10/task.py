from threading import Thread

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def add_child(self, child):
        self.children.append(child)

with open("/home/onyxia/work/aoc/2024/day_10/input.txt") as file:
    data = file.read().split("\n")
    data = [list(line) for line in data]
    data = {j+i*1j: int(data[i][j]) for i in range(len(data)) for j in range(len(data[0]))}
    
starting_locations = {key: set() for key, val in data.items() if val == 0}

threads = []

starting_trees = {key: TreeNode(key) for key, val in data.items() if val == 0}

def traverse(origin, current_location, incline):
    global threads
    directions = (current_location + (0-1j), current_location + (0+1j), current_location + (-1+0j), current_location + (1+0j))
    if incline == 9:
        return
    
    for next_step in directions:        
        if next_step in data and data[next_step] == incline + 1:
            starting_locations[origin].add((next_step, data[next_step]))
            thread = Thread( target=traverse, args=(origin, next_step, incline + 1))
            thread.start()   
            threads.append(thread)

def traverse_tree(current_location: TreeNode, incline: int):
    global threads  

    if incline == 9:
        return
    if current_location.data == (1+6j):
        pass
    next_incline = incline +1
    directions = (current_location.data + (0-1j), current_location.data + (0+1j), current_location.data + (-1+0j), current_location.data + (1+0j))    

    for next_step in directions:
        if next_step in data and data[next_step] == next_incline:
            next_node = TreeNode(next_step)
            current_location.add_child(next_node)            
            thread = Thread( target=traverse_tree, args=(next_node, next_incline))
            thread.start()   
            threads.append(thread)   

for origin in starting_locations:
    traverse(origin,origin,0)

for worker in threads:
    worker.join()

threads = []

scores = []

for start, paths in starting_locations.items():
    score = 0
    for location in paths:
        match location:
            case (_, 9):
                score += 1
    scores.append(score)

print(sum(scores))

for origin, root in starting_trees.items():
    traverse_tree(root,0)

for worker in threads:
    worker.join()

scores_2 = []

def walk_tree(node: TreeNode, ):
    if len(node.children) == 0 and data[node.data] == 9:
        return 1

    return sum((walk_tree(child) for child in node.children))


for root in starting_trees.values():
    scores_2.append(walk_tree(root))

print(sum(scores_2))