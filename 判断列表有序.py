y:bool =True
x = list(map(int, input().split(' ')))
for i in range(len(x)-1):
    if x[i] > x[i+1]:
        print('list',x,'is not sorted')
        y=False
        break
if(y):
    print('list',x,'is already sorted')
