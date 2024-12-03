with open("input.txt") as file:
    data = file.read().split("\n")
    data = [a.split() for a in data]
    data = [list(map(int, a)) for a in data]

def safe(values):
    prev_diff = 0   
    for i in range(1, len(values)):
        if i == 0:
            continue
        diff = values[i] - values[i-1]
        if (prev_diff * diff < 0) or (abs(diff) < 1 or abs(diff) > 3):
            return False
        prev_diff = diff
    return True

def problem_dampener(line):
    backup_line = line
    for x in range(len(line)):
        line = line[:x] + line[x + 1:]
        if safe(line):
            return True
        else:
            line = backup_line
    return False

safe_count = len([report for report in data if problem_dampener(report)])

print(safe_reports)