y=list(map(int, input()))
#y.sort()
sum = y[0]*100+y[1]*10+y[2]
print('%d'%sum, end=' ')
if y[0]**3+y[1]**3+y[2]**3 == sum:
    print('yes')
else:
    print('no')
