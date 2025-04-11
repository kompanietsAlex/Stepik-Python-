class StringValue:
	def __init__(self, min_length, max_length):
		self.min_length = min_length
		self.max_length = max_length

	def __set_name__(self, owner, name):
		self.name = "_" + name

	def __get__(self, instance, owner):
		return getattr(instance, self.name)

	def __set__(self, instance, value):
		if type(value) == str and self.min_length <= len(value) <= self.max_length:
			setattr(instance, self.name, value)

class PriceValue:
	def __init__(self, max_value):
		self.max_length = max_value

	def __set_name__(self, owner, name):
		self.name = "_" + name

	def __get__(self, instance, owner):
		return getattr(instance, self.name)

	def __set__(self, instance, value):
		if type(value) in (int, float) and 0 <= value <= self.max_length:
			setattr(instance, self.name, value)

class Product:

	name = StringValue(2, 50)
	price = PriceValue(10000)

	def __init__(self, name, price):
		self.name = name
		self.price = price

class SuperShop:
	def __init__(self, name):
		self.name = name # название магазина (строка)
		self.goods = [] # список из товаров

	def add_product(self, product): # добавление товара в	магазин
		self.goods.append(product)

	def remove_product(self, product): # удаление	товара из магазина
		if product in self.goods:
			self.goods.remove(product)


shop = SuperShop("У Балакирева")
shop.add_product(Product("Курс по Python", 0))
shop.add_product(Product("Курс по Python ООП", 2000))
for p in shop.goods:
	print(f"{p.name}: {p.price}")