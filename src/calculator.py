from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    
    @abstractmethod
    def get_area(self):
        pass

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
    
    def __init__(self, Square_side_length):
        super().__init__(Square_side_length, Square_side_length)
    
    def get_area(self):
        """
        Calculate the area of the square.

        Returns:
            float: The area of the square, calculated as the square of the side length.
        """
        return super().get_area()
    

class Triangle(Rectangle):
    
    def __init__(self, width, height):
        super().__init__(width, height)
    
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


class Equilateral_triangle(Shape):
    
    def __init__(self, width, height):
        super().__init__(width, height)
    
    def get_area(self):
        return super().get_area()

# class Hexagon(Shape):
    
#     def __init__(self, width, height):
#         super().__init__(width, height)
    
#     def get_area(self):
#         return super().get_area() / 2

