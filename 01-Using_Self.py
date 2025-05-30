# Assignment 6, Question 1
# Using Self

class Student:
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def display(self):
        print(f"\n- The Student {self.name} got {self.marks} marks!")
        
student1 = Student("Muhammad Shariq", 95)
student2 = Student("Adeel", 89)

student1.display()
student2.display()