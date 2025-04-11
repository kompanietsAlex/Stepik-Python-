class Budget:
	"""для управления семейным бюджетом"""
	def __init__(self):
		self.items = [] # список пунктов расходов

	def add_item(self, it):
		"""добавляет новый пункт расхода в список"""
		self.items.append(it.money)

	def remove_item(self, indx):
		"""удаляет пункт расхода из списка по индексу"""
		del self.items[indx]

	def get_items(self):
		"""возвращает список всех пунктов расходов"""
		return self.items

class Item:
	"""пункт расходов бюджета"""
	def __init__(self, name, money):
		self.name = name # название	статьи расхода
		self.money = money # сумма расходов

	def __add__(self, other):
		self.money += other.money
		return self.money

	def __radd__(self, other):
		return other + self.money

my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))

# вычисление общих расходов
s = 0
for x in my_budget.get_items():
	s = s + x
print(f"Общие расходы: {s}")
