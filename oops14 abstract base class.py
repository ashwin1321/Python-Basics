from abc import ABC, abstractmethod

class Shape(ABC):                                   # ABC forces all its derived class to include some method that are written under @ abstractmethod

    @abstractmethod                                 # this means all the derived class must have this method compulsarily to run
    def printarea(self):
        return 0
   

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.printarea())

  