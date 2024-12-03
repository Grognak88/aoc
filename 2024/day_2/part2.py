with open("input.txt") as file:
    reports = file.read().split("\n")
    reports = [report.split() for report in reports]
    reports = [[int(s) for s in report] for report in reports]

def lst_diff(lst):   
    for x in range(1, len(lst)):
        diff = abs(lst[x] - lst[x - 1])
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

def damp_report(lst):
    backup_lst = lst
    for x in range(len(lst)):
        lst = lst[:x] + lst[x + 1:]
        if is_ascending_or_descending(lst) and lst_diff(lst):
            return True
        else:
            lst = backup_lst
    return False

safe_reports = [report for report in reports if damp_report(report)]
print(len(safe_reports))