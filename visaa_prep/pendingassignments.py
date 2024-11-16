x, y, z = map(int, input().split())
rt = x * y
ta = z * 24 * 60
if rt <= ta:
    print("YES")
else:
    print("NO")
