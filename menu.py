from enum import Enum
import inspect
from src.calculator import Rectangle, RightAngledTriangle, Circle, Square, EquilateralTriangle, Hexagon

class ShapeType(Enum):
    RECTANGLE = 1
    SQUARE = 2
    TRIANGLE = 3
    CIRCLE = 4
    EQUILATERAL_TRIANGLE = 5
    HEXAGON = 6



class menu:
    
    def __init__(self,):
        self.shapes = {
            ShapeType.RECTANGLE : None,
            ShapeType.SQUARE : None,
            ShapeType.TRIANGLE : None,
            ShapeType.CIRCLE : None,
            ShapeType.EQUILATERAL_TRIANGLE : None,
            ShapeType.HEXAGON : None
            }
    
    def start(self):
        while True:
            print("=" * 10)
            print("1) Calculating shapes\n2) creating shapes\n3) Calculations between shapes\n4) Exit ")
            print("=" * 10)

            match input("Select a option: "):
                case "1": self.shapes_calculation_menu()
                case "2": self.creating_shape_menu()
                case "3": print(self.between_shapes_calculation() or "")
                case "4": break
                case _ : print("Invalid input")
                
        print("\nGoodbye")
        
        
    def shapes_calculation_menu(self):
        while True:
            if not self.print_shapes_exist(): return

            select = input("Select a shape: ")
            match select:
                case "1" | "2" | "3" | "4" | "5" | "6":
                    return self.Calculation(ShapeType(int(select)))
                case _ : print("Invalid input")
    
    def creating_shape_menu(self):
        while True:
            self.print_shapes()

            select = input("Select a shape type to create: ")
            match select:
                case "1" | "2" | "3" | "4" | "5" | "6":
                    Shape_Type: ShapeType = ShapeType(int(select))
                    print(f"Creating a {Shape_Type.name}...")
                    shape = self.creating_shape(Shape_Type)
                    print(f"{shape} is created")
                    self.shapes[Shape_Type] =shape
                    return
                case _ : print("Invalid input")
                
    def between_shapes_calculation(self):
            if not self.print_shapes_exist(): return

            select = input("Select 2 shape to calculate and a operation between separated by space, like ( 1 + 2) or ( 3 == 2) etc : ").strip().split(" ")
            try:
                match select[1]:
                    case "+": 
                        return self.shapes[ShapeType(int(select[0]))] + self.shapes[ShapeType(int(select[2]))]
                    case "-": 
                        return self.shapes[ShapeType(int(select[0]))] - self.shapes[ShapeType(int(select[2]))]
                    case "*": 
                        return self.shapes[ShapeType(int(select[0]))] * self.shapes[ShapeType(int(select[2]))]
                    case "/": 
                        return self.shapes[ShapeType(int(select[0]))] / self.shapes[ShapeType(int(select[2]))]
                    case "%": 
                        return self.shapes[ShapeType(int(select[0]))] % self.shapes[ShapeType(int(select[2]))]
                    case "**": 
                        return self.shapes[ShapeType(int(select[0]))] ** self.shapes[ShapeType(int(select[2]))]
                    case "//": 
                        return self.shapes[ShapeType(int(select[0]))] // self.shapes[ShapeType(int(select[2]))]
                    case ">": 
                        return self.shapes[ShapeType(int(select[0]))] > self.shapes[ShapeType(int(select[2]))]
                    case "<": 
                        return self.shapes[ShapeType(int(select[0]))] < self.shapes[ShapeType(int(select[2]))]
                    case ">=": 
                        return self.shapes[ShapeType(int(select[0]))] >= self.shapes[ShapeType(int(select[2]))]
                    case "<=": 
                        return self.shapes[ShapeType(int(select[0]))] <= self.shapes[ShapeType(int(select[2]))]
                    case "==": 
                        return self.shapes[ShapeType(int(select[0]))] == self.shapes[ShapeType(int(select[2]))]
                    case "!=": 
                        return self.shapes[ShapeType(int(select[0]))] != self.shapes[ShapeType(int(select[2]))]
                    case _ : print("Invalid input")
            except Exception as e:
                print("Invalid input")

                
    def creating_shape(self, shapeType:ShapeType):
        match shapeType:
            case ShapeType.RECTANGLE :
                return self.analyze_init(Rectangle)
            
            case ShapeType.CIRCLE :
                return self.analyze_init(Circle)
            
            case ShapeType.TRIANGLE :
                return self.analyze_init(RightAngledTriangle)
            
            case ShapeType.SQUARE :
                return self.analyze_init(Square)
            
            case ShapeType.EQUILATERAL_TRIANGLE :
                return self.analyze_init(EquilateralTriangle)
            
            case ShapeType.HEXAGON :
                return self.analyze_init(Hexagon)
    
    def Calculation(self, shapeType:ShapeType):
        shape = self.shapes[shapeType]
        if shape is None:
            print(F"Shape {shapeType.name} not found")
            return
        
        area = shape.get_area()
        perimeter = shape.get_perimeter()
        print(F"Calculating the area and perimeter of a {shape}...")
        print(f"Area: {area}")
        print(f"Perimeter: {perimeter}")
            
            
    def get_num(self):
        while True:
            vel = input("Select a number: ")
            try: return float(vel)
            except: print("Invalid input")

    def print_shapes(self):
        print("\n","=" * 10)
        for i in ShapeType: print(i.value,")", i.name)
        print("\n","=" * 10)
    
    def print_shapes_exist(self):
        exist = False
        print("\n","=" * 10)
        for i in ShapeType: 
            if self.shapes[i] is not None: 
                print(i.value,")", i.name)
                exist = True
        print("=" * 10, "\n")
        if not exist: print("No shapes exist")
        return exist

    def analyze_init(self,cls):

        params = inspect.signature(cls.__init__).parameters
        args = []
        
        for name, param in params.items():
            if name == 'self' or  name == "args":
                continue 

            if param.default == inspect.Parameter.empty:
                print(f"Enter the {name}")
                args.append(self.get_num())

            else:
                print(f"{name} (default: {param.default})")
                if input("Press enter 'y' to use the default value :") != "y":
                    args.append(self.get_num())
                else:
                    args.append(param.default)
                    
        return cls(*args)
            
if __name__ == "__main__":
    menu().start()
