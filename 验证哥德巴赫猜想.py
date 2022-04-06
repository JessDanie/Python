def ss(n:int)-> bool:
    i = 2
    while i < n**(0.5) + 1:
        if(n%i==0):
            return False
        i+=1
    return True

x=int(input())
for i in range(3, int(x/2)):
    if ss(i) and ss(x-i):
        print('%d %d'%(i, x-i))


