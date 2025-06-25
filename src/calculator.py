from __future__ import annotations
from abc import ABC, abstractmethod
from math import pi, sqrt


class Shape(ABC):
    def __new__(cls, width, Length):
        print (f"__new__ magic method is called by {cls.__name__}")
        inst = object.__new__(cls)
        return inst
    
    @abstractmethod
    def __str__(self):
        pass
    
    @abstractmethod
    def __repr__(self):
       pass
   
    @abstractmethod
    def get_area(self):
        pass

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
        if isinstance(other, Shape): return self.get_area() == other.get_area()
        else: return NotImplemented
    
    def __ne__(self, other):	#To get called on comparison using != operator.
        if isinstance(other, Shape): return self.get_area() != other.get_area()
        else: return NotImplemented
    
    def __ge__(self, other):	#To get called on comparison using >= operator.
        if isinstance(other, Shape): return self.get_area() >= other.get_area()
        else: return NotImplemented
    
    


class Rectangle(Shape):
    
    def __init__(self, width, Length):
        self.width = width
        self.Length = Length
        
    def __str__(self):
        return f"{self.__class__.__name__} with ---  width: {self.width},  Length: {self.Length}"
    
    def __repr__(self):
        return f"{self.__class__.__name__}( {self.width}, {self.Length} )"
    
    def get_area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle, calculated as width times height.
        """
        return self.width * self.Length
    

class Square(Rectangle):

    def __init__(self, width, height):
        super().__init__(width, height)
    
    def get_area(self):
        """
        Calculate the area of the square.

        Returns:
            float: The area of the square, calculated as the square of the side length.
        """
        return super().get_area()
    

class Triangle(Rectangle):
    
    def __init__(self, legs , hypotenuse = None):
        super().__init__(legs , legs )
        self.hypotenuse = hypotenuse
        
    def __str__(self):
        return f"{self.__class__.__name__} with ---  Legs: ({self.width}, {self.Length}),  Hypotenuse: {self.hypotenuse}"
    
    def __repr__(self):
        return f"{self.__class__.__name__}( {self.width}, {self.hypotenuse} )"
    
    def get_area(self):
        """
        Calculate the area of the triangle.

        Returns:
            float: The area of the triangle, calculated as half the base times the height.
        """
        return super().get_area() / 2
        
class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius
    
    def __str__(self):
        return f"{self.__class__.__name__} with ---  radius: {self.radius}"
    
    def __repr__(self):
        return f"{self.__class__.__name__}( {self.radius} )"
    
    def get_area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return round(self.radius ** 2 * pi, 2)


class Equilateral_triangle(Triangle):
    
    def __init__(self, Side ):
        super().__init__(Side, Side)
        
    def __str__(self):
        return f"{self.__class__.__name__} with ---  Side:( {f"{self.width}, " * 3 } )"
    
    def __repr__(self):
        return f"{self.__class__.__name__}( {self.width} )"
    
    def get_area(self):
        """
        Calculate the area of the equilateral triangle.

        The area of an equilateral triangle is given by the formula:

        A = (a^2 * sqrt(3)) / 4

        where a is the side of the triangle.

        Returns:
            float: The area of the triangle.
        """
        return (self.width ** 2) * (sqrt(3) / 4)


class Hexagon(Equilateral_triangle):
    
    def __init__(self,Side):
        super().__init__(Side, Side)
    
    def __str__(self):
        return f"{self.__class__.__name__} with ---  Side:( {f"{self.width}, " * 6 } )"
    
    def get_area(self):
        """
        Calculate the area of the hexagon.

        Returns:
            float: The area of the hexagon, calculated as six times the area of the equilateral triangle .
        """
        return super().get_area() * 6


if __name__ == "__main__":
    print(Rectangle(4,5) == Rectangle(5,4))
