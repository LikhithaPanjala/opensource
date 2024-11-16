def dnd(x, y, z):
    d = 0
    nd = 0
    for num in z:
        if num % y == 0:
            d += num
            
        else:
            nd += num
    return d - nd
x, y = map(int, input().split())
z = list(map(int, input().split()))
print(dnd(x, y, z))
