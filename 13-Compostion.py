# Assignment 6, Question 13
# Composition

class Engine():
    def start(self):
        print("\n- Engine is starting")
        
        
class Car():
    def __init__(self):
        self.engine = Engine()
        
    def drive(self):
        self.engine.start()
        print("- The car is moving...\n")
        
c1 = Car()
c1.drive()