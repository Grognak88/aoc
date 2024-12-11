from functools import cache

with open("input.txt") as file:
  data = file.read().replace("\n", "").split(" ")
  data = list(map(int, data))

@cache
def count(num, i, max_depth):   
  if i == max_depth:      
    return 1

  if num == 0:        
    return count(1, i+1, max_depth)
  elif len(str(num)) % 2 == 0:
    length = int(len(str(num)) // 2)
    part1 = int(str(num)[:length])
    part2 = int(str(num)[length:])             
    return count(part1, i+1, max_depth) + count(part2, i+1, max_depth)
  else:
    new_val = int(num * 2024)
    return count(new_val, i+1, max_depth)
     
count_1 = 0
count_2 = 0

for start in data:
  count_1 += count(start, 0, 25)

print(count_1)

for loc in data:
  count_2 += count(loc, 0, 75)

print(count_2)