# Assignment 6, Question 21
# Custom Class Iterable

class Countdown:
    
    def __init__(self, start):
        self.start = start
        self.current = start
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        
        value = self.current
        self.current -= 1
        
        return value
    
for num in Countdown(10):
    print(num)