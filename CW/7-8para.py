class Character:
    def __init__(self, name):
        self.name = name
    def Introduce(self):
        print(f"Character's name is {self.name}")
class Player(Character):
    def Introduce(self):
        print(f"Player name is {self.name}")
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory
class Inventory:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        print(f"added {item} to inventory")
inventory = Inventory()
my_player = Player("John", inventory)
my_player.Introduce()
my_player.inventory.add_item("wood")

try:
    a = 10
    b = 2
    print(a / b)
except ZeroDivisionError:
    print("error")


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate(self):
        if self.length or self.width <= 0:
            print("Error")
        result = self.length * self.width
        return result
rectangle= Rectangle( 10, 0)
print(rectangle.calculate())
rectangle= Rectangle( 10, 2)
print(rectangle.calculate())


class StringIterator:
    def __init__(self, strings):
        self.strings = strings
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.strings):
            raise StopIteration
        string = self.strings[self.index]
        self.index += 1
        return string
string_iter = StringIterator(["apple", "banana", "potato"])
for string in string_iter:
    print(string)


class Generate:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def generate(self):
        count = self.start
        while count <= self.end:
            yield count
            count += 1
my_generate = Generate(1, 6)
for i in my_generate.generate():
    print(i)