import re

with open("input.txt") as file:
    content = file.read()
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(pattern, content)



def mul(command):
    digs = "\\d{1,3}"
    nums = re.findall(digs, command)
    return int(nums[0]) * int(nums[1])

product = [mul(x) for x in matches]

print(sum(product))