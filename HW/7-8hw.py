class InvalidAgeError(Exception):
    def __init__(self, message):
        self.message = message
class Person:
    def __init__(self, name):
        self.name = name
        self.age = age
    def set_age(self, age):
        if age < 0 or age > 120:
            raise InvalidAgeError("Возраст отрицательный или превышает 120 лет.")
        self.age = age

try:
    age = 14
    person = Person("Heorhii")
    person.set_age(age)
    print(f"Ваш возраст: {person.age}")
except InvalidAgeError as error:
    print(f"Ошибка: {error}")
try:
    age = 150
    person = Person("Heorhii")
    person.set_age(age)
    print(f"Ваш возраст: {person.age}")
except InvalidAgeError as error:
    print(f"Ошибка: {error}")
try:
    age = -8
    person = Person("Heorhii")
    person.set_age(age)
    print(f"Ваш возраст: {person.age}")
except InvalidAgeError as error:
    print(f"Ошибка: {error}")





class MyIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= self.n:
            self.current += 1
            return self.current - 1
        raise StopIteration
    def count_down(self):
        for i in range(self.n, -1, -1):
            yield i
    def multiplier(self, m):
        def multiply_by_m(x):
            return x * m * self.n
        return multiply_by_m
def print_result(func):
    def decorated_function(arg):
        result = func(arg)
        print(f"Результат: {result}")
        return result
    return decorated_function
@print_result
def test_iterator(n):
    iterator = MyIterator(n)
    return list(iterator)
@print_result
def test_count_down(n):
    iterator = MyIterator(n)
    return list(iterator.count_down())
@print_result
def test_multiplier(args):
    value, m = args
    iterator = MyIterator(1)
    multiply = iterator.multiplier(m)
    return multiply(value)
test_iterator(5)
test_count_down(10)
test_multiplier((6, 3))