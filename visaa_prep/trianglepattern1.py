x=int(input())
c=1
for i in range(1, x+1):
    for j in range(1, i+1):
        print(c, end=" ")
        c+=1
    print()
