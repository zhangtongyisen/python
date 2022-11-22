import random
import math
import decimal
b=decimal.Decimal('0.1')
m=decimal.Decimal('0.2')
print(b+m)
n=random.randint(1,10)
if n>math.pi:
    l=n*math.pi
    a=math.pi*(n/2)**2
else:
    l=2*math.pi*n
    a=math.pi*n*n
print(n)
print('周长是：',round(l,2))
print('面积是：',round(a,2))
