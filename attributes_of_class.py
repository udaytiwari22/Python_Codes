
class student:
    
    # def __init__(self,name):
    #     self.name=name
    def studentdetails(self,name):
        self.name=name
        return name
    
    staticmethod
    def welcome():
        print('Hey Welcome to this Program')
# s=student('abc')
# s1=student('def')
# s2=student('sdf')
# s.pp=70  
# print(s.pp)
# print(s1.pp)
# print(s.__dict__)    
# print(s1.__dict__)
# print(id(s.pp),id(s1.pp),id(s2.pp))
s1=student()
# print(s1.studentdetails('ghjj'))
student.welcome()