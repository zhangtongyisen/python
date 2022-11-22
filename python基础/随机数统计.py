import random
lst=[]
for i in range(100):
    n=random.randint(0,9)
    lst.append(n)
d={}
for n in lst:
    if n in d:
        d[n]+=1
    else:
        d[n]=1
print(lst)
print(d)
