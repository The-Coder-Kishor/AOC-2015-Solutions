from re import S


file = open('input.txt', 'r')
sizes = file.readlines()
ribbon = 0
for i in sizes:
    dimesnions = i.split('x')
    l  = int(dimesnions[0])
    w = int(dimesnions[1])
    h = int(dimesnions[2])
    perimeter1 = 2*l + 2*w
    perimeter2 = 2*l + 2*h
    perimeter3 = 2*w + 2*h
    smallest = min(perimeter1, perimeter2, perimeter3)
    ribbon += smallest + l*w*h
print(ribbon)