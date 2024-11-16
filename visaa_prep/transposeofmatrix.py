n = int(input())
m = []
for _ in range(n):
    r = list(map(int, input().split()))
    m.append(r)
t = [[m[j][i] for j in range(n)] for i in range(n)]
for r in t:
    print(" ".join(map(str, r)))
