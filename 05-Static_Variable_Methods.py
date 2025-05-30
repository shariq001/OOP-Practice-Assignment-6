# Assignment 6, Question 5
# Static Variable and Static Methods

class MathUtils:
    
    @staticmethod
    def add(a, b):
        result = a + b
        print(f"\n- The Result of [ {a} + {b} = {result} ]")
        
MathUtils.add(5, 10)