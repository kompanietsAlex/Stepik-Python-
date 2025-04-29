class Integer:
	def __init__(self, start_value=0):
		self.__value = start_value

	@property
	def value(self):
		return self.__value

	@value.setter
	def value(self, new_value):
		if type(new_value) != int:
			raise ValueError('должно быть целое число')
		self.__value = new_value

	def __repr__(self):
		#__str__ возвращает строковое представление объекта
		return str(self.__value)

class Array:
	def __init__(self, max_length, cell):
		self.__max_length = max_length
		self.__cell = cell
		self.__array = [self.__cell() for _ in range(max_length)]

	def __check8(self, ind):
		# проверка на корректность индекса
		if type(ind) != int or not (-self.__max_length <= ind < self.__max_length):
			raise IndexError('неверный индекс для доступа к элементам массива')

	def __getitem__(self, index):
		self.__check8(index)
		return self.__array[index].value

	def __setitem__(self, index, value):
		self.__check8(index)
		self.__array[index].value = value

	def __repr__(self):
		return ' '.join(map(str, self.__array))

ar_int = Array(10, cell=Integer)
print(ar_int[3])
print(ar_int) # должны отображаться все значения массива в одну строчку через пробел
ar_int[1] = 10
ar_int[1] = 10.5 # должно генерироваться исключение ValueError
ar_int[10] = 1 # должно генерироваться исключение IndexError