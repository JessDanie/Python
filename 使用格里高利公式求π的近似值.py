from tokenize import Double


n = int(input())
i:int=1
sum:Double = 0
m:int=1
while True:
    t = 1/(2*i-1)
    if(10**-n>t):
        break
    sum+= t*m
    m=-m
    i+=1

print('%.5f'%(sum*4))
