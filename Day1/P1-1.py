import sys

sys.path.append('C:\\Code Projects\\Template\\AoC-template')
from aoc import get_input


data = get_input(1).splitlines()
# Print all the inputs
# for line in data:
#     print(line)


calories = [None if a is '' else int(a) for a in data]

sum = 0
greatest_sum = 0

for i in calories:
    if i is None:
        sum = 0
    else:
        sum += i
    
    if greatest_sum < sum:
        greatest_sum = sum

print(greatest_sum)
