t = int(input())
r = []
for _ in range(t):
    x = int(input())
    if 67 <= x <= 45000:
        r.append("YES")
    else:
        r.append("NO")
print("\n".join(r))
