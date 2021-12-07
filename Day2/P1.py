from re import S


file = open('input.txt', 'r')
sizes = file.readlines()
net_area = 0
for i in sizes:
    dimesnions = i.split('x')
    l  = int(dimesnions[0])
    w = int(dimesnions[1])
    h = int(dimesnions[2])
    area = 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
    net_area += area
print(net_area)