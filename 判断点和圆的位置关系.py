r, x, y= input().split(' ')
r, x, y=float(r), float(x), float(y)
if x*x+y*y<=r*r:
    print('Point (%.1f, %.1f) is in the circle'%(x, y))
else :
    print('Point (%.1f, %.1f) is not in the circle'%(x, y))

