class AppStore:
	def __init__(self):
		self.market = []

	def add_application(self, app):
		"""добавление нового приложения app в магазин;="""
		self.market.append(app)

	def remove_application(self, app):
		"""удаление приложения app из магазина"""
		self.market.remove(app)

	def block_application(self, app):
		"""блокировка приложения app"""
		self.market[self.market.index(app)].blocked = True

	def total_apps(self):
		"""возвращает общее число приложений в магазине"""
		return len(self.market)


class Application:
	def __init__(self, name):
		self.name = name
		self.blocked = False


store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
print(store.market[0].__dict__["blocked"])
store.block_application(app_youtube)
print(store.market[0].__dict__["blocked"])
store.remove_application(app_youtube)