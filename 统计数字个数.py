x = list(map(int, input().split(' ')))
s = list(set(x))
s.sort()
for i in s:
    print('%-6d'%i, x.count(i), sep='')

