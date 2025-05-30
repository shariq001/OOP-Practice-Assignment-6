# Assignment 6, Question 19
# Callable ( callable() ) and __call__()

class Multiplier:
    
    def __init__(self, factor):
        self.factor = factor
        
    def __call__(self, number):
        return number * self.factor
    
m1 = Multiplier(5)

# Chacking is it callable
print(callable(m1))

result = m1(10)
print(result)