with open("input.txt", 'r') as file:
    data = file.read().split("\n")
    data = [a.split(" ") for a in data]
    data = [list(map(int, a)) for a in data]

def safe(values):  
    for i in range(len(values)):    
        if i == 0:
            continue 
        diff = abs(values[i] - values[i-1])
        if diff < 1 or diff > 3:
            return False
    return True

def is_ascending_or_descending(lst):
    ascension_score = 0
    descending_score = 0
    for x in range(1, len(lst)):
        if (lst[x] - lst[x - 1]) > 0:
            ascension_score += 1
    for x in range(1, len(lst)):
        if (lst[x] - lst[x - 1]) < 0:
            descending_score += 1
    if len(lst) -1 == ascension_score  or len(lst) -1 == descending_score:
        return True
    else:
        return False

count = len([a for a in data if safe(a) and is_ascending_or_descending(a)])

print(count)