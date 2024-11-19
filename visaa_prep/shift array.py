n = int(input())
arr = list(map(int, input().split()))
if n > 1:
    r_arr = arr[1:] + arr[:1]
else:
    r_arr = arr
print(" ".join(map(str, r_arr)))
