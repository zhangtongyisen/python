class student:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_course(self):
        return max(self.course)
s1=student("Tom",18,[90,95,80])
print(s1.get_name())
print(s1.get_age())
print(s1.get_course())
