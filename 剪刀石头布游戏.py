import os

import random

def pk(i:int,j:int):        

    x = i-1

    y = i+1

    if x < 1:

        x=3

    if y > 3:

        y = 1

    if j == x:

        return '恭喜您赢了!'

    elif j == y:

        return '计算机赢.'

    elif j==i:

        return '平局'



dct = {1:'剪刀',2:'石头',3:'布'}

w=0

while w < 3:

    i = int(input('请输入1~3分别代表剪刀,石头,布：'))

    c = random.randrange(1,4)

    p = pk(i,c)

    print('计算机出%s,您出%s,%s'%(dct[c],dct[i],p))

    if p == '恭喜您赢了!':

        w+=1