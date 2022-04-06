s=input()
m=list(s)
n = m.copy()
m.reverse()
print(s,end=' ')
if n==m:
    print('yes')
else:
    print('no')


