n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
rs = [0] * n
cs = [0] * n
for i in range(n):
    for j in range(n):
        rs[i] += m[i][j]
        cs[j] += m[i][j]
ra = [rs[i] + cs[i] for i in range(n)]
print(" ".join(map(str, ra)))
