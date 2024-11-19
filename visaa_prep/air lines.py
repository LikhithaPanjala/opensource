x, n = map(int, input().split())
p = (n + 99) // 100
a = p - x
if a < 0:
    a = 0
print(a)
