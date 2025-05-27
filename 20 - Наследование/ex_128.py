class Validator:
	def _is_valid(self, data):
		return True

	def __call__(self, data, *args, **kwargs):
		if not self._is_valid(data):
			raise ValueError('данные не прошли валидацию')
		return data

class IntegerValidator(Validator):
	"""для проверки, что data - целое число в заданном диапазоне;"""
	def __init__(self, min_value, max_value):
		self.min_value = min_value
		self.max_value = max_value

	def _is_valid(self, data):
		if type(data) != int or data < self.min_value or data > self.max_value:
			return False
		return True

class FloatValidator(Validator):
	"""для проверки, что data - вещественное число в заданном диапазоне."""
	def __init__(self, min_value, max_value):
		self.min_value = min_value
		self.max_value = max_value

	def _is_valid(self, data):
		if type(data) != float or data < self.min_value or data > self.max_value:
			return False
		return True


v = Validator()
print(v(10))  # 10
integer_validator = IntegerValidator(-10, 10)
float_validator = FloatValidator(-1, 1)
res1 = integer_validator(10)  # исключение не генерируется (проверка проходит)
print(res1)  # 10
res2 = float_validator(10)  # исключение ValueError
print(res2)  # 0.1
