import math
from itertools import product


def concat_ints(x, y):
    if y != 0:
        a = math.floor(math.log10(y))
    else:
        a = -1

    return int(x * 10 ** (1 + a) + y)


with open("input.txt") as file:
    data = file.read().split("\n")
    data = [line.split(":") for line in data]
    data = {line[0]: line[1].strip().split(" ") for line in data if len(line) == 2}

# print(data)


data = {int(key): [int(i) for i in line] for key, line in data.items()}


def find_results(numbers, target, usable_operators):
    n = len(numbers)

    for operators in product(usable_operators, repeat=n - 1):
        result = numbers[0]

        for i, operator in enumerate(operators):
            if operator == "+":
                result += numbers[i + 1]
            elif operator == "*":
                result *= numbers[i + 1]
            elif operator == "||":
                result = concat_ints(result, numbers[i + 1])

        if result == target:
            return True

    return False


# part1
result_1 = {key: find_results(data[key], key, ["*", "+"]) for key in data}

sum_res = sum((key for key in result_1 if result_1[key]))

print(sum_res)

# part 2

result_2 = {key: find_results(data[key], key, ["*", "+", "||"]) for key in data}

sum_res = sum((key for key in result_2 if result_2[key]))

print(sum_res)

