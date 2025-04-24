class Ellipse:
	def __init__(self, *args):
		if len(args) == 4:
			self.x1 = args[0]
			self.y1 = args[1]
			self.x2 = args[2]
			self.y2 = args[3]
		else:
			pass

	def __bool__(self):
		return hasattr(self, "x1")

	def get_coords(self):
		if len(self.__dict__) == 0:
			raise AttributeError('нет координат для извлечения')
		else:
			return self.x1, self.y1, self.x2, self.y2



lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 2, 3, 4), Ellipse(5, 6, 7, 8)]
for i in lst_geom:
	if bool(i):
		i.get_coords()
