class MyList:
    def __init__(self,num):
        self.num=num
    def add(self,a):
        for i in range(len(self.num)):
            self.num[i]=self.num[i]+a.num[i]
        print(self.num)
x=MyList([1,2,3,4])
y=MyList([5,6,7,8])
x.add(y)
