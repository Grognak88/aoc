from sympy import solve
from sympy.abc import a, b
import re

with open("input.txt") as file:
    data = file.readlines()

data_sectionized = []

pattern = r"([A-B]): X\+(\d{2}), Y\+(\d{2})"
pattern_target = r"Prize: X=([0-9]+), Y=([0-9]+)"

section = {}
for line in data:
    match_button = re.findall(pattern, line)
    match_target = re.findall(pattern_target, line)
    if match_button:
        section[match_button[0][0]]= (int(match_button[0][1]), int(match_button[0][2]))
    if match_target:
        section['target'] = (int(match_target[0][0]), int(match_target[0][1]))
        data_sectionized.append(section)
        section={}

def solve_equation(current_section, p_2):
    COST_A = 3
    COST_B = 1
    ERROR = 10000000000000
    TARGET_X = current_section['target'][0]+(ERROR if p_2 else 0)
    TARGET_Y = current_section['target'][1]+(ERROR if p_2 else 0)
    solvable = False
    solution = solve([a*current_section['A'][0]+b*current_section['B'][0]-TARGET_X, 
                      a*current_section['A'][1]+b*current_section['B'][1]-TARGET_Y], [a,b], dict=True)
    if solution[0][a].is_Integer and solution[0][b].is_Integer:
        solvable = True

    return solvable, solution[0][a]*COST_A+ solution[0][b]*COST_B


result_1 = sum([cost for solvable, cost in [solve_equation(sec, False) for sec in data_sectionized] if solvable])

print(result_1)


result_2 = sum([cost for solvable, cost in [solve_equation(sec, True) for sec in data_sectionized] if solvable])

print(result_2)