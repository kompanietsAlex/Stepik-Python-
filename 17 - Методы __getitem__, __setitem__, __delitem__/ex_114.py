class Bag:
	def __init__(self, max_weight):
		self.max_weight = max_weight
		self.__things = []
		self.__weight = 0

	def add_thing(self, thing):


class Thing:
	def __init__(self, name, weight):
		self.name = name if type(name) == str else None
		self.weight = weight if type(weight) in (int, float) else None

bag = Bag(1000)
bag.add_thing(Thing('книга', 100))
bag.add_thing(Thing('носки', 200))
bag.add_thing(Thing('рубашка', 500))
bag.add_thing(Thing('ножницы', 300)) # генерируется исключение ValueError
print(bag[2].name) # рубашка
bag[1] = Thing('платок', 100)
print(bag[1].name) # платок
del bag[0]
print(bag[0].name) # платок
t = bag[4] # генерируется исключение IndexError