class Vehicle:
    def __init__(self, color, maxspeed):
        self.color = color
        self.maxspeed = maxspeed


class Car(Vehicle):
    def __init__(self, color, maxspeed, numgears, isconvertible):
        super().__init__(color, maxspeed)
        self.numgears = numgears
        self.isconvertible = isconvertible
    def printcar(self):
        print('color:',self.color)
        print('maxspeed:',self.maxspeed)
        print('numgears:',self.numgears)
        print('isconvertible:',self.isconvertible)    
        
c=Car("red",15,3,False)
c.printcar()