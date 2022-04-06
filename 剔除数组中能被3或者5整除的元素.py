m = list(map(int, input().split(' ')))
s=0
for i in m:
    if i%3!=0 and i%5!=0:
        print(i,end=' ')
        s+=1
if not s:
    print('NULL')