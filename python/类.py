class Student:
    def __init__(self,name,grade,subject):
        self.name=name
        self.grade=grade
        self.subject=subject

    def shijian(self,time):
        if self.grade > 3 and time>2:
            return True
        elif self.grade<3 and time>1:
            return False
        else:
            return False
class Teacher:
    def __init__(self,name,subject):
        self.name=name
        self.subject=subject
    def pingjia(self,result=True):
        if result:
            return "You are great"
        else:
            return "you should work hard"
stu_zhang=Student('zhang',5,'math')
tea_wang=Teacher('wang','math')
said=tea_wang.pingjia(stu_zhang.shijian(1))
print("Teacher {0} said: {1},{2}".format(tea_wang.name,stu_zhang.name,said))
