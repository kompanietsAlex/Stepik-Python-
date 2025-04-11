class PolyLine:
	def __init__(self, start_coord, *args):
		self.__coords = (start_coord,) + args

	def add_coord(self, x, y): # добавление	новой координаты
		self.__coords = tuple(self.__coords) + ((x, y),)

	def remove_coord(self, indx): # удаление координаты	по индексу
		self.__coords = list(self.__coords)
		del self.__coords[indx]

	def get_coords(self): # получение списка координат
		return list(self.__coords)

poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))
