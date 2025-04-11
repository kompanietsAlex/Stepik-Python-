class Thing:
	"""Описание предмета, с указанием веса."""
	def __init__(self, name, weight):
		self.name = name # имя предмета
		self.weight = weight # вес предмета

class Bag:
	"""Класс для создания рюкзака."""
	def __init__(self, max_weight=0):
		self.max_weight = max_weight # максимальный вес рюкзака
		self.__things = []

	@property
	def things(self):
		return self.__things

	def add_thing(self, thing):# добавление	нового предмета в рюкзак
		if self.get_total_weight() + thing.weight < self.max_weight:
			self.__things.append(thing)

	def	remove_thing(self, indx): # удаление предмета по индексу списка
		self.__things.pop(indx)

	def get_total_weight(self): # возвращает суммарный вес предметов в рюкзаке
		return sum(thing.weight for thing in self.__things)


bag = Bag(1000)
bag.add_thing(Thing("Книга по Python", 100))
bag.add_thing(Thing("Котелок", 500))
bag.add_thing(Thing("Спички", 20))
bag.add_thing(Thing("Бумага", 100))
w = bag.get_total_weight()
print(f"Общий вес предметов в рюкзаке: {w}")
for t in bag.things:
	print(f"{t.name}: {t.weight}")