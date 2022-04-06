#y=list(map(int, input().split(" ")))
y=int(input())
d = dict()
s:int = 0
lis=[]
for i in range(y):
    h=input().split(" ")
    s=int(h.pop())
    d[s] = " ".join(h)
    lis.append(s)
lis.sort()
for g in lis:
    print(d[g],g)
