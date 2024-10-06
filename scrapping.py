class Mother:
    def __init__(self):
        self.name = 'Manju'

    def print(self):
        print("print of mother is called")


class Father:
    def __init__(self):
        self.name = 'Ajay'

    def print(self):
        print("print of father is called")


class Child(Father, Mother):
    def __init__(self):
        super().__init__()

    def printchild(self):
        print('Name of child is', self.name)


c = Child()
# c.printchild()
print(Child.mro())

