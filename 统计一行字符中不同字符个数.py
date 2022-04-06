m=list(input())
suma:int =0
sumb:int =0
summ:int =0
sumc:int =0
for i in m:
    if 'a'<=i<='z' or 'A'<=i<='Z':
        suma+=1
    elif i == ' ':
        sumb+=1
    elif '0'<=i<='9':
        summ+=1
    else:
        sumc+=1
print('%d %d %d %d'%(suma, sumb, summ, sumc))
