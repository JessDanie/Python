i = list(input().split(' '))
del i[(i.index('0')):]
sum = 0
f = 0
z = 0
for x in range(0, len(i)):
    sum+=int(i[x])
    if(0 < int(i[x])):
        z+=1

print("%d %d %d"%(z, len(i) - z, sum))
