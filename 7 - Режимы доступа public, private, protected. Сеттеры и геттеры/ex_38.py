class Line:
	def __init__(self, x1=0, y1=0, x2=0, y2=0):
		self.set_coords(x1, y1, x2, y2)

	def set_coords(self, x1, y1, x2, y2): # для изменения координат линии;
		self.__x1, self.__y1 = x1, y1  # начальная координата
		self.__x2, self.__y2 = x2, y2  # конечная координата

	def get_coords(self): # для получения кортежа из текущих координат линии
		return self.__x1, self.__y1, self.__x2, self.__y2

	def draw(self): # для отображения в консоли списка текущих координат линии
		print(*self.get_coords())


l1 = Line(1, 2, 3, 4)
l1.draw()