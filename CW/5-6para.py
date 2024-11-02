"""Создайте класс Bicycle с атрибутами brand (бренд велосипеда), model (модель) и year (год выпуска).
Добавьте метод get_age,
который вычисляет возраст велосипеда как разницу между текущим годом и годом выпуска.
class Bicycle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


    def get_age(self):
        return 2024 - self.year

bicycle = Bicycle("TREK", "Speed bike", 2020)

print(f"Разница между текущим годом и годом выпуска {bicycle.get_age()} года")



# Создайте классы Doctor и Patient. Класс Doctor должен иметь атрибут `name`, а класс Patient — метод
# `introduce_doctor`, который будет выводить имя врача, переданного в качестве аргумента.
class Doctor:
    def __init__(self, name):
        self.name = name

class Patient:
    def __init__(self, name):
        self.name = name
    def introduce_doctor(self, doctor):
        print(f"My doctor is {doctor.name}")

doctor = Doctor("Ben")
patient = Patient("Emma")
patient.introduce_doctor(doctor)

#Создайте классы Vehicle и Car. Vehicle должен иметь метод `move`, выводящий на экран
#"Vehicle moves". Car должен наследовать Vehicle и переопределять метод `move`, выводя "Car drives". Создайте объект Car и вызовите метод `move`.
class Vehicle:
    def move(self):
        print("Vehicle moves")

class Car(Vehicle):
    def move(self):
        print("Car drives")
my_car = Car()
my_car.move()
"""
class Pen:
  def write(self):
    print("Writing")

class Highlighter:
  def highlight(self):
    print("Highlighting")

class Marker(Pen, Highlighter):
  pass

my_marker = Marker()
my_marker.write()
my_marker.highlight()