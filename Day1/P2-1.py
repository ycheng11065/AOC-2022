import sys

sys.path.append('C:\\Code Projects\\Template\\AoC-template')
from aoc import get_input


data = get_input(1).splitlines()
# Print all the inputs
# for line in data:
#     print(line)


calories = [None if a is '' else int(a) for a in data]


greatest_three = []

sum = 0
greatest_sum = 0

for a in range(len(calories)):
    i = calories[a]

    if i is None:
        greatest_three.append(sum)
        sum = 0
    else:
        sum += i

        if a == len(calories) - 1:
            greatest_three.append(sum)

counter = 0
three_sum = 0

for i in range(3):
    index = greatest_three.index(max(greatest_three))
    three_sum += max(greatest_three)
    greatest_three.pop(index)

print(three_sum)
