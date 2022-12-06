import sys

sys.path.append('C:\\Code Projects\\Template\\AoC-template')
from aoc import get_input


data = get_input(6).splitlines()
test_data = data[0]
# test_data = 'bvwbjplbgvbhsrlpgdmjqwftvncz'


password = ''
memory = {}
ans = 0

for i in test_data:
    ans += 1
    password += i
    # print(password)
    # print(memory)
    if i in memory.keys():
        if memory[password[0]] == 1:
            memory.pop(password[0])
        else:
            memory[password[0]] -= 1
        password = password[1:len(password)]
        print(memory)
        if i in memory.keys():
            memory[i] += 1
        else:
             memory[i] = 1
        print(memory)

        continue
    else:
        memory[i] = 1
    
    if len(password) == 14:
        # print(password)
        for a,b in memory.items():
            if b > 1:
                print(password)
                print(memory)
                if memory[password[0]] == 1:
                    memory.pop(password[0])
                else:
                    memory[password[0]] -= 1
                password = password[1:len(password)]
                break
        
        if len(password) == 14:
            print(password)
            print(ans)
            break
    
