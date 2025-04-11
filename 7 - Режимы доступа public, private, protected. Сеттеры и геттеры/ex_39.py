class Point:
	def __init__(self, x, y):
		self.__x, self.__y = x, y # координаты точки на плоскости.

	def get_coords(self): # возвращение координат __x, __y
		return self.__x, self.__y


class Rectangle:
	def __init__(self, a, b, c=None, d=None):
		self.__sp, self.__ep = None, None # начальная и конечная точки прямоугольника.

		if isinstance(a, Point) and isinstance(b, Point): # проверка, являются ли координаты точками
			self.__sp, self.__ep = a, b
		elif all(map(lambda x: type(x) in (int, float), [a, b, c, d])): # проверка, являются ли координаты числами
			self.__sp = Point(a, b)
			self.__ep = Point(c, d)

	def set_coords(self, sp, ep): # установка координат прямоугольника
		self.__sp = sp
		self.__ep = ep

	def get_coords(self): # возвращение координат начальной и конечной точек прямоугольника
		return self.__sp, self.__ep

	def draw(self): # отображение сообщения:
		print(f"Прямоугольник с координатами: {self.__sp.get_coords()} {self.__ep.get_coords()}")


rect = Rectangle(0, 0,20, 34)
rect.draw()