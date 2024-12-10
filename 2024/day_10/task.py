from time import time
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
    data = {j+i*1j: int(data[i][j]) for i in range(len(data)) for j in range(len(data[0]))}
   
roots = {key: TreeNode((key, val)) for key, val in data.items() if val == 0}
           
def traverse_tree(current_location: TreeNode, incline: int):
    if incline == 9:
        return
    next_incline = incline +1
    directions = (current_location.data[0] + (0-1j), current_location.data[0] + (0+1j), current_location.data[0] + (-1+0j), current_location.data[0] + (1+0j))    

    for next_step in directions:
        if next_step in data and data[next_step] == next_incline:
            next_node = TreeNode((next_step, next_incline))
            current_location.add_child(next_node)  
            traverse_tree(next_node, next_incline)        
             
for origin, root in roots.items():
    traverse_tree(root,0)

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