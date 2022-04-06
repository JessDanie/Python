x, y= input().split(' ')
x, y=float(x), float(y)
x=y/(x*x)
if x <18.5:
    print('%.1f'%x,'Underweight')
elif x <24:
    print('%.1f'%x,'Normal')
elif x <28:
    print('%.1f'%x,'Overweight')
else:
    print('%.1f'%x,'Obese')
