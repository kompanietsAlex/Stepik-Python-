class Shop: # класс для управления магазином
	def __init__(self, name):
		self.name = name # название магазина
		self.goods = [] # список товаров в магазине

	def add_product(self, product):
		"""добавление товара в магазин"""
		self.goods.append(product)

	def remove_product(self, product):
		"""удаление товара product из магазина"""
		if product in self.goods:
			self.goods.remove(product)


class Product: # класс для представления отдельного товара
	_id = 1 # статический идентификатор для создания уникальных идентификаторов товаров
	attrs = {"name": (str, ), "price": (int, float), "weight": (int, float)} # допустимые атрибуты товара
	def __init__(self, name, weight, price):

		self.id = Product._id # идентификатор товара
		Product._id += 1 # увеличение статического идентификатора на 1

		self.name = name # название товара
		self.price = price # цена товара
		self.weight = weight # вес товара

	def __setattr__(self, key, value):
		if key in self.attrs and type(value) in self.attrs[key]:
			if (key == "price" or key == "weight") and value <= 0:
				raise TypeError("Неверный тип присваиваемых данных.")
		elif key in self.attrs:
			raise TypeError("Неверный тип присваиваемых данных.")

		object.__setattr__(self, key, value)

	def __delattr__(self, item):
		if item == "id":
			raise AttributeError("Атрибут id удалять запрещено.")
		object.__delattr__(self, item)

shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
	print(f"{p.name}, {p.weight}, {p.price}")