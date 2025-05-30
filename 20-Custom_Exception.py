# Assignment 6, Question 20
# Custom Exception

class MyCustomError(Exception):
    pass

def check_age(age):
    
    if age < 18:
        raise MyCustomError("Age must be 18 or older")
        
    else:
        print("Access Granted!")
        
try:
    check_age(14)
    
except MyCustomError as e:
    print("\nCustom Exception Caught: ", e)