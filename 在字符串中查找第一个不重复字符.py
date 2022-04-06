#y=list(map(int, input().split(" ")))
from xmlrpc.client import boolean


y=input()
f = True
d = dict.fromkeys([chr(x) for x in range(ord('a'), ord('z')+1)], 0)
for n in y:
    d[n]+=1
for n in y:
    if d[n] == 1:
        print(n)
        f=False
        break
if f:
    print(y+" error")

