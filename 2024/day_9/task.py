with open("/home/onyxia/work/aoc/2024/day_9/input.txt") as file:
    data = file.read()
    data = list(data)

def return_repeted_char(ident, times):
    out = []

    for i in range(times):
        out.append(ident)
    
    return out

disk_layout = []

ident = 0

for i, val in enumerate(data):
    if i % 2 == 0:
        disk_layout.append(return_repeted_char(ident, int(val)))
        ident += 1
    else:
        disk_layout.append(return_repeted_char('.', int(val)))

flat_layout = [c for block in disk_layout for c in block]

def dots_length(starting_index):
    last_index = starting_index
    for i in range(starting_index+1, len(flat_layout)): # +1 to save one iteration
        last_index += 1
        if flat_layout[i] != '.':
            break        
    return last_index - starting_index    

print(flat_layout)
print(len(flat_layout))

def rearrange(continous_space):
    global flat_layout
    i = -1
    while i > (-1*len(flat_layout) - 1):       
        dot_index = flat_layout.index('.')          
        element = flat_layout[i]
        if element == '.':
                i -= 1
                continue 
        if continous_space:
            length_dots = dots_length(dot_index)
            first_occurance_of_element = flat_layout.index(element)
            length_element = len(flat_layout[first_occurance_of_element:i+1 if i < -1 else None])
            while length_dots < length_element:
                dot_index = flat_layout.index('.', dot_index+length_dots) if '.' in flat_layout[dot_index+length_dots:] else None
                if  dot_index == None or dot_index > first_occurance_of_element:
                    break
                length_dots = dots_length(dot_index)
                        
            if dot_index is not None and dot_index < first_occurance_of_element:
                first = flat_layout[:dot_index]
                file = flat_layout[first_occurance_of_element:i+1 if i < -1 else None]
                middle = flat_layout[dot_index + length_element: first_occurance_of_element]
                before_end = flat_layout[i+1:] if i < -1 else []
                free_space = flat_layout[dot_index: dot_index + length_element]            
                flat_layout = [*first, *file, *middle, *free_space, *before_end]
   
            i -= length_element

        else:             
            flat_layout[dot_index] = element
            flat_layout[i] = '.'        
            if i == -1*len(flat_layout):
                flat_layout.pop(0)
                flat_layout.append('.')
            i -= 1

# rearrange(False)

def multiply_positions():
    cum_sum = 0

    for i, val in enumerate(flat_layout):
        if val == '.':
            continue
        cum_sum += i * val
    return cum_sum

# print(multiply_positions())

# data_dict = {(i, ident): len(file) for i, file in enumerate(disk_layout) for ident in file}

# print(data_dict)

rearrange(True)

print(flat_layout)

print(multiply_positions())