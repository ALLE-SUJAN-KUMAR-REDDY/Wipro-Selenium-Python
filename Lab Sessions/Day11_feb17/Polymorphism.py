# 1. Create a Shape class with method area(). Implement Circle and Rectangle.

class Shape:
    def area(self):
        print("Area of shape")

class Circle(Shape):
    def area(self, radius):
        return 3.14 * radius * radius

class Rectangle(Shape):
    def area(self, length, width):
        return length * width

# Object Creation & Method Calls

shape = Shape()
circle = Circle()
rectangle = Rectangle()

shape.area()

print("Circle Area:", circle.area(5))
print("Rectangle Area:", rectangle.area(4, 6))

# 2. Demonstrate method overloading using default arguments.

class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()

print("Add 1 number:", calc.add(5))
print("Add 2 numbers:", calc.add(5, 10))
print("Add 3 numbers:", calc.add(5, 10, 15))


# 3. Demonstrate operator overloading (__add__).

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

n1 = Number(10)
n2 = Number(20)

print("Addition:", n1 + n2)


# 4. Create Engine class and use it inside Car class.

class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        print("Car starting...")
        self.engine.start()

car = Car()
car.start_car()


# 5. Create Team class that contains multiple Player objects.

# Player Class

class Player:
    def __init__(self, name):
        self.name = name

# Team Class (Contains Multiple Players)

class Team:
    def __init__(self):
        self.players = []   # list to store Player objects

    def add_player(self, player):
        self.players.append(player)

    def show_players(self):
        print("Team Players:")
        for player in self.players:
            print(player.name)

# Object Creation & Method Calls

team = Team()

p1 = Player("Dhoni")
p2 = Player("Virat")
p3 = Player("Rohit")

team.add_player(p1)
team.add_player(p2)
team.add_player(p3)

team.show_players()

