import sys
import math

sys.path.append('C:\\Code Projects\\Template\\AoC-template')
from aoc import get_input


data = get_input(3).splitlines()

# Print all the inputs
# for line in data:
#     print(line)

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
d= {}

for i in range(len(characters)):
    d[characters[i]] = i + 1

i = 0
sum = 0

while i + 2 < len(data):
    first = data[i]
    second = data[i + 1]
    third = data[i + 2]

    for j in first: 
        if (j in second and j in third):
            sum += d[j]
            break
    
    i += 3

print(sum)

