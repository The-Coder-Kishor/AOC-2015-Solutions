import hashlib
key = "bgvyzdsv"
y = True
i = 1
while(y):
    code = key + str(i)
    hash = hashlib.md5(code.encode('utf-8')).hexdigest()
    if hash[:5] == "00000":
        print(hash)
        y = False
        break
    i += 1
print(i)