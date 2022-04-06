from cmath import pi
from pickletools import float8
from tokenize import Double
y, m = input().split()
y, m=float(y), float(m)
print('%.2f'%(pi*y*y*m))
