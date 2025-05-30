# Assignment 6, Question 16
# Function Decorator

def log_function_call(func):
    
    def wrapper():
        print("\nFunction is Called (Before)")
        func()
        print("Function is Called (After)\n")
        
    return wrapper

@log_function_call
def say_hello():
    print("Hello Function Decorator")
    
say_hello()