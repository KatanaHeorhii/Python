
class Student:
    print("Hi")

    def __init__(self):
        self.height = 160
        print("I am alive!")

first_student = Student()

class Student:
    def __init__(self, height=160):
        self.height = height


nick = Student()
kate = Student(height=170)
print(nick.height)
print(kate.height)



class Student:
    def __init__(self):
        self.height = 170

    def printer(self):
        print(self.height)


student1 = Student()
student1.printer()


class Machine:

    def __init__(self, kolesa, karkas):
        self.kolesa = kolesa
        self.karkas = karkas

    def printer(self):
        print(f"В машині {self.kolesa} колес, каркас {self.karkas}")

marka = Machine(4, "BMW" )
marka.printer()