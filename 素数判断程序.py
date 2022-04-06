n = int(input())
def sushu(n:int)-> bool:
    i = 2
    if n == 2:
        return True
    while i < n**(0.5) + 1:
        if(n%i==0):
            return False
        i+=1
    return True

if sushu(n):
    print(n, 'Yes')
else:
    print(n, 'No')