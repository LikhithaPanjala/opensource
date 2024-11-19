n = int(input())
def c_m(l, d):
    return l // d
c3 = c_m(n, 3)
c5 = c_m(n, 5)
cb = c_m(n, 15)
r = c3 + c5 - cb
print(r)
