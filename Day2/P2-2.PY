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


sum_part2 = 0
i = 0
while i < len(curr_filtered):
    a = curr_filtered[i]
    b = curr_filtered[i+1]
    rock = 1
    paper = 2
    scissors = 3
    win = 6
    lose = 0
    draw = 3

    if (a == 'A'):  # Rock
        if (b == 'X'): # Lose
            sum_part2 += lose + scissors
        elif (b == 'Y'): # Draw
            sum_part2 += draw + rock
        else: # Win
            sum_part2 += win + paper

    elif (a == 'B'): # Paper
        if (b == 'X'): 
            sum_part2 += lose + rock
        elif (b == 'Y'): 
            sum_part2 += draw + paper
        else: 
            sum_part2 += win + scissors

    else :  # Scissors
        if (b == 'X'):
            sum_part2 += lose + paper
        elif (b == 'Y'): 
            sum_part2 += draw + scissors
        else: 
            sum_part2 += win + rock

    i += 2


print(sum_part2)