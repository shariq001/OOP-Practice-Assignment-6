# Assignment 6, Question 6
# Constructor and Destructor

class Logger:
    
    def __init__(self):
        print(f"\n- Object Created!")
        
    def __del__(self):
        print(f"\n- Object Destroyed!")
        
obj1 = Logger()
del obj1