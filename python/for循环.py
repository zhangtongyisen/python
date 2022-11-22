a='string'
b='float'
r1=zip(a,b)
print(list(r1))#以短的为界限
c=[1,2,3,4,5]
d=[5,6,7,8,9]
r2=[]
for x,y in zip(c,d):
    r2.append(x+y)
print(r2)
import random
lst=[]
for i in range(100):
    k=random.randint(1,10)
    lst.append(k)
dir={}
for k in lst:
    if k in dir:
        dir[k]+=1
    else:
        dir[k]=1
print(dir)
