def fun(x,*b):#b为元组
    print ('x=:',x)
    print('b=:',b)
fun(1,2,3,4,5)
fun(1)
def bar(x,**b):#b为字典
    print('x=:',x)
    print('b=:',b)
bar(1,a=2,b=3,c=3)
def find(dct,**a):
    r={k:v for k,v in a.items() if dct.get(k)==v}
    return r
d={'a':39,'b':99,'c':40,'d':100}
fr=find(d,a=1,b=99)
print(fr)
