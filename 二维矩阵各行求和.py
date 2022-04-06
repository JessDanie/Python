x = list(map(int, input().split(' ')))
t=[list(map(int, input().split(' '))) for i in range(x[0])]
for i in range(x[0]):
    sum=0
    for j in range(x[1]):
        sum+=t[i][j]
    print(sum, sep='', end=' ')

