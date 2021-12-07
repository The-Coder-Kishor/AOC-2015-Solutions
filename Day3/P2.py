from tkinter import Y


file = open('input.txt', 'r')
directions = file.readline()
map = []
for i in range(len(directions)):
    sub = []
    for i in range(len(directions)):
        sub.append(0)
    map.append(sub)
x1 = 0
y1 = 0
x2 = 0
y2 = 0
k = 0
map[x1][y1] = 1
for i in directions:
    if k%2 == 0:
        if i == '^':
            x1 += 1
        elif i == 'v':
            x1 -= 1
        elif i == '<':
            y1 -= 1
        elif i == '>':
            y1 += 1
    elif k%2 == 1:
        if i == '^':
            x2 += 1
        elif i == 'v':
            x2 -= 1
        elif i == '<':
            y2 -= 1
        elif i == '>':
            y2 += 1
    if(x1 == x2 and y1 == y2):
        map[x1][y1] += 1
    else:
        map[x1][y1] += 1
        map[x2][y2] += 1
    k += 1
count = 0
for i in map:
    for j in i:
        if j >= 1:
            count += 1
print(count)