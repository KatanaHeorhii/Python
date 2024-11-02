"""class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculate_area(self):
        return self.width * self.height
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
my_rectangle = Rectangle(3, 5)
print(f"Площа прямокутника: {my_rectangle.calculate_area()}")
print(f"Периметр прямокутника: {my_rectangle.calculate_perimeter()}")
"""

class Product:
    def __init__(self, name = "Apples", price = 5, quantity = 12):
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price * self.quantity
    def display_info(self):
        print(f"Product: {self.name}, price: {self.price}, quantity: {self.quantity}")
my_product = Product()
my_product.display_info()