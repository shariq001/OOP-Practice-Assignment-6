# Assignment 6, Question 7
# Access Modifiers: Public, Private and Protected

class Employee:
    
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn
        

emp1 = Employee("Muhammad Shariq", 100000, "123-456-7890")
print(emp1.name)
print(emp1._salary)
print(emp1.__ssn) # Error Protect variables cannot be accessed outside of the class