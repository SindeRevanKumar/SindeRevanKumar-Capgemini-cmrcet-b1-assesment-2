# 5. Create a `Product` class with attributes `name`, `price`, and `stock`. 
# Write a method `check_availability(quantity)` that returns whether the requested quantity is available.

class Market:
    def __init__(self,initial_stock=10):
        self.initial_stock=initial_stock
    def product(self,name,price,required):
        self.name=name
        self.price=price
        self.required=required
    def check(self):
        if self.initial_stock>self.required:
            print(f"the {self.name} are  available...")
        else:
            print(f"{self.required} are not avilable only {self.initial_stock} {self.name} are available...and price is {self.required*self.price}")
M=Market()  
M.product("banana",6,12)
M.check()
