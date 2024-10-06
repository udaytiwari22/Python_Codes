class Student:
    def __init__(self,name,age):
        self.name=name
        self.age = age
    def krkeDikha(self):
        return (self.name)
    staticmethod
    def welcome():
        print("Hello Student")
    
    
    def vehicle(cls,salutation,name,age):
        return cls(salutation+name,age)
        
        
class Car:
    def __init__(self,name,age):
        self.name="Car "+name
        self.age = age

class Bike:
    def __init__(self,name,age):
        self.name="Bike "+name
        self.age = age


s1= Student("Uday",21)
print(type(s1))
s2=Student("Uday","21").krkeDikha()
print(s2)