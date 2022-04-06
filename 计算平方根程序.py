#y=list(map(int, input().split("")))
y = int(input())
if 0<y<1000:
    x, c= (y**0.5), int(y**0.5)
    if x >= c+0.500000000:
        c+=1
    print("%d"%c)
else:
    print("%d error"%y)
