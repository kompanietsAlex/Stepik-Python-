from string import digits
class InputValues:
	def __init__(self, render):     # render - ссылка на функцию или объект для преобразования
		self.render = render

	def __call__(self, func, *args, **kwargs):     # func - ссылка на декорируемую функцию
		def wrapper(*args, **kwargs):
			return list(map(self.render, func(*args, **kwargs).split()))
		return wrapper


class RenderDigit:
	def __call__(self, string, *args, **kwargs):
		return int(string) if all(map(lambda x: x in digits, string)) else None



render = RenderDigit()
input_dg = InputValues(render)(input)
res = input_dg()
print(res)