d=dict(a=1,b=2,c=3)
print(d)
print(d['a'])
d['b']=5
print(d)
print(len(d))
del d['c']
print(d)
s=dict([('a',1),('name','python')])
print(s)
print(s.get('b','hh'))
s.setdefault('n')
print(s)
s.setdefault('m','ko')
print(s)
if(s.get('v')==None):
    print("true")#循环了四次
s.update(j=50,io=90)
print(s)
s.pop('a')
print(s)
print(s.pop('a','e'))
l={'a': 1, 'name': 'python', 'n': None}
for t in l:
    print(t,l[t])#t为键，l[t]为键值
dt={}
for t in l:
    dt[l[t]]=t
print(dt)
a2,*b1=1,2,3,4
print(a2,b1)
