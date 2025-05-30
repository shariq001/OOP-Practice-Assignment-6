# Assignment 6, Question 14
# Aggregation

class Department:
    
    def __init__(self, name):
        self.name = name
        
class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department
        
    def show(self):
        print(f"\n- Employee: {self.name} | Department: {self.department.name}")
        
        
dept1 = Department("Artificial Intelligence")
dept2 = Department("Data Science")

emp1 = Employee("Muhammad Shariq", dept1)
emp2 = Employee("Adeel", dept2)

emp1.show()
emp2.show()