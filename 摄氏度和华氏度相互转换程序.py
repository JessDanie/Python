y=input()
if y[-1] == 'F':
    y1=float(y[:-1])
    print('F=%.2f'%(1.8*y1+32))
elif y[-1] == 'C':
    y1=float(y[:-1])
    print('C=%.2f'%((y1-32)/1.8))
