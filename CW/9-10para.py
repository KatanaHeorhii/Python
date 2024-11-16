"""Создайте абстрактный класс GameCharacter с абстрактным методом attack
Реализуйте два дочерних класса: Warrior и Mage, которые определяют этот метод по-своему
Напишите функцию, которая вызывает метод attack для всех объектов списка персонажей
from abc import ABC, abstractmethod
class GameCharacter(ABC):
  @abstractmethod
  def attack(self):
    pass
class Warrior(GameCharacter):
    def attack(self):
      return "10 dmg"
class Mage(GameCharacter):
    def attack(self):
        return "30 dmg"

my_warrior = Warrior()
my_mage = Mage()
print(my_warrior.attack())
print(my_mage.attack())
class PlayerInventory:
  def __init__(self):
    self.__items = []

  def add_item(self, item):
    self.__items.append(item)

  def remove_item(self, item):
    if item in self.__items:
      self.__items.remove(item)

  def show_inventory(self):
    for item in self.__items:
            print(f"Inventory:{item}")
my_inventory = PlayerInventory()
my_inventory.add_item("wood")
my_inventory.add_item("potion")
my_inventory.show_inventory()
my_inventory.remove_item("wood")
my_inventory.show_inventory()



pip import BeautifulSoup, Requests
class MovieParser:
  def __init__(self, url):
    self.url = url
  def fetch_page(self):
    response = requests.get(self.url)
    if response.status.code == 200:
      return response.text
    else:
      raise Exception (f"Не удалось загрузить страницу, код ошибки: {response.status.code}")
  def parse_movies(self, html):
    soup = BeautifulSoup(html, 'html.parser')
    movie_elements = soup.find_all('p', class_ = 'long-title')
    movies = [movie.text.strip() for movie in movie_elements]
    return movies
url = "https://movies.disney.com/"
parser = MovieParser(url)
html_content = parser.fetch_page()
movies = parser.parse_movies(html_content)
print("Список мультфильмов:")
for movie in movies:
  print(movie)"""