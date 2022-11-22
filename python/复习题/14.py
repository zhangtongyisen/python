n=int(input("输入n："))
x=input("输入n个数（空格隔开）:").split()
x=[int(i) for i in x]
x.sort()
minx=x[1]-x[0]
for i in range(2,len(x)):
    t=x[i]-x[i-1]
    if(t<minx):
        minx=t
print(minx)
