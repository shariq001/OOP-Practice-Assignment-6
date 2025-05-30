# Assignment 6, Question 18
# Property Decorators

class Product:
    
    def __init__(self, price):
        self._price = price
        
    @property
    def price(self):
        print("\nGetting Price...")
        return self._price
    
    @price.setter
    def price(self, value):
        print("Setting Price...")
        self._price = value
        
    @price.deleter
    def price(self):
        print("Deleting Price...\n")
        del self._price
        
p1 = Product(50000)
print(p1.price)

p1.price = 55000

print(p1.price)

del p1.price