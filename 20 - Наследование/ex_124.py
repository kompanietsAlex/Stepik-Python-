class Animal:
	def __init__(self, name, old):
		"""Конструктор класса Animal"""
		self.name = name # название животного(строка);
		self.old = old # возраст животного(целое число).

class Cat(Animal):
	def __init__(self, name, old, color, weight):
		"""Конструктор класса Cat"""
		super().__init__(name, old) # вызов конструктора родительского класса Animal
		self.color = color # цвет кота(строка).
		self.weight = weight # вес кошки

	def get_info(self):
		"""Метод получения информации о коте"""
		return f"{self.name}: {self.old}, {self.color}, {self.weight}"

class Dog(Animal):
	def __init__(self, name, old, breed, size):
		"""Конструктор класса Dog"""
		super().__init__(name, old) # вызов конструктора родительского класса Animal
		self.breed = breed # порода собаки(строка).
		self.size = size # размер собаки(кортеж из двух чисел).

	def get_info(self):
		"""Метод получения информации о собаке"""
		return f"{self.name}: {self.old}, {self.breed}, {self.size}"

cat = Cat('кот', 4, 'black', 2.25)
dog = Dog('пёс', 5, 'доберман', (1.2, 0.7))
print(cat.get_info())
print(dog.get_info())