# Assignment 6, Question 3
# Public Variables and Methods

class Car:
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def start(self):
        print(f"\n- Starting the car {self.brand} {self.model}")
        
my_car = Car("Honda", "HR-V")

print(f"\n- My Car is {my_car.brand} {my_car.model}")
my_car.start()