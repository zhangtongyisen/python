import os
print(os.getcwd())#查看默认路径
f=open("test.txt","w")#保存在默认路径 可写入
f.write("hello world")
f.close()
with open ('test.txt','a') as f:
    f.write('!!!')#在后面追加文字
f=open('test.txt')
for line in f:
    print(line)
