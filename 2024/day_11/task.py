class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def add_child(self, child):
        self.children.append(child)


with open("input.txt") as file:
    data = file.read().replace("\n", "").split(" ")
    data = {i: TreeNode(int(val)) for i, val in enumerate(data)}

nums_1 = []
nums_2 = []

def grow_tree(node: TreeNode, i, max_depth):
    if node.data == 0:
        new_child = TreeNode(1)
        node.add_child(new_child)
    elif len(str(node.data)) % 2 == 0:
        length = len(str(node.data)) // 2
        part1 = TreeNode(int(str(node.data)[:length]))
        part2 = TreeNode(int(str(node.data)[length:]))        
        node.add_child(part1)
        node.add_child(part2)
    else:
        new_val = TreeNode(node.data * 2024)
        node.add_child(new_val)

    if i+1 == 25:
        nums_1.append(node.children)
    
    if i+1 == max_depth:
        nums_2.append(node.children)
        return

    for child in node.children:
        grow_tree(child, i+1, max_depth)    

for root in data.values():
    grow_tree(root, 0, 75)

print(len([d for ld in nums_1 for d in ld]))

print(len([d for ld in nums_2 for d in ld]))

