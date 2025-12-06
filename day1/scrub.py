
file_path = 'day1/day1_input.txt'

with open(file_path, 'r') as file:
    # Use a list comprehension to read each line, strip whitespace/newlines,
    # and store the clean string in a list.
    my_inputs = [line.strip() for line in file]

# print(my_inputs) 

current = 50
zero_counter = 0

for turn in my_inputs:
    direction = turn[0]
    mag = int(turn[1:])

    if direction == 'L':
        current = (current - mag) % 100
    else:
        current = (current + mag) % 100

    if current == 0:
        zero_counter += 1

print(zero_counter)
