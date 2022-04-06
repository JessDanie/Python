#m = set(map(int, input().split(' ')))
m = input().split(' ')
n = m.pop()
if n in m:
    print(m.index(n))
else:
    print(n,'no')
