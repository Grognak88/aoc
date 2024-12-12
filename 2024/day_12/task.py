from collections import defaultdict
from time import time

start_time = time()

with open("/mnt/c/Users/aer/workspace/aoc/2024/day_12/input.txt") as file:
    data = file.read().split("\n")
    data = [list(line) for line in data]

plots = defaultdict(list)

visited = set()

for y,line in enumerate(data):
    for x,val in enumerate(line):
        plots[val].append((x,y))

def count_plots(plant_type):
    visited.add(plots[plant_type][0])
    regions = []
    count_1 = 0
    count_2 = 0

    for plant in plots[plant_type]:
        if plant in visited:
            continue
        plot = [plant]
        region = set(plot)

        while plot:        
            plant_x, plant_y = plot.pop()
            neighbors = [(plant_x+1, plant_y), (plant_x-1, plant_y), (plant_x, plant_y-1), (plant_x, plant_y+1)]
            for neighbor in neighbors:
                if len(data[0])-1 < neighbor[0] or neighbor[0] < 0 or len(data)-1 < neighbor[1] or neighbor[1] < 0:
                    continue                
                if (data[neighbor[1]][neighbor[0]] == plant_type and neighbor not in visited):
                    visited.add(neighbor)
                    plot.append(neighbor)
                    region.add(neighbor)
        
        regions.append(region)

           
        area = len(region)      
        count_region_1 = sum(1 
                    for 
                    (plant_x, plant_y) in region
                    for neighbor in 
                    [(plant_x+1, plant_y), (plant_x-1, plant_y), 
                     (plant_x, plant_y-1), (plant_x, plant_y+1)] 
                     if neighbor not in region)         
        count_1 += count_region_1 * area
             
    
    
        
        count_region = 0
        for x, y in region:
            if (x, y - 1) not in region and (
                (x - 1, y) not in region or (x - 1, y - 1) in region
            ):
                count_region += 1
            if (x, y + 1) not in region and (
                (x - 1, y) not in region or (x - 1, y + 1) in region
            ):
                count_region += 1
            if (x - 1, y) not in region and (
                (x, y - 1) not in region or (x - 1, y - 1) in region
            ):
                count_region += 1
            if (x + 1, y) not in region and (
                (x, y - 1) not in region or (x + 1, y - 1) in region
            ):
                count_region += 1
        count_2 += count_region * area
    
    return count_1, count_2

counts = [count_plots(i) for i in plots]

counts_1 = sum(c[0] for c in counts)
counts_2 = sum(c[1] for c in counts)

print(f"{counts_1}:{counts_2}: {time() - start_time:.3f}s")   