n = int(input())
a = list(map(int, input().split()))
ps = [0] * (n + 1)
ss = [0] * (n + 1)
for i in range(1, n + 1):
    ps[i] = ps[i - 1] + a[i - 1]
for i in range(n - 1, -1, -1):
    ss[i] = ss[i + 1] + a[i]
B = []
for i in range(n):
    lw = ps[i]
    rw = ss[i + 1]
    B.append(abs(lw - rw))
print(" ".join(map(str, B)))
