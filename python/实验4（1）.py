class MyArray:
    def __init__(self):
        self.arr=[]
        m=int(input("请输入行数"))
        n=int(input("请输入列数"))
        for i in range(0,m,1):
              self.arr.append([])
              for j in range(n):
                  x=int(input("请输入"))
                  self.arr[i].append(x)
    def __add__(self,my2):
        my3=[]
        for k in range(0,len(self.arr),1):
                       my3.append([])
                       for i,j in zip(self.arr[k],my2.arr[k]):
                               my3[k].append(i+j)
        return my3
                  
    def __mul__(self,my2):
        my3=[]
        for k in range(0,len(self.arr),1):
            my3.append([])
            for m in range(0,len(self.arr),1):
                sum=0
                for n in range(0,len(my2.arr[0]),1):
                    sum+=self.arr[m][n]*my2.arr[n][m]
                my3[k].append(sum)
        return my3
    def __sub__(self,my2):
        my3=[]
        for k in range(0,len(my2.arr),1):
                       my3.append([])
                       for i,j in zip(self.arr[k],my2.arr[k]):
                               my3[k].append(i-j)
        return my3
    
my1=MyArray()
print("输入与my1一样的行与列")
my2=MyArray()
l1=len(my2.arr)
l2=len(my1.arr)
print("数组相加")
for i in range(0,l1,1):
    print(my1.__add__(my2)[i])
print("数组相减")
for i in range(0,l1,1):
    print(my1.__sub__(my2)[i])
print("数组相乘")
for i in range(0,l2,1):
    print(my1.__mul__(my2)[i])

