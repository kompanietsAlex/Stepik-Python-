class Vector:
	def __init__(self, *args):
		self.coords = list(args)

	def __checker(self, v1, v2):
		if len(v1) != len(v2):
			raise ArithmeticError('размерности векторов не совпадают')

	def __add__(self, other):
		self.__checker(self.coords, other.coords)
		return Vector(*(a + b for a, b in zip(self.coords, other.coords)))

	def __sub__(self, other):
		self.__checker(self.coords, other.coords)
		return Vector(*(a - b for a, b in zip(self.coords, other.coords)))

	def __mul__(self, other):
		self.__checker(self.coords, other.coords)
		return Vector(*(a * b for a, b in zip(self.coords, other.coords)))

	def __iadd__(self, other):
		if isinstance(other, Vector):
			self.coords = [a + b for a, b in zip(self.coords, other.coords)]
			return self
		self.coords = list(a + other for a in self.coords)
		return self

	def __isub__(self, other):
		if isinstance(other, Vector):
			self.coords = [a - b for a, b in zip(self.coords, other.coords)]
			return self
		self.coords = list(a - other for a in self.coords)
		return self

	def __eq__(self, other):
		# сравнение векторов
		return self.coords == other.coords

	def __ne__(self, other):
		# сравнение векторов
		return self.coords != other.coords


v1 = Vector(1, 2)
v2 = Vector(3, 4)

print((v1 + v2).__dict__) # суммирование соответствующих координат векторов
print((v1 - v2).__dict__) # вычитание соответствующих координат векторов
print((v1 * v2).__dict__) # умножение соответствующих координат векторов

v1 += 10 # прибавление ко всем координатам вектора числа 10
print(v1.__dict__)
v1 -= 10 # вычитание из всех координат вектора числа 10
print(v1.__dict__)
v1 += v2 # прибавление к вектору другого вектора
print(v1.__dict__) # суммирование соответствующих координат векторов
v2 -= v1
print(v2.__dict__) # вычитание из вектора другого вектора

print(v1 == v2) # True, если соответствующие координаты векторов равны
print(v1 != v2) # True, если хотя бы одна пара координат векторов не совпадает