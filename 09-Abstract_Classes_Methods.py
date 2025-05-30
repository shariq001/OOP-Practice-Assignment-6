# Assignment 6, Question 9
# Abstract Class and Methods

from abc import ABC, abstractmethod

class Shape(ABC):
    def area(self):
        pass
    
class Rectangle(Shape):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
rect1 = Rectangle(51, 10)
print(f"\n- The Area of Trianlge is '{rect1.area()}'")