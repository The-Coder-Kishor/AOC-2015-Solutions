file = open('input.txt', 'r')
directions = file.readline()
map = []
for i in range(len(directions)):
    sub = []
    for i in range(len(directions)):
        sub.append(0)
    map.append(sub)
x = 0
y = 0
map[x][y] = 1
for i in directions:
    if i == '^':
        x += 1
    elif i == 'v':
        x -= 1
    elif i == '<':
        y -= 1
    elif i == '>':
        y += 1
    map[x][y] += 1
count = 0
for i in map:
    for j in i:
        if j >= 1:
            count += 1
print(count)