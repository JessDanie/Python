from operator import mod
x, n=input().split()
x, n=int(x), int(n)
r=[]
m=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
while x:
    r.append(m[int(x%n)])
    x=int(x/n)
r.reverse()
s=''.join(r)
print(s)
