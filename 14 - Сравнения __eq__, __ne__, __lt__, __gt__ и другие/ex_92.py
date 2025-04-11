class CentralBank:
	rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

	def __new__(cls, *args, **kwargs):
		return

	@classmethod
	def register(cls, money):
		money.cb = cls

class Money:
	EPS = 0.1
	type_money = None

	def __init__(self, volume=0):
		self.__volume = volume
		self.__cb = None

	@property
	def cb(self):
		return self.__cb

	@cb.setter
	def cb(self, obj):
		self.__cb = obj

	@property
	def volume(self):
		return self.__volume

	@volume.setter
	def volume(self, value):
		self.__volume = value

	def get_volume(self, other):
		if self.__cb is None:
			raise ValueError("Неизвестен курс валют.")

		if self.type_money is None:
			raise ValueError("Неизвестный тип кошелька.")

		v1 = self.volume / self.cb.rates[self.type_money]
		v2 = other.volume / other.cb.rates[other.type_money]
		return v1, v2

	def __eq__(self, other):
		v1, v2 = self.get_volume(other)
		return abs(v1 - v2) < self.EPS

	def __lt__(self, other):
		v1, v2 = self.get_volume(other)
		return v1 < v2

	def __le__(self, other):
		v1, v2 = self.get_volume(other)
		return v1 <= v2

class MoneyR(Money):
	"""для рублевых кошельков"""
	type_money = "rub"

class MoneyD(Money):
	"""для долларовых кошельков"""
	type_money = "dollar"

class MoneyE(Money):
	"""для евро-кошельков"""
	type_money = "euro"

CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

r = MoneyR(45000)
d = MoneyD(500)

CentralBank.register(r)
CentralBank.register(d)

if r > d:
	print("неплохо")
else:
	print("нужно поднажать")