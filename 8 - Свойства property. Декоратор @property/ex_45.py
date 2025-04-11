class RadiusVector2D:
	MIN_COORD = -100
	MAX_COORD = 1024

	def __init__(self, x, y):
		if not self.check_value(x):
			self.__x = 0
		else:
			self.__x = x
		if not self.check_value(y):
			self.__y = 0
		else:
			self.__y = y

	def check_value(cls, value):
		return type(value) in (int, float) and cls.MIN_COORD <= value <= cls.MAX_COORD

	@property
	def x(self):
		return self.__x

	@x.setter
	def x(self, value):
		if self.check_value(value):
			self.__x = value

	@property
	def y(self):
		return self.__y

	@y.setter
	def y(self, value):
		if self.check_value(value):
			self.__y = value

	@staticmethod
	def norm2(vector):
		return vector.x ** 2 + vector.y ** 2

rv2d = RadiusVector2D(-905, 2000)
print(rv2d.__dict__)