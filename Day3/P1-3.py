import sys
import math

sys.path.append('C:\\Code Projects\\Template\\AoC-template')
from aoc import get_input


data = get_input(3).splitlines()

# Print all the inputs
# for line in data:
#     print(line)


middle  = 0
box1 = ''
box2 = ''
letter = ''
priorities = 0

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
d= {}

for i in range(len(characters)):
    d[characters[i]] = i + 1

for i in data: # Each compartment
    middle = math.floor(len(i)/2)
    # print(middle)
    box1 = i[0: middle]
    box2 = i[middle: len(i)]

    for j in box1:
        if j in box2:
            letter = j
            break
    priorities += d[letter]

print(priorities)
