import math
def prime(x):
    k=int(math.sqrt(x)+1)
    for i in range(2,k):
        if(x%i==0):
            return "NO"
    return "YES"
print(prime(7))
