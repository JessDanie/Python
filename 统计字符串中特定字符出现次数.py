#y=list(map(int, input().split(" ")))
y=input()
x=input()
#print("%d"%(y.count(x)))
sum:int=0
for u in y:
    if u ==x:
        sum+=1
print(sum)
