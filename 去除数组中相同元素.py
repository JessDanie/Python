m = list(map(int, input().split(' ')))
print(m[0],end=' ')
for i in range(1,len(m)):
    if m[i] not in m[0:i]:
        print(m[i],end=" ")