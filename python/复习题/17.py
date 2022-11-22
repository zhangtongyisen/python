class Listinfo:
    def __init__(self,a):
        self.list=a
    def add_key(self,keyname):
        self.list.append(keyname)
        return self.list
    def get_key(self,num):
        if num>=0 and num<len(self.list):
            return self.list[num]
        else:
            return 'error'
    def update_list(self,list):
        self.list+=list
        return self.list
    def del_key(self):
        if len(self.list)>0:
            return self.list.pop()
        else:
            return 'error'
list1=Listinfo([1,2,3,4,'aaa','bbb'])
print(list1.add_key('ccc'))
print(list1.get_key(1))
print(list1.update_list([5,'ss']))
print(list1.del_key())
