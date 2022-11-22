def opt(func,seq):
    r=[func(i) for i in seq]
    print(r)
opt(abs,range(-5,5))
a=1
def f1():
    global a
    a=a+1
    print(a)
f1()
def foo():
    a=1
    def bar():
        nonlocal a
        a=a+1
        print(a)
    bar()
foo()
def w(m,g):
    return m*g
def weight(g):
    def cal(m):
        return m*g
    return cal
w=weight(10)
G=w(100)
print (G)
