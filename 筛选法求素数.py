x = list(map(int, input().split(' ')))
def sushu(n:int)-> bool:
    i = 2
    if n == 2:
        return True
    while i < n**(0.5) + 1:
        if(n%i==0):
            return False
        i+=1
    return True
s:int = 0
for i in range(2, x[0]+1):
    if(sushu(i)):
        s+=1
        print(i,end=" ")
        if not s%5:
            print()
