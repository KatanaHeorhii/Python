class Task:
    def __init__(self, name, description, deadline, state):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.state = state

class TaskManager:
    def __init__(self):
        self.tasks = []

    def adding(self, name, description, deadline, state):
        task = Task(name, description, deadline, state)
        self.tasks.append(task)

    def deleting(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                self.tasks.remove(task)
                break

    def mark_as_done(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.state = "Виконано"
                break

    def print_tasks(self):
        for task in self.tasks:
            print(f"Назва: {task.name}, Опис: {task.description}, Дедлайн: {task.deadline}, Стан: {task.state}")
task_manager = TaskManager()
task_manager.adding("Завдання 1", "Зв'язування класів", "2024-09-11", "Не виконано")
task_manager.adding("Завдання 2", "Винятки", "2024-17-11", "Не виконано")
task_manager.mark_as_done("Завдання 1")
task_manager.print_tasks()
task_manager.deleting("Завдання 1")
task_manager.print_tasks()



class Character:
    def __init__(self, name, health ):
                 self.name = name
                 self.health = health
    def attack(self):
        pass
class Hero(Character):
    def __init__(self, name, health, weapon):
        super().__init__(name, health)
        self.weapon = weapon
    def attack(self):
        print(f"{self.name} атакує з {self.weapon}")
class Enemy(Character):
    def __init__(self, name, health, damage):
        super().__init__(name, health)
        self.damage = damage
    def attack(self):
        print(f"{self.name} атакує з {self.damage}")
hero = Hero("Ланцелот", 30, "меч")
enemy = Enemy("Скелет", 70, "лук")
hero.attack()
enemy.attack()