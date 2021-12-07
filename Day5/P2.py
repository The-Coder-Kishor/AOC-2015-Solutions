file = open('input.txt', 'r')
strings = file.readlines()

def count_of_pairs(a):
    for i in range(len(a)-1):
        str = a[i] + a[i+1]
        if str in a[i+2:]:
            return True
    return False

def count_of_double_letters(a):
    for i in range(len(a)-1):
        if a[i] in a[i+2:]:
            return True
    return False

sum = 0
for i in strings:
    if count_of_double_letters(i) or count_of_pairs(i):
        sum += 1
print(sum)