from math import pi, sqrt
from src.shape import Shape



class Rectangle(Shape):
    
    def __init__(self, width, length, *args):
        super().__init__(width, length, *args)
        self.width = width
        self.length = length
    
    def get_area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle, calculated as width times height.
        """
        return self.width * self.length
    
    def get_perimeter(self): 
        """
        Calculate the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle, calculated as twice the sum of the width and length.
        """
        return 2 * (self.width + self.length)
    

class Square(Rectangle):

    def __init__(self, Side):
        super().__init__(Side, Side)
    
    def get_area(self):
        """
        Calculate the area of the square.

        Returns:
            float: The area of the square, calculated as the square of the side length.
        """
        return super().get_area()
    

class RightAngledTriangle(Rectangle):
    
    def __init__(self, legs , hypotenuse = None):
        
        if hypotenuse is None:
            hypotenuse = sqrt(legs ** 2 + legs ** 2)
            
        super().__init__(legs , legs, hypotenuse)
        self.hypotenuse = hypotenuse
    
    def get_area(self):
        """
        Calculate the area of the right-angled triangle.

        The area of a right-angled triangle is half the product of the two legs.

        Returns:
            float: The area of the triangle.
        """
        return super().get_area() / 2
    
    def get_perimeter(self): 
        """
        Calculate the perimeter of the right-angled triangle.

        Returns:
            float: The perimeter of the triangle, calculated as the sum of the two legs and the hypotenuse.
        """
        return self.length + self.width + self.hypotenuse

        
class Circle(Shape):
    
    def __init__(self, radius):
        super().__init__(radius)
        self.radius = radius
    
    def get_area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return round(self.radius ** 2 * pi, 2)
    
    def get_perimeter(self): 
        """
        Calculate the perimeter of the circle.

        Returns:
            float: The perimeter of the circle, calculated as 2 * pi * radius.
        """
        return self.radius * 2 * pi


class EquilateralTriangle(RightAngledTriangle):
    
    def __init__(self, Side ):
        super().__init__(Side, Side)
    
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
    
    def get_perimeter(self): 
        """
        Calculate the perimeter of the equilateral triangle.

        The perimeter of an equilateral triangle is given by the formula:

        P = 3a

        where a is the side of the triangle.

        Returns:
            float: The perimeter of the triangle.
        """
        return self.width * 3


class Hexagon(EquilateralTriangle):
    
    def __init__(self,Side):
        super().__init__(Side)
    
    def get_area(self):
        """
        Calculate the area of the hexagon.

        Returns:
            float: The area of the hexagon, calculated as six times the area of the equilateral triangle .
        """
        return super().get_area() * 6
    
    def get_perimeter(self): 
        """
        Calculate the perimeter of the hexagon.

        The perimeter of a hexagon is given by the formula:

        P = 2 * 3a

        where a is the side of the triangle.

        Returns:
            float: The perimeter of the hexagon.
        """
        return super().get_perimeter() * 6
    

if __name__ == "__main__":
    print(Rectangle(2, 3))
