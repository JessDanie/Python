n = int(input())
d = dict()
for i in range(n):
    l = input().split(' ')
    d[int(l[0])] = l[1]+" "+l[2]
k = dict().fromkeys(d, 0)
max:int = 0
max_i:int = 0
x = list(map(int, input().split(' ')))
for i, v in k.items():
    k[i] = x.count(i)
    if k[i] >max:
        max=k[i]
for i, v in k.items():
    if max == k[i]:
        print(i, d[i])
