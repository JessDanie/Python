x = list(map(int, input().split(' ')))
t=[list(map(int, input().split(' '))) for i in range(x[0])]
for i in range(x[1]):
    sum=0
    for j in range(x[0]):
        sum+=t[j][i]
    print(sum, sep='', end=' ')

