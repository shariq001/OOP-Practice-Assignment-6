# Assignment 6, Question 12
# Static Methods

class TemperatureConverter:
    
    @staticmethod
    def celcius_to_fahrenheit(c):
        
        fahreinheit = (c * 9/5) + 32
        print(f"\n- The {c}C in Fahrenheit is {fahreinheit}")
        
TemperatureConverter.celcius_to_fahrenheit(47)