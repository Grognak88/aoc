from time import time

start_time = time()

with open("input.txt") as file:
    data = file.read()
    data = list(data)

free_spaces = 0

def return_repeted_char(ident, times):
    global free_spaces
    out = []
    if ident == '.':
        free_spaces += times
    for i in range(times):
        out.append(ident)
        
    return out

disk_layout = [return_repeted_char(i >> 1,int(x)) if i+1&1 else return_repeted_char('.', int(x)) for i,x in enumerate(data) ]

ident = 0

flat_layout = [c for block in disk_layout for c in block]

print(time() - start_time)

def dots_length(starting_index):
    last_index = starting_index
    for i in range(starting_index+1, len(flat_layout)): # +1 to save one iteration
        last_index += 1
        if flat_layout[i] != '.':
            break        
    return last_index - starting_index    

def rearrange():
    global flat_layout
    i = -1
    while i > (-1*len(flat_layout) - 1):       
        dot_index = flat_layout.index('.')          
        element = flat_layout[i]
        if element == '.':
            i -= 1
            continue 
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

       

def part1():
    global free_spaces
    while free_spaces:        
        element = flat_layout.pop()
        if element != '.':
            dot_index = flat_layout.index('.')
            flat_layout[dot_index] = element
        free_spaces -= 1

# rearrange()

def multiply_positions():
    return sum([i * val for i, val in enumerate(flat_layout)])
    
part1()

print(time() - start_time)

print(multiply_positions())

flat_layout = [c for block in disk_layout for c in block]

# rearrange(True)

# print(flat_layout)

# print(multiply_positions())