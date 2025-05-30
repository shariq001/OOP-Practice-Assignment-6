# Assignment 6, Question 10
# Instance Methods

class Dog:
    
    def __init__(self, name, breed):
        self.name = name 
        self.breed = breed
        
    def bark(self):
        print(f"\n- The {self.name} ({self.breed}) is barking!")
        
dog1 = Dog("Tommy", "Husky")
dog1.bark()