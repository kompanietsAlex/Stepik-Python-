class Dimensions:
	def __init__(self, a, b, c):
		if not all([type(i) in (int, float) and i > 0 for i in (a, b, c)]):
			raise ValueError("габаритные размеры должны быть положительными числами")
		else:
			self.a = a
			self.b = b
			self.c = c

	def __hash__(self):
		return hash((self.a, self.b, self.c))

s_inp = input()
lst_dims = [Dimensions(*map(float, nums.split())) for nums in s_inp.split('; ')]
lst_dims.sort(key=hash)