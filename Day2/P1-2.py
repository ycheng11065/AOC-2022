import sys

sys.path.append('C:\\Code Projects\\Template\\AoC-template')
from aoc import get_input


data = get_input(2).splitlines()
# Print all the inputs
# for line in data:
#     print(line)

data_var = ''

for i in data:
    data_var+= ' '
    data_var+= i

# print(data_var)


curr = [*data_var]
curr_filtered = []

for i in curr:
    if i != ' ':
        curr_filtered.append(i)


sum = 0
i = 0
while i < len(curr_filtered):
    a = curr_filtered[i]
    b = curr_filtered[i+1]

    if (a == 'A'):  # Rock
        if (b == 'X'): # Rock
            sum += 3 + 1
        elif (b == 'Y'): # Paper
            sum += 6 + 2
        else: # Scissors
            sum += 0 + 3

    elif (a == 'B'): # Paper
        if (b == 'X'): # Rock
            sum += 0 + 1
        elif (b == 'Y'): # Paper
            sum += 3 + 2
        else: # Scissors
            sum += 6 + 3

    else :  # Scissors
        if (b == 'X'): # Rock
            sum += 6 + 1
        elif (b == 'Y'): # Paper
            sum += 0 + 2
        else: # Scissors
            sum += 3 + 3

    i += 2

print(sum)