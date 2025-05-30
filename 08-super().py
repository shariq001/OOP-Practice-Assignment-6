# Assignment 6, Question 8
# Super Function super()

class Person:
    
    def __init__(self, name):
        self.name = name
        
class Teacher(Person):
    
    def __init__(self, name, subject_field):
        super().__init__(name)
        self.subject_field = subject_field
        
    def show_details(self):
        print(f"\n- Teacher Name: {self.name} | Subject Field: {self.subject_field}")
        
teacher1 = Teacher("Hamza Syed", "Python")
teacher1.show_details()