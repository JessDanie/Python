m=int(input())
sum:int =0
n1:int =1
n2:int =1

for i in range(1, m-1):
    n1, n2 = n2, n1 + n2
if m in [1,2]:
    print(1)
else:
    print(n2)


