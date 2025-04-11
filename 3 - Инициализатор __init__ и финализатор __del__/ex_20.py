class Cart:
	def __init__(self):
		self.goods = []

	def add(self, gd):
		self.goods.append(gd)

	def remove(self, indx):
		del self.goods[indx]

	def get_list(self):
		return [f"{x.name}: {x.price}" for x in self.goods]


class Table:
	def __init__(self, name, price):
		self.name = name
		self.price = price


class TV:
	def __init__(self, name, price):
		self.name = name
		self.price = price


class Notebook:
	def __init__(self, name, price):
		self.name = name
		self.price = price


class Cup:
	def __init__(self, name, price):
		self.name = name
		self.price = price

tv = TV("sony", "1000")
table = Table("ikea", "100")
notebook = Notebook("asus", "10000")
cup = Cup("usa", "10")

cart = Cart()
cart.add(tv)
cart.add(tv)
cart.add(table)
cart.add(notebook)
cart.add(notebook)
cart.add(cup)
# два телевизора(TV),
# один стол(Table),
# два ноутбука(Notebook)
# одну кружку(Cup).