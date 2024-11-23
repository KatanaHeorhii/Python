class Character:
  def __init__(self, name):
    self.__health = 100
    self.__energy = 100
    self.__weapon = None
    self.name = name
  def attack(self):
    self.__energy -= 10
    if self.__energy < 0:
      print("Недостаточно энергии чтобы атаковать")
  def take_damage(self, damage):
    self.__health -= damage
    if self.__health <= 0:
      print("Персонаж", self.name, "погибает")
  def equip_weapon(self, weapon):
    self.__weapon = weapon
  def get_status(self):
    return (f"Имя: {self.name}, Здоровье: {self.__health}, Энергия: {self.__energy}, Оружие: {self.__weapon}")

my_character = Character("Боб")
print(my_character.get_status())
my_character.equip_weapon("Лук")
print(my_character.get_status())
my_character.attack()
print(my_character.get_status())
my_character.take_damage(50)
print(my_character.get_status())
my_character.attack()
print(my_character.get_status())
my_character.take_damage(50)
print(my_character.get_status())

my_character = Character("Том")
print(my_character.get_status())
my_character.equip_weapon("Посох")
print(my_character.get_status())
my_character.attack()
print(my_character.get_status())
my_character.attack()
print(my_character.get_status())
my_character.take_damage(5)
print(my_character.get_status())
my_character.attack()
print(my_character.get_status())
my_character.take_damage(5)
print(my_character.get_status())
my_character.attack()
print(my_character.get_status())
my_character.take_damage(5)
print(my_character.get_status())
my_character.attack()
print(my_character.get_status())
my_character.take_damage(5)
print(my_character.get_status())
my_character.attack()
print(my_character.get_status())
my_character.take_damage(5)
print(my_character.get_status())
my_character.attack()
print(my_character.get_status())
my_character.take_damage(5)
print(my_character.get_status())
my_character.attack()
print(my_character.get_status())
my_character.take_damage(5)
print(my_character.get_status())
my_character.attack()
print(my_character.get_status())
my_character.take_damage(5)
print(my_character.get_status())
my_character.attack()
print(my_character.get_status())
my_character.take_damage(5)
print(my_character.get_status())
my_character.attack()
print(my_character.get_status())
my_character.take_damage(5)
print(my_character.get_status())