import time
class GeyserClassic:
	""" фильтр для очистки воды.В классе три слота для фильтров"""
	MAX_DATE_FILTER = 100 # максимальное время работы фильтра(любого)
	def __init__(self):
		self.filter_class = ("Mechanical", "Aragon", "Calcium")
		self.filters = {(1, self.filter_class[0]): None, (2, self.filter_class[1]): None, (3, self.filter_class[2]): None}

	def add_filter(self, slot_num, filter):
		"""добавление фильтра filter в указанный слот slot_num"""
		key = (slot_num, filter.__class__.__name__)
		if key in self.filters and not self.filters[key]:
			self.filters[key] = filter

	def remove_filter(self, slot_num):
		"""извлечение фильтра из указанного слота(slot_num: 1, 2, 3)"""
		if type(slot_num) == int and 1 <= slot_num <= 3:
			key = (slot_num, self.filter_class[slot_num - 1])
			if key in self.filters:
				self.filters[key] = None

	def get_filters(self):
		"""возвращает кортеж из набора трех	фильтров в порядке установки"""
		return tuple(self.filters.values())

	def water_on(self):
		"""включение воды возвращает True, если	вода течет"""
		end = time.time()
		for f in self.filters.values():
			if f is None:
				return False
			start = f.date
			if end - start > self.MAX_DATE_FILTER:
				return False
		return True


class Mechanical:
	"""для очистки от крупных механических частиц"""
	def __init__(self, date):
		self.date = date

	def __setattr__(self, key, value):
		if key == 'date' and key in self.__dict__:
			return
		super().__setattr__(key, value)

class Aragon:
	"""для последующей очистки воды"""
	def __init__(self, date):
		self.date = date

	def __setattr__(self, key, value):
		if key == 'date' and key in self.__dict__:
			return
		super().__setattr__(key, value)

class Calcium:
	"""для обработки воды на третьем этапе"""
	def __init__(self, date):
		self.date = date

	def __setattr__(self, key, value):
		if key == 'date' and key in self.__dict__:
			return
		super().__setattr__(key, value)

my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on() # False
my_water.add_filter(3, Calcium(time.time()))
w = my_water.water_on() # True
f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
my_water.add_filter(3, Calcium(time.time())) # повторное добавление в занятый слот невозможно
my_water.add_filter(2, Calcium(time.time())) # добавление в "чужой" слот также невозможно