t = int(input())
for _ in range(t):
    x, n = map(int, input().split())
    st = x// 10
    s = st * n
    print(s)
