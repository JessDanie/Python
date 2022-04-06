import datetime
y, m, d = input().split()
y, m, d=int(y), int(m), int(d)
a=datetime.date(y,m,d)
b=datetime.date(y,1,1)
c=a-b
print(c.days+1)
