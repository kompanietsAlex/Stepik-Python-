class Complex:
	def __init__(self, real, img):
		self.__real = self.__img = 0
		self.real = real
		self.img = img

	@property
	def real(self):
		return self.__real

	@real.setter
	def real(self, value):
		if type(value) not in (int, float):
			raise ValueError("Неверный тип данных.")
		self.__real = value

	@property
	def img(self):
		return self.__img

	@img.setter
	def img(self, value):
		if type(value) not in (int, float):
			raise ValueError("Неверный тип данных.")
		self.__img = value

	def __abs__(self):
		return (self.__real ** 2 + self.__img ** 2) ** 0.5


cmp = Complex(real= 7, img= 8)
cmp.real, cmp.img = 3, 4
c_abs = abs(cmp)