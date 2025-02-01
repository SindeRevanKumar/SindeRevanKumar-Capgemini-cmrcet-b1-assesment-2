# # 6. Implement a multi-level inheritance example where `Vehicle` is a base class, `Car` and `Bike` 
# # inherit from `Vehicle`, and `ElectricCar` inherits from `Car`.
class Vehicle:
    def __init__(self,name,cc):
        self.name=name
        self.cc=cc
    def display(self):
        print(f"the name is {self.name}\nthe cc is {self.cc}")
class Bike(Vehicle):
    def __init__(self,name,cc,registration):
        super().__init__(name,cc)
        self.registration=registration
    def displayy(self):
        print(f"the name is {self.name}\nthe cc is {self.cc}\nthe registration is {self.registration}")
class Car(Bike):
    def __init__(self,chasis,registration,name,cc):
        super().__init__(registration,name,cc)
        self.chasis=chasis
    def displayyy(self):
        print(f"the name is {self.name}\nthe cc is {self.cc}\nthe registration is {self.registration}\nthe chasis is {self.chasis}")
c=Car("12","Ts19c1516","Honda","1250cc")
c.displayyy()




