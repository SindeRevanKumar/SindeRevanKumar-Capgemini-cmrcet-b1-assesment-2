#  Develop a `Shape` class with a method `area()`. Implement `Square` and `Triangle` classes that provide 
# specific implementations for `area()`.
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self,**kwargs):
        pass
class Square(Shape):
    def area(self,**kwargs):
        length=kwargs.get("length")
        print(f"the area of square is {(length*length)}")
class Triangle(Shape):
    def area(self,**kwargs):
        length=kwargs.get("length")
        height=kwargs.get("height")
        print(f"the area of square is {0.5*length*height}")
s=Square()
s.area(length=4)
t=Triangle()
t.area(length=1,height=2)
