import sys

sys.path.append('C:\\Code Projects\\Template\\AoC-template')
from aoc import get_input


data = get_input(5).splitlines()
data_crates = []  # List of all crate info
data_inst = []    # List of all instruction info
switch = 0        # Switch for seperating both crates and inst
stack_count = 0   # Number of crate positions
stack_height = 0  # Number of possible items stacked vertically



test_data = ['    [D]    ', '[N] [C]    ', '[Z] [M] [P]', ' 1   2   3 ', '', 'move 1 from 2 to 1', 'move 3 from 1 to 3', 'move 2 from 2 to 1', 'move 1 from 1 to 2'] 

# for line in test_data:
#     print(line)

# Print all the inputs
for line in data:

    if len(line) == 0:
        switch = 1
        continue

    if switch == 0:
        data_crates.append(line)
    else:
        data_inst.append(line)

data_crates.reverse()
data_crates.pop(0)
# print(data_crates)


data_instructions = []

for sentence in data_inst:
    a = ''
    for letter in sentence:
       if letter.isalpha():
        continue
       else:
        a+= letter
    data_instructions.append(a)


stack = {
    1:['F', 'T', 'C', 'L', 'R', 'P', 'G', 'Q'],
    2:['N', 'Q', 'H', 'W', 'R', 'F', 'S', 'J'],
    3:['F', 'B', 'H', 'W', 'P', 'M', 'Q'],
    4:['V', 'S', 'T', 'D', 'F'],
    5:['Q', 'L', 'D', 'W', 'V', 'F', 'Z'],
    6:['Z', 'C', 'L', 'S'],
    7:['Z','B', 'M', 'V', 'D','F'],
    8:['T', 'J','B'],
    9:['Q', 'N', 'B', 'G', 'L', 'S', 'P', 'H'],
}

test_stack = {
    1:['Z', 'N'],
    2:['M', 'C', 'D'],
    3:['P']
}



print(stack)
for i in data_instructions:
    i = i[1:]
    i_inst = i.split()
    print(i_inst)
    crate_amount = int(i_inst[0])
    start = int(i_inst[1])
    end = int(i_inst[2])

    counter = 0
    temp = []
    j = 0
    while j < crate_amount:
        counter += 1
        # print(counter)
        # print('start')
        # print(stack[start])
        temp.append(stack[start].pop())
        # print(stack[start])
        # print('end')
        # print(stack[end])
        
        j += 1
    temp.reverse()
    stack[end] = stack[end] + temp


ans = ''
for a, b in stack.items():
    # print(b)
    # print(b.pop())
    # print(len(b))
    if len(b) != 0:
        ans += str(b.pop())

ans = ans.replace('[', '')
ans = ans.replace(']', '')


print(ans)