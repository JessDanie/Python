x = list(map(int, input().split(' ')))
t=[list(map(int, input().split(' '))) for i in range(x[0])]
max = -1
max_i, max_j = 0, 0
min = 100
min_i , min_j = 0, 0
for i in range(x[0]):
    for j in range(x[1]):
        if t[i][j]>max:
            max, max_i, max_j =t[i][j], i, j
        if t[i][j]<min:
            min, min_i, min_j =t[i][j], i, j
print('max[%d][%d]=%d min[%d][%d]=%d'%(max_i, max_j, max, min_i, min_j, min))

