"""
OOP: object oriented programming
    class/object
    attributes/methods
    inheritance
    encapsulation/absctrack
    overriding/polymorhism
"""
from abc import ABC, abstractmethod
#inheritance
#parent
class Shape(ABC):
    """
    Shape = super class/abstrack class
    """
    @abstractmethod
    def area(self):pass
    @abstractmethod
    def perimeter(self):pass
    # overriding/polymorhism
    def tostring(self):pass

class Sguare(Shape):
    "sub class"
    def __init__(self,edge):
        self.__edge=edge  # iki alt çizgi koyarak encapsulation yaptık yani dışardan erişim olmayacak
    def area(self):
        result=self.__edge ** 2
        print("sguare area :",result)
    def perimeter(self):
        result=self.__edge * 4
        print("sguare perimeter :" ,result)
    def tostring(self):
        "polymorhism kullandık to stringde yukarada pass idi burda "
        print("sguare edge :" ,self.__edge)
#child
class Circle(Shape):
    "constant variable"
    PI=3.14
    def __init__(self,radius):
        self.__radius=radius

    def area(self):
        result=self.PI*self.__radius ** 2
        print("circle area :",result)

    def perimeter(self):
        result=2*self.PI*self.__radius  #2 * pi ** 2
        print("circle perimeter :",result)
    def tostring(self):
        print("circle radius :",self.__radius)
c = Circle(5)
c.area()
c.perimeter()
c.tostring()
"---------------------------------"
s=Sguare(4)
s.area()
s.tostring()
s.perimeter()














