class Vector:
	_allowed_types = (int, float)

	def __init__(self, *args):
		if not all(isinstance(i, self._allowed_types) for i in args):
			raise ValueError("неправильный тип координат")
		self._coords = args

	def get_coords(self):
		return self._coords

	def check_type(self, other):
		if not isinstance(other, Vector):
			raise ValueError("неправильный тип")
		if len(self._coords) != len(other._coords):
			raise ValueError("размерности векторов не совпадают")

	def make_vector(self, coords):
		try:
			return self.__class__(*coords)
		except ValueError:
			return Vector(*coords)

	def __add__(self, other):
		self.check_type(other)
		coords = (a + b for a, b in zip(self._coords, other._coords))
		return self.make_vector(coords)

	def __sub__(self, other):
		self.check_type(other)
		coords = (a - b for a, b in zip(self._coords, other._coords))
		return self.make_vector(coords)

class VectorInt(Vector):
	_allowed_types = (int, )




v1 = VectorInt(1, 2, 3, 4)
v2 = VectorInt(4, 2, 3, 4)
v3 = Vector(1.0, 2, 3, 4)

v = v1+v2
print(type(v))