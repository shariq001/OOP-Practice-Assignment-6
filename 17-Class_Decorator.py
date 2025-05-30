# Assignment 6, Question 17
# Class Decorator

def add_greeting(cls):
    
    def greet(self):
        return "\n- Hello from Decorator!\n"
    
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name
        
p = Person("Muhamamd Shariq")
print(p.greet())