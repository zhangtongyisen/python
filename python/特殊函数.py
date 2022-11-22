lam=lambda x:x+3
print(lam(2))
def add(x):
    x+=3
    return x
print(add(2))
m=map(lambda x:x+3,range(10))
print(list(m))
lst1=[1,2,3,4,5]
lst2=[6,7,8,9,0]
lst3=[7,8,9,2,1]
print([x+y+z for x,y,z in zip(lst1,lst2,lst3)])
r=map(lambda x,y,z:x+y+z,lst1,lst2,lst3)
print(list(r))
n=range(-5,5)
f=filter(lambda x:x>0,n)
print(list(f))
