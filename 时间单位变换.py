import datetime
y= input()
y=int(y)
h=y/3600
m = (y%3600)/60
s=(y%60)
print('%d:%d:%d'%(h, m, s))


