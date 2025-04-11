class LineTo:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class PathLines:
	def __init__(self, *args):
		self.path = [LineTo(0, 0)]
		for obj in args:
			self.path.append(obj)

	def get_path(self): # возвращает список из объектов класса LineTo
		return self.path

	def get_length(self): # возвращает суммарную длину пути
		g = ((self.path[i-1], self.path[i]) for i in range(1, len(self.path)))
		return sum(map(lambda t: ((t[0].x - t[1].x) ** 2 + (t[0].y - t[1].y) ** 2) ** 0.5, g))


	def add_line(self, obj): # добавление нового линейного объекта LineTo) в
		self.path.append(obj)

p = PathLines(LineTo(10, 20), LineTo(10, 30))
p.add_line(LineTo(20, -10))
dist = p.get_length()
print(f'Длина пути: {dist}')
