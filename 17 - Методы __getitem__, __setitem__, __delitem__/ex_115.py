class Thing:
	def __init__(self, name, weight):
		self.name = name if isinstance(name, str) else str(name)
		self.weight = weight if isinstance(weight, int) and weight > 0 else 0

class Bag:
	def __init__(self, max_weight):
		self.max_weight = max_weight
		self.things = []

	def __check_index(self, indx):
		if not type(indx) == int or indx < 0 or indx >= len(self.things):
			raise IndexError('неверный индекс')

	def add_thing(self, thing):
		if self.get_total_weight() + thing.weight > self.max_weight:
			raise ValueError('превышен суммарный вес предметов')
		self.things.append(thing)

	def get_total_weight(self):
		return sum(thing.weight for thing in self.things)

	def __getitem__(self, index):
		self.__check_index(index)
		return self.things[index]

	def __setitem__(self, index, value):
		self.__check_index(index)
		if self.things[index].weight + value.weight > self.max_weight:
			raise ValueError('превышен суммарный вес предметов')
		self.things[index] = value

	def __delitem__(self, index):
		self.__check_index(index)
		del self.things[index]


b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

b[0] = Thing('рубашка', 500)

b[0] = Thing('рубашка', 800)
