from enum import Enum
from src.calculator import Rectangle, RightAngledTriangle, Circle, Square

class ShapeType(Enum):
    RECTANGLE = 1
    SQUARE = 2
    TRIANGLE = 3
    CIRCLE = 4
    EQUILATERAL_TRIANGLE = 5
    HEXAGON = 6


class menu:
    
    def __init__(self, ):
        pass
    
    def start(self):
        print("\n_____ Welcome to Trouble Calculator _____\n")
        
        while True:
            print("=" * 10)
            print("1) Calculating Trouble\n2) Exit")
            print("=" * 10)

            match input("Select a option: "):
                case "1": self.shapes_menu()
                case "2": break
                case _ : print("Invalid input")
                
        print("Goodbye")
        
        
    def shapes_menu(self):
        while True:
            print("=" * 10)
            for i in ShapeType: print(i.value,")", i.name)
            print("=" * 10)

            select = input("Select a shape: ")
            match select:
                case "1" | "2" | "3" | "4" | "5" | "6":return self.Calculation(ShapeType(int(select)))
                case _ : print("Invalid input")
    
    
    def Calculation(self, shapeType:ShapeType):
        print(shapeType.name)
        match shapeType:
            case ShapeType.RECTANGLE :
                pass
            case ShapeType.CIRCLE :
                pass
            case ShapeType.TRIANGLE :
                pass
            case ShapeType.SQUARE :
                pass
            case ShapeType.EQUILATERAL_TRIANGLE :
                pass
            case ShapeType.HEXAGON :
                pass

            
            
if __name__ == "__main__":
    menu().start()