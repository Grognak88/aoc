rules = []
pages = []

input_break = False

with open("input.txt") as file:
    for line in file:
        if line == '\n':
            input_break = True
            continue
        if input_break:
            pages.append(line.strip())
        else:
            rules.append(line.strip())


# MAke a dict of rules, with trigger index as values, staring at -1
pages = [[int(a) for a in line.split(',')] for line in pages]
rules = {(int(rule.split('|')[0]),int(rule.split('|')[1])): (-1,-1) for rule in rules}

def is_ordered(line):
    global rules

    for i, d in enumerate(line):
        for key in rules:
            match key:
                case (l,r) : 
                    (orig_l,orig_r) = rules[(l,r)]
                    if l == d:
                        rules[(l,r)] = (i, orig_r)
                    if r == d:
                        rules[(l,r)] = (orig_l, i)
                case _ : return False
    
    for key, val in rules.items():
        (l,r) = val
        if l > r and r != -1:
            for key in rules:
                rules[key] = (-1,-1)
            return False
    
    for key in rules:
                rules[key] = (-1,-1)

    return True

ordered = [is_ordered(line) for line in pages]
ordered_index = [i for i, val in enumerate(ordered) if val]

# print(rules)

# print(ordered)

# print(ordered_index)

ordered_middle_elements = [line[len(line)//2] for line in [pages[a] for a in ordered_index]]

# print(ordered_middle_elements)
print(f"Sum of middle elements: {sum(ordered_middle_elements)}")

# part2
from collections import defaultdict

unordered_indexes = [i for i, val in enumerate(ordered) if not val]

print(unordered_indexes)

rules_as_dict_of_sets = defaultdict(set)

# all pages to the right of k is in set k
for (k, v) in rules:
    rules_as_dict_of_sets[k].add(v)

def order_line(line):
    i = 0

    while i < len(line) - 1:
        side_nummer = line[i]
        resten_av_sider = set(line[i + 1:])
        #Check if remaining pages is a subset of the pages to the right of side_nummer
        if not (resten_av_sider <= rules_as_dict_of_sets[side_nummer]):
            #if not move current page to the end
            line.append(line.pop(i))
            # restart looop
            i=0
        else:
            i+=1
    return line

rettet = [order_line(line) for line in [pages[i] for i in unordered_indexes]]
rettet_middle_elements = [line[len(line)//2] for line in rettet]

print(sum(rettet_middle_elements))
