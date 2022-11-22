def count(s):
    a=0
    b=0
    c=0
    d=0
    for i in s:
        if i.isupper():
            a=a+1
        elif i.islower():
            b=b+1
        elif i.isdigit():
            c=c+1
        else:
            d=d+1
    return a,b,c,d
x=input()
print(count(x))
