a=0
while a<3:
    s=input('input your lang:')
    if s=='python':
        print ('your lang is {0}'.format(s))
        break
    else:
        a+=1
        print('a=',a)
print ('the end a is: ',a)#遇到continue是跳到循环最后一行的后面
import random
number=random.randint(1,100)
while 1:
    num=input('input a number:')#输入的是字符串
    if not num.isdigit():#判断输入是否为数字
        print('please input interger')
    elif int(num)<0 or int (num)>=100:
        print ('the number should be in 1 to 100')
    else:
        if number==int(num):
            print('you are right！！!')
            break
        elif number>int (num):
            print('your number is smaller')
        else:
            print ('your number is bigger')
