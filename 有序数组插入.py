p=int(input())
x = list(map(int, input().split(' ')))
p=int(input())

#if p>x[-1]:
#    x.append(p)
#elif p<x[0]:
#    x.insert(0, p)
#else:
#    for i in range(len(x)-1):
#        if x[i]<=p<=x[i+1]:
#            x.insert(i+1, p)
#            break
x.append(p)
x.sort()
for i in x:
    print(i, end=' ')

