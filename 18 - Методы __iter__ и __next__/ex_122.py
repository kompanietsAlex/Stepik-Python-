class Matrix:
	def __init__(self, rows_or_lst, cols=0, fill_value=0):
		if type(rows_or_lst) == list:
			self._rows = len(rows_or_lst)
			self._cols = len(rows_or_lst[0])
			if not all(len(r) == self._cols for r in rows_or_lst) or \
				not all(self.__is_disit(x) for row in rows_or_lst for x in row):
				raise TypeError('список должен быть прямоугольным, состоящим из чисел')
			self._lst = rows_or_lst
		else:
			if type(rows_or_lst) != int or type(cols) != int or type(fill_value) not in (int, float):
				raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
			self._rows = rows_or_lst
			self._cols = cols
			self._lst = [[fill_value for _ in range(cols)] for _ in range(rows_or_lst)]

	@staticmethod
	def __is_disit(x):
		return type(x) in (int, float)

	def __check_index(self, index):
		r, c = index
		if not (0 <= r < self._rows) or not (0 <= c < self._cols):
			raise IndexError('недопустимые значения индексов')

	def __getitem__(self, item):
		self.__check_index(item)
		r, c = item
		return self._lst[r][c]

	def __setitem__(self, key, value):
		self.__check_index(key)
		if not self.__is_disit(value):
			raise TypeError('значения матрицы должны быть числами')
		r, c = key
		self._lst[r][c] = value

	def __check_dimensions(self, m):
		rows, cols = m._rows, m._cols
		if self._rows != rows or self._cols != cols:
			raise ValueError('операции возможны только с матрицами равных размеров')

	def __add__(self, other):
		if type(other) == type(self):
			self.__check_dimensions(other)
			return Matrix([[self[i, j] + other[i, j] for j in range(self._cols)] for i in range(self._rows)])
		else:
			self.__is_disit(other)
			return Matrix([[self[i, j] + other for j in range(self._cols)] for i in range(self._rows)])

	def __sub__(self, other):
		if type(other) == type(self):
			self.__check_dimensions(other)
			return Matrix([[self[i, j] - other[i, j] for j in range(self._cols)] for i in range(self._rows)])
		else:
			self.__is_disit(other)
			return Matrix([[self[i, j] - other for j in range(self._cols)] for i in range(self._rows)])

mt = Matrix([[1, 2], [3, 4]])
res = mt[0, 0] # 1
print(res)
res2 = mt[0, 1] # 2
print(res2)
res3 = mt[1, 0] # 3
print(res3)
res4 = mt[1, 1] # 4
print(res4)