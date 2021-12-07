file = open('input.txt','r')
instructions = file.readline()
floor = 0
for i in range(len(instructions)):
    if floor == -1:
        print(i)
        break
    if instructions[i] == '(':
        floor += 1
    elif instructions[i] == ')':
        floor -= 1