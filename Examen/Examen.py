import requests
from bs4 import BeautifulSoup
#Класс для управления списком сайтов
class SiteManager:
    def __init__(self):
        self.sites = []
    def add_site(self, url):
        if url not in self.sites:
            self.sites.append(url)
            print("Сайт добавлен.")
        else:
            print("Сайт уже в списке.")
    def sites_list(self):
        return self.sites
#Класс для парсинга и поиска по страницам
class SiteParser:
    def __init__(self, sites):
        self.sites = sites
    def search(self, query):
        results = {}
        for site in self.sites:
            try:
                response = requests.get(site)
                response.raise_for_status()
                soup = BeautifulSoup(response.text, 'html.parser')
                text = soup.get_text().lower()
                count = text.count(query.lower())
                if count > 0:
                    results[site] = count
            except Exception as e:
                print(f"Не удалось совершить поиск по сайту {site}: {e}")
        return results
#Класс для взаимодействия с пользователем
class UserInterface:
    def __init__(self, site_manager, parser):
        self.site_manager = site_manager
        self.parser = parser
    def show_menu(self):
        while True:
            print("Меню:")
            print("1. Добавить сайт")
            print("2. Показать сайты")
            print("3. Искать на сайтах")
            print("4. Выход")
            choice = input("Ваш выбор: ").strip()
            if choice == "1":
                url = input("Введите URL сайта: ").strip()
                self.site_manager.add_site(url)
            elif choice == "2":
                sites = self.site_manager.sites_list()
                if sites:
                    print("Сайты в списке:")
                    for site in sites:
                        print(f"| {site}")
                else:
                    print("Список с сайтами пуст.")
            elif choice == "3":
                request = input("Ваш запрос для поиска: ").strip()
                sites = self.site_manager.sites_list()
                if sites:
                    results = self.parser.search(request)
                    if results:
                        print("Результаты поиска:")
                        for site, count in results.items():
                            print(f"{site} | {count} совпадений")
                    else:
                        print("Совпадений не найдено.")
                else:
                    print("Список сайтов пуст. Чтобы искать, добавьте сайты.")
            elif choice == "4":
                print("Выход.")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")
#Основной класс программы
class SearchApp:
    def __init__(self):
        self.site_manager = SiteManager()
        self.parser = SiteParser(self.site_manager.sites_list())
    def run(self):
        my_interface = UserInterface(self.site_manager, self.parser)
        my_interface.show_menu()
#Запуск программы
start = SearchApp()
start.run()