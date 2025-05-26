# Using SELF

print("*" * 10, "Using self", "*" * 10)

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def display(self):
        print(f"\n- Name: {self.name} got: {self.marks} marks!\n")
    

student1 = Student("Muhammad Shariq", 98)       
student1.display() 

# ----------------------------------------------------------

# Using cls

print("*" * 10, "Using cls", "*" * 10)

class Counter:
    
    count = 0
    
    def __init__(self):
        Counter.count += 1
        
    @classmethod
    def show_count(cls):
        print(f"\n- The total number of instance created is: {cls.count}\n")
        
a = Counter()
b = Counter()
c = Counter()

Counter.show_count() # Since i created 3 instances it will print 3

# ----------------------------------------------------------

# Public Variables and Methods

print("*" * 10, "Public Variables and Methods", "*" * 10)

class Car:
    def __init__(self, brand):
        self.brand = brand
        
    def start(self):
        print(f"\n- {self.brand} is Starting...\n")
          
my_car = Car("Toyota")
print(f"\n- Car Brand: {my_car.brand}")
my_car.start()

# ----------------------------------------------------------

# Class Variables and Class Methods

print("*" * 10, "Class Variables and Class Methods", "*" * 10)

class Bank:
    bank_name = "Habib Bank Limited"
    
    def __init__(self, account_holder):
        self.account_holder = account_holder  
    
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
        
    def show_details(self):
        print(f"\n- Bank Name: {Bank.bank_name} | Account Holder: {self.account_holder}\n")
        
account1 = Bank("Muhammad Shariq")
account1.show_details()

# ----------------------------------------------------------

# Static Variables and Static Method

print("*" * 10, "Static Variables and Static Methods", "*" * 10)

class MathUtils:
    
    @staticmethod
    def add(a, b):
        result = a + b
        print(f"\n- The sum of {a} and {b} is: {result}\n")
    
MathUtils.add(5, 10)

# ----------------------------------------------------------

# Constructor and Destructors

print("*" * 10, "Constructor and Destructors", "*" * 10)

class Logger:
    
    def __init__(self):
        print("\n- Object Created! 'Constructor'\n")
        
    def __del__(self):
        print("\n- Object Destroyed! 'Destructor'\n")
        
obj1 = Logger()
del obj1

# ----------------------------------------------------------

# Access Modifiers: Public, Private, and Protected

print("*" * 10, "Access Modifiers: Public, Private, and Protected", "*" * 10)

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn
        
emp1 = Employee("Muhammad Shariq", 100000, "123-45-6789")

print(f"\n- Employee Name: {emp1.name} 'Public'\n") # Accessing public variable

print(f"\n- Employee Salary: {emp1._salary} 'Protected'\n") # Accessing protected variable
        
# ----------------------------------------------------------

# The super() Function

print("*" * 10, "The super() Function", "*" * 10)

class Person:
    
    def __init__(self, name):
        self.name = name
        
class Teacher(Person):
    
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        
    def show_info(self):
        print(f"\n- Teacher Name: {self.name} | Subject: {self.subject}\n")
        
teacher1 = Teacher("Muhammad Shariq", "Biology")
teacher1.show_info()

# ----------------------------------------------------------

# Abstract Classes and Methods

print("*" * 10, "Abstract Classes and Methods", "*" * 10)

from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
class Rectangle(Shape):
    
    def __init__(self, width, length):
        self.width = width
        self.length = length
        
    def area(self):
        return self.width * self.length
    
rectangle1 = Rectangle(5, 10)
print(f"\n- Area of Rectangle is {rectangle1.area()}\n")

# ----------------------------------------------------------

# Instance Methods

print("*" * 10, "Instance Methods", "*" * 10)

class Dog:
    
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
    def bark(self):
        print(f"\n- {self.name} (Breed: {self.breed}) is barking!\n")
        
dog1 = Dog("Tommy", "American Eskimo")
dog1.bark()