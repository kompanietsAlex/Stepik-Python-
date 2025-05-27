class ListInteger(list):

	@staticmethod
	def __check_type(value):
		if type(value) != int:
			raise TypeError('можно передавать только целочисленные значения')
		return value

	def __init__(self, *args):
		super().__init__(*args)

	def __setitem__(self, index, value):
		self.__check_type(value)
		super().__setitem__(index, value)

	def append(self, value):
		self.__check_type(value)
		super().append(value)


s = ListInteger((1, 2, 3))
print(s)
s[1] = 10
s.append(11)
print(s)
s[0] = 10.5 # TypeError