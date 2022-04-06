i = list(input().split(' '))
del i[(i.index('0')):]
i.sort()
print(i[-1],i.count(i[-1]))
