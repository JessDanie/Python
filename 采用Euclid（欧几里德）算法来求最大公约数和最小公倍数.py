m, n = input().split(' ')
m,n=int(m),int(n)
t=m*n
while n:
    m,n=n,m%n
print('%d %d'%(m,t/m))


