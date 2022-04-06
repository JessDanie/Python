x, y= input().split(' ')
x, y=float(x), float(y)
if -5<=x <=5 and -3<=y<=3:
    print('Point (%.1f, %.1f) is in the rectangle'%(x, y))
else :
    print('Point (%.1f, %.1f) is not in the rectangle'%(x, y))

