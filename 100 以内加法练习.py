import os

import random

i = int(input('请输入练习题数量：'))

x = 0

while x < i:

    t1 = random.randrange(1,101)

    t2 = random.randrange(1,101)

    print("%d + %d= ? "%(t1, t2),end = '')

    h = int(input(''))

    while h != t1+t2:

        print("%d + %d= ? %d 不对，请重新计算"%(t1, t2, h))

        print("%d + %d= ? "%(t1, t2),end = '')

        h = int(input(''))

    x+=1

print('恭喜你完成此次加法练习！')