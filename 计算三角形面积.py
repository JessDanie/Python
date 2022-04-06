from cmath import sqrt
x, y, z= input().split(' ')
x, y, z= float(x), float(y), float(z)
s=(x+y+z)/2.0
a=sqrt(s*(s-x)*(s-y)*(s-z))
if x+y>z and x-y<z:
    print('%.2f'%((a.real**2+a.imag**2)**0.5))
else:
    print('%.2f %.2f %.2f error'%(x,y,z))
