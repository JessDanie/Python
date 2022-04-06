from tokenize import Double


n = int(input())
i:int=1
sum:int = 0
m:int=1
while m<n+1:
    sum+= m*m+m
    m+=2

print(sum)
