class SmartPhone:
	def __init__(self, model):
		self.model = model # марка смартфона
		self.apps = [] # список из установленных приложений

	def add_app(self, app):
		"""добавление нового приложения на смартфон"""
		if len(tuple(filter(lambda x: type(x) == type(app), self.apps))) == 0:
			self.apps.append(app)

	def remove_app(self, app):
		"""удаление приложения по ссылке на объект app"""
		if app in self.apps:
			self.apps.remove(app)


class AppVK:
	"""класс приложения ВКонтакте"""
	def __init__(self):
		self.name = "ВКонтакте"


class AppYouTube:
	"""класс приложения YouTube"""
	def __init__(self, memory_max):
		self.name = "YouTube"
		if type(memory_max) in (int, float):
			self.memory_max = memory_max  # максимальное объем памяти приложения в Мб


class AppPhone:
	"""класс приложения телефона"""
	def __init__(self, phone_list):
		self.name = "Phone"
		self.phone_list = phone_list # список контактов в виде словаря с именами и номерами телефонов


app_1 = AppVK() # name = "ВКонтакте"
app_2 = AppYouTube(1024) # name = "YouTube", memory_max = 1024
app_3 = AppPhone({"Балакирев": 1234567890, "Сергей": 98450647365, "Работа": 112}) # name = "Phone", phone_list = словарь с контактами
sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())  # второй раз добавляться не должно
sm.add_app(AppYouTube(2048))
for a in sm.apps:
	print(a.name)