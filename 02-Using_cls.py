# Assignment 6, Question 2
# Using cls

class Counter:
    
    count = 0 # class variable
    
    def __init__(self):
        Counter.count += 1
        
    @classmethod
    def show_count(cls):
        print(f"\n- The total number of instance created is {cls.count}")
        
a = Counter()
b = Counter()
c = Counter()

Counter.show_count()