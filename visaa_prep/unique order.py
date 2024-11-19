n = int(input())
arr = list(map(int, input().split()))
u_e = []
s = set()
for num in arr:
    if num not in s:
        u_e.append(num)
        s.add(num)
print(" ".join(map(str, u_e)))
