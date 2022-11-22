name=input("your name is:")
old=input("your old is:")
old=int(old)
n=old+10
print(name,n)
a=" we love python! "
lst=a.split(" ")
l=a.strip(" ")
print(l)
print(lst)
print("-".join(lst))
print("I like {1:^10} and {0:>15}".format("python","money"))#1,0代表顺序":"代表宽度">"代表右对齐，数字默认右对齐"d"代表整数“f”代表实数
t=a.index('e')
d=a.index('e',5)
print(t)
print(d)
s=a[2:9]
b=a[::-1]
m=a[2:9:3]#要注意方向和顺序
print(s)
print(b)
print(m)
print("she is {0:^4d} years old and {1:.2f}m in height".format(28,1.68))
k=[2,3,1,6]
print(k)
if 2 in k:
    print('hh')
    k[1]=100
    print(k)
    k.append('book')
    k.insert(0,29)
    k.extend('book')
    print(k)
    print(k.pop(2))#默认删除最后一个值
    print(k)
    k.remove(29)
    k.remove('b')#默认从左到右第一个出现的
    print(k)
lst2=[1,4,3,5,6,8,2,3]
lst2.sort()
print(lst2)
lst2.sort(reverse=True)#等于lst2.reverse()等于lst2[::-1]
print(lst2)
p='python'
o=list(p)
print(o)
print(''.join(o))#列表转化为字符串
