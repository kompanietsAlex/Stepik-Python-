class Box:
	def __init__(self):
		self.things = [] # список предметов в коробке

	def add_thing(self, obj): # добавление предмета obj (объект другого класса Thing) в ящик;
		self.things.append(obj)

	def get_things(self): # получение списка объектов ящика.
		return sorted(self.things)

	def __eq__(self, other): # сравнение двух ящиков;
		return sorted(self.things) == sorted(other.things)

class Thing:
	def __init__(self, name, weight):
		self.name = name # название предмета
		self.weight = weight # вес предмета

	def __eq__(self, other):
		return str.lower(self.name) == str.lower(other.name) and self.weight == other.weight

	def __ge__(self, other):
		return self.weight >= other.weight

	def __gt__(self, other):
		return self.weight > other.weight

b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

res = b1 == b2 # True