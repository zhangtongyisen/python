def p(func):
    def w(name):
        return '<p>{0}</p>'.format(func(name))
    return w
@p
def book(name):
    return 'the name of my book is {0}'.format(name)
py=book('hh')
print (py)
import time
def func(func):
    def wrapper():
        start=time.time()
        func()
        stop=time.time()
        return stop-start
    return wrapper
@func
def append():
    lst=[]
    for i in range(1000000):
        lst.append(i)
@func
def compare():
    lst=[i for i in range(1000000)]
a=append()
b=compare()
print('普通创建列表：{0} and 高级创建列表：{1}'.format(a,b))
print('两者比率：',round(a/b,3))
