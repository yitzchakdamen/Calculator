from __future__ import annotations
from abc import ABC, abstractmethod
import inspect

class Shape(ABC):
    
    def __new__(cls, *args):
        print (f"__new__ magic method is called by {cls.__name__}")
        inst = object.__new__(cls)
        return inst
    
    def __init__(self,*args):
        self.args = args
        for arg in self.args:
            if not isinstance(arg, (int, float)):
                raise TypeError("must be integers or floats.")
            elif arg <= 0:
                raise ValueError("must be positive numbers.")

    def __str__(self):
        sig = inspect.signature(self.__class__.__init__)
        params = list(sig.parameters.keys())[1:]
        args_dict = {name: getattr(self, name, "") for name in params}
        return f"shape {self.__class__.__name__} with --- {", ".join(f"{kye}: {val}" for kye, val in args_dict.items() if kye != 'args')}"
    
    def __repr__(self):
       return f"{self.__class__.__name__} {self.args}"
   
    @abstractmethod
    def get_area(self):
        pass
    
    @abstractmethod
    def get_perimeter(self): 
        pass

    def __hash__(self):
        return hash((self.__class__, self.get_area(), self.get_perimeter()))

    def __add__(self, other:Shape):	#To get called on add operation using + operator
        if isinstance(other, Shape): return self.get_area() + other.get_area()
        else: return NotImplemented
    
    def __sub__(self, other):	#To get called on subtraction operation using - operator.
        if isinstance(other, Shape): return self.get_area() - other.get_area()
        else: return NotImplemented
    
    def __mul__(self, other):	#To get called on multiplication operation using * operator.
        if isinstance(other, Shape): return self.get_area() * other.get_area()
        else: return NotImplemented
    
    def __floordiv__(self, other):	#To get called on floor division operation using // operator.
        if isinstance(other, Shape): return self.get_area() // other.get_area()
        else: return NotImplemented
    
    def __truediv__(self, other):	#To get called on division operation using / operator.
        if isinstance(other, Shape): return self.get_area() / other.get_area()
        else: return NotImplemented
    
    def __mod__(self, other):	#To get called on modulo operation using % operator.
        if isinstance(other, Shape): return self.get_area() % other.get_area()
        else: return NotImplemented
    
    def __pow__(self, other):	#To get called on calculating the power using ** operator.
        if isinstance(other, Shape): return self.get_area() ** other.get_area()
        else: return NotImplemented
    
    def __lt__(self, other):	#To get called on comparison using < operator.
        if isinstance(other, Shape): return self.get_area() < other.get_area()
        else: return NotImplemented

    def __gt__(self, other):	#To get called on comparison using > operator.
        if isinstance(other, Shape): return self.get_area() > other.get_area()
        else: return NotImplemented
    
    def __le__(self, other):	#To get called on comparison using <= operator.
        if isinstance(other, Shape): return self.get_area() <= other.get_area()
        else: return NotImplemented
    
    def __eq__(self, other):	#To get called on comparison using == operator.
        if isinstance(other, Shape): return self.__class__ == other.__class__ and self.get_area() == other.get_area() and self.get_perimeter() == other.get_perimeter()
        else: return NotImplemented
    
    def __ne__(self, other):	#To get called on comparison using != operator.
        return not self.__eq__(other)
    
    def __ge__(self, other):	#To get called on comparison using >= operator.
        if isinstance(other, Shape): return not self.get_area() >= other.get_area()
        else: return NotImplemented
    
    