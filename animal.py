from abc import ABC,abstractmethod
class Animal:
    @abstractmethod
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        print("The dog is barking.....")
class Cat(Animal):
    def speak(self):
        print("The cat is meowing...")
def myfun(obj):
    obj.speak()
d=Dog()
myfun(d)
c=Cat()
myfun(c)