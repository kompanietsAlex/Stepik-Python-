class TVProgram:
	def __init__(self, name):
		self.name = name # переменная для хранения информации о телепередаче
		self.items = [] # список телепередач

	def add_telecast(self, tl): # добавление телепередачи в	список
		self.items.append(tl)

	def remove_telecast(self, indx): # удаление	телепередачи по	ее порядковому номеру __id
		ttv = tuple(filter(lambda x: x.uid == indx, self.items))
		for i in ttv:
			self.items.remove(i)

class Telecast:
	def __init__(self, id, name, duration):
		self.__id = id # переменная для хранения уникального идентификатора телепередачи
		self.__name = name # переменная для хранения названия телепередачи
		self.__duration = duration # переменная для хранения продолжительности телепередачи

	@property # получение уникального идентификатора телепередачи
	def uid(self):
		return (self.__id)

	@uid.setter # установка уникального идентификатора телепередачи
	def uid(self, value):
		self.__id = value

	@property # получение названия телепередачи
	def name(self):
		return self.__name

	@name.setter # установка названия телепередачи
	def name(self, value):
		self.__name = value

	@property # получение продолжительности телепередачи
	def duration(self):
		return self.__duration

	@duration.setter # установка продолжительности телепередачи
	def duration(self, value):
		self.__duration = value


pr = TVProgram("Первый канал")
pr.add_telecast(Telecast(1, "Доброе утро", 10000))
pr.add_telecast(Telecast(2, "Новости", 2000))
pr.add_telecast(Telecast(3, "Интервью с Балакиревым", 20))
for t in pr.items:
	print(f"{t.name}: {t.duration}")