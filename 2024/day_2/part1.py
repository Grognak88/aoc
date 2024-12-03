with open("input.txt", 'r') as file:
    data = file.read().split("\n")
    data = [a.split(" ") for a in data]
    data = [list(map(int, a)) for a in data]

def safe(values): 
    prev_diff = 0 
    for i in range(len(values)):    
        if i == 0:
            continue 
        diff = values[i] - values[i-1]
        if (prev_diff * diff < 0) or (abs(diff) < 1 or abs(diff) > 3):
            return False
        prev_diff = diff
    return True

count = len([a for a in data if safe(a)])

print(count)