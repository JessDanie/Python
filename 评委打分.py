score:list = list(map(float, input().split(' ')))
mx, mn, s = 0, 101, 0
for i in score:
	if i<mn:
		mn =i
	if i>mx:
		mx =i
	s+=i
s-=(mx+mn)
s/=(len(score)-2)
print('%.2f'%(s))
del mx, mn, s
#1.55 50.55 50.55 50.55 50.55 50.55 50.55 50.55 50.55 100
