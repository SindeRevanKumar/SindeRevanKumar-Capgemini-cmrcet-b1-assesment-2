class Electronics:
    def __init__(self,price):
        self.price=price
    def display(self):
        print(f"The mobile price is {self.price}")
class Mobiledevice(Electronics):
    def __init__(self,model,price):
        super().__init__(price)
        self.model=model
    def displayy(self):
        print(f"The {self.model} is costing {self.price}...")
class Smartphone(Mobiledevice):
    def __init__(self,smart,model,price):
        super().__init__(model,price)
        self.smart=smart
    def displayyy(self):
        print(f"the {self.model} {self.smart} is costing {self.price}")
s = Smartphone("Smart", "iPhone 13", 50000)  
s.display()
s.displayy()
s.displayyy()  
