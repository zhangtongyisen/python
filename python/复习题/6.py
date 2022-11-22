import math
def isPrime(x):
    for i in range(2,int(math.sqrt(x)+1)):
        if x%i == 0:
            return False
    return True
 
data=[2, 3] 
for i in range(1,5):
    for j in range(1,5):
        if i!=j:
            data.append(i*10+j)
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and j!=k and i!=k:
                data.append(i*100+j*10+k)
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            for m in range(1,5):
                if i!=j and i!=k and i!=m and j!=k and j!=m and k!=m:
                    data.append(i*1000+j*100+k*10+m)
for i in data:
    if isPrime(i):
        print(i)
