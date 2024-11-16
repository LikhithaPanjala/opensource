def ri(n):
    ng = n<0
    if ng:
        n = -n
    reversedNum = 0
    while n!= 0:
        d = n%10
        reversedNum = reversedNum * 10 + d
        n //= 10
    if ng:
        reversedNum =- reversedNum
    if reversedNum <-2 ** 31 or reversedNum>2**31-1:
        return 0
    return reversedNum
n = int(input())
print(ri(n))
