class Student:
    def __init__(self , name , rollnumber):
        self.name = name
        self.rollNumber=rollnumber
    def printstudent(self):
        print('My name is',self.name,'My roll number is', self.rollNumber)    
s1=Student('Ankush',12)
# print(s1.__dict__)
s2=Student('Rohan',13)    
# print(s2.__dict__)   
s1.printstudent()
Student.printstudent(s2) 