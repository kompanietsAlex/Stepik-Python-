class VerifySize:
	def __set_name__(self, owner, name):
		self.name = "__" + name

	def __get__(self, instance, owner):
		return property() if instance is None else getattr(instance, self.name)

	def __set__(self, instance, value):
		if type(value) in (int, float) and instance.MIN_DIMENSION <= value <= instance.MAX_DIMENSION:
			setattr(instance, self.name, value)

class Dimensions:
	MIN_DIMENSION = 10
	MAX_DIMENSION = 1000

	a = VerifySize()
	b = VerifySize()
	c = VerifySize()

	def __init__(self, a, b, c):
		self.__a = self.__b = self.__c = None # габаритные размеры(целые или вещественные числа).
		self.a, self.b, self.c = a, b, c

	def __setattr__(self, key, value):
		if key in ['MIN_DIMENSION', 'MAX_DIMENSION']:
			raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
		else:
			super().__setattr__(key, value)


d = Dimensions(10.5, 20.1, 30)
d.a = 8
d.b = 15
a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
d.MAX_DIMENSION = 10  # исключение AttributeError