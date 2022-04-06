x , s, sum, f= int(input()), [1], 1, '='
for i in range(2,int(x**0.5)+1):
    if x%i==0:
        sum+=(i+x/i)
        s.append (int(i))
        s.append(int(x/i))
if s[-1] ==s[-2]:
    s.pop()
    sum-=x**0.5
s.sort()
if x<sum:
    f='<'
elif x>sum:
    f='>'
print('%d%c'%(x, f),end='')
for i in s[:-1]:
    print('%d+'%(i),end='')
print('%d'%(s[-1]),end='')

