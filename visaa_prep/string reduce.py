st = input().strip()
r = ""
cc = st[0]
c = 0
for char in st:
    if char == cc:
        c += 1
    else:
        r += cc + str(c)
        cc = char
        c = 1
r += cc + str(c)
print(r)
