x1, y1= input().split(' ')
x2, y2= input().split(' ')
x1, y1, x2, y2=int(x1), float(y1), int(x2), float(y2)
if x1/y1 > x2/y2:
    print(x1, y1)
else:
    print(x2, y2)

