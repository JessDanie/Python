y=list(map(int, input().split(' ')))
#y.sort()
sum = y[0]*100+y[1]*10+y[2]
print('%d %d %d'%(y[0], y[1], y[2]), end=' ')
if y[0]+y[1]>y[2] and y[0]-y[1]<y[2]:
    print('yes')
else:
    print('no')
