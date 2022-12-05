import sys

sys.path.append('C:\\Code Projects\\Template\\AoC-template')
from aoc import get_input


data = get_input(4).splitlines()

# Print all the inputs
# for line in data:
#     print(line)


total = 0

for i in data:
    pair_list = i.split(',')

    set1 = pair_list[0].split('-')
    set2 = pair_list[1].split('-')

    set1_start = int(set1[0])
    set1_end = int(set1[1])

    set2_start = int(set2[0])
    set2_end = int(set2[1])

    if (set1_start <= set2_start and set1_end >= set2_end) or (set1_start >= set2_start and set1_end <= set2_end):
        total+= 1 

print(total)