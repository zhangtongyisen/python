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
lst=[1,5,3,20,6,2,7]
print(list(enumerate(lst)))
for i,ele in enumerate(lst):
      if ele%2==0:
        lst[i]='even'#i为索引，ele为元素
print(lst)
s='Life is short You need python love'
f={}
for i in s:
    if i.isalpha():
        if i.isupper():
            i=i.lower()
        if i in f:
                f[i]+=1
        else:
                f[i]=1
print (f)
print([i**2 for i in range(10)])
