file = open('input.txt', 'r')
strings = file.readlines()

def count_of_vowels(a):
    count = 0
    for i in a:
        if i in "aeiou":
            count += 1
    if count >= 3:
        return True
    else:
        return False

def count_of_double_letters(a):
    count = 0
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            return True
    return False

def count_of_bad_strings(a):
    if 'ab' in i:
        return False
    elif 'cd' in i:
        return False
    elif 'pq' in i:
        return False
    elif 'xy' in i:
        return False
    return True
sum = 0
for i in strings:
    if count_of_vowels(i) and count_of_double_letters(i) and count_of_bad_strings(i):
        sum += 1
print(sum)