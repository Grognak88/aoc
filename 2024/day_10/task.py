from time import time
from threading import Thread
start_time = time()

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def add_child(self, child):
        self.children.append(child)

with open("/home/onyxia/work/aoc/2024/day_10/input.txt") as file:
    data = file.read().split("\n")
    data = [list(line) for line in data]
    dimension = len(data)
    data = {j+i*1j: int(data[i][j]) for i in range(dimension) for j in range(len(data[0]))}
   
roots = {key: TreeNode((key, val)) for key, val in data.items() if val == 0}

thread_pool = []

def traverse_tree(current_location: TreeNode):
    if current_location.data[1] == 9:
        return
    next_incline = current_location.data[1] + 1
    directions = (current_location.data[0] + (0-1j), current_location.data[0] + (0+1j), current_location.data[0] + (-1+0j), current_location.data[0] + (1+0j))    

    for next_step in directions:
        if next_step in data and data[next_step] == next_incline:
            next_node = TreeNode((next_step, next_incline))
            current_location.add_child(next_node)
            traverse_tree(next_node)                   

def workers(start, step, dimension):
    global roots
    for root in list(roots.values())[start:start + step if start+step <= dimension else None]:        
        traverse_tree(root)

def main_thread():
    step = 3
    for i in range(0,dimension, 3):       
        thread = Thread(target=workers, args=(i, step, dimension))
        thread.start()
        thread_pool.append(thread)

main_thread()

for thread in thread_pool:
    thread.join()

scores = []
scores_2 = []

def walk_tree(node: TreeNode, unique_nodes):
    if len(node.children) == 0 and node.data[1] == 9:
        unique_nodes.add(node.data)
        return 1

    return sum((walk_tree(child, unique_nodes) for child in node.children))

for root in roots.values():
    unique_nodes = set()
    scores_2.append(walk_tree(root,unique_nodes))
    scores.append(len(unique_nodes))

print(f"{sum(scores)}: ({time() - start_time:.3f}s)")
print(f"{sum(scores_2)}: ({time() - start_time:.3f}s)")