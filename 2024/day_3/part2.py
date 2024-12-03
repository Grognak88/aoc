import re

multi = True

with open("input.txt") as file:
    content = file.read()
    pattern = r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(pattern, content)

def mul(command):
    global multi
    if command == "don't()":
        multi = False
        return None
    if command == "do()":    
        multi = True
        return None
    
    digs = "\\d{1,3}"
    nums = re.findall(digs, command)
    if multi:
        return int(nums[0]) * int(nums[1])
    else:
        return None

product = [mul(x) for x in matches]

def none_filter(val):
    if val == None:
        return False
    else:
        return True

filtered_product = filter(none_filter, product)

print(sum(filtered_product))