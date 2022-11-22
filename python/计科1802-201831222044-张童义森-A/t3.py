def f1(s):
    a=0
    b=0
    x=[int(i) for i in s]
    for i in x:
        a=a+i
        b=b+1
    return a,b
list=input().split(",")
y=[int(i) for i in list]
print(f1(list))
