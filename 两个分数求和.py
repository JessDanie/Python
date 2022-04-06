a1, b1, a2, b2=input().replace('/', ' ').split()
a, b=int(a1)*int(b2)+int(a2)*int(b1), int(b1)*int(b2)
if a > b:
    m, n=a, b
else:
    m, n=b, a
while n:
    m,n=n,m%n
print('%d/%d'%((a)/m, (b)/m))


