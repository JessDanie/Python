x = int(input())
M, m, sum, min, max=6, 5, 0, 0, x
if x > 3:
    min=x-3
for i in range(min, max):
    if i>=M:
        sum+= M+m-i+1
    elif i>=m:
        sum+=m+1
    else:
        sum+=i+1
if not sum:
    sum = 1
print("%d"%sum)


