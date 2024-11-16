n = int(input())
st = list(map(int, input().split()))
st.sort(reverse=True)
mp = -1
for i in range(n - 2):
    if st[i] < st[i + 1] + st[i + 2]:
        mp = st[i] + st[i + 1] + st[i + 2]
        break
print(mp)
