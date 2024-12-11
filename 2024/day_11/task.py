from functools import cache
from time import time

start_time = time()

with open("input.txt") as file:
  data = file.read().replace("\n", "").split(" ")
  data = list(map(int, data))

@cache
def digits(num):
  count=0
  while(num>0):
    count=count+1
    num=num//10
  return count

@cache
def tenbase(zeros):
  val = 1
  i = 0
  while i < zeros:
    val *= 10
    i += 1
  
  return val

@cache
def count(num, i, max_depth):   
  if i == max_depth:      
    return 1

  if num == 0:        
    return count(1, i+1, max_depth)
  elif len(str(num)) % 2 == 0:
    length = digits(num)//2
    splitter = tenbase(length)
    part1 = num // splitter
    part2 = num % splitter            
    return count(part1, i+1, max_depth) + count(part2, i+1, max_depth)
  else:
    new_val = int(num * 2024)
    return count(new_val, i+1, max_depth)
     
count_1 = 0
count_2 = 0

for start in data:
  count_1 += count(start, 0, 25)

print(f"{count_1}: {time() - start_time:.3f}s")

for loc in data:
  count_2 += count(loc, 0, 75)

print(f"{count_2}: {time() - start_time:.3f}s")