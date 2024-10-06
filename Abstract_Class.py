from abc import ABC, abstractmethod
class Automobile(ABC):
    def __init__(self) :
        print("Automobile Created")
    
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
    @abstractmethod
    def drive(self):
        pass
# c=Automobile()    This will give error because we cannot create object of abstract class
class Car(Automobile):
    def __init__(self,name):
        print('Car Created')
        self.name=name
    def start(self):
        pass
    def stop(self):
        pass
    def drive(self):
        pass

c=Car('Honda')  
      