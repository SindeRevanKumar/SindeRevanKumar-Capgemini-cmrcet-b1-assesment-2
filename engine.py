from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started") 
    def stop_engine(self):
        print("Car engine stopped")
class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started")
    def stop_engine(self):
        print("Bike engine stopped")
class Truck(Vehicle):
    def start_engine(self):
        print("Truck engine started")
    def stop_engine(self):
        print("Truck engine stopped")

car = Car()
car.start_engine()
car.stop_engine()

bike = Bike()
bike.start_engine()
bike.stop_engine()

truck = Truck()
truck.start_engine()
truck.stop_engine()