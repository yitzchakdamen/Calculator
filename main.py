from src.calculator import Rectangle, Triangle, Circle, Square
from menu import menu

def main():
    print("Hello, world!")
    c = Rectangle(10, 12)
    print(c)
    print(repr(c))
    print(c.get_area())
    
    menu().start()

if __name__ == "__main__":
    main()
