# 1. Create a class Book with attributes title and author.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print("Title  :", self.title)
        print("Author :", self.author)
        print("--------------------")

# Create 3 different book objects and print all details.
# Creating 3 book objects
book1 = Book("Python Basics", "Guido van Rossum")
book2 = Book("Clean Code", "Robert C. Martin")
book3 = Book("The Alchemist", "Paulo Coelho")

# Printing book details
book1.display()
book2.display()
book3.display()


#2. Create a class Rectangle with a constructor that takes length and width and stores area and perimeter as object attributes.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = length * width
        self.perimeter = 2 * (length + width)


# Creating an object
rect = Rectangle(10, 5)

# Printing details
print("Length     :", rect.length)
print("Width      :", rect.width)
print("Area       :", rect.area)
print("Perimeter  :", rect.perimeter)
