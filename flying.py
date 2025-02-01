# Simulate multiple inheritance where `FlyingCar` inherits from both `Car` and `defAirplane`. 
# Handle potential conflicts in the `move()` method.
class Aeroplane:
    def __init__(self,a):
        self.a=a
    def display(self):
        print(f"The aeroplane is {self.a}")
class Car:
    def __init__(self,b):
        self.b=b
    def display(self):
        print(f"The car is {self.b}")
class Flyingcar(Aeroplane,Car):
    def __init__(self,c,a,b):
        Aeroplane.__init__(self,a)
        Car.__init__(self,b)
        self.c=c
    def display(self):
        print(f"The car is a {self.c} {self.a}{self.b}")
c=Car("Car")
c.display()
a=Aeroplane("Flying")
a.display()
f=Flyingcar("Modern","flying","Car")
f.display()
