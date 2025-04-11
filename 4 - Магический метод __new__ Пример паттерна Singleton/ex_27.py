class Factory:
	@staticmethod
	def build_sequence():
		lst = []
		return lst

	@staticmethod
	def build_number(a):
		float_num = float(a)
		return float_num


class Loader:
	@staticmethod
	def parse_format(string, factory):
		seq = factory.build_sequence()
		for sub in string.split(","):
			item = factory.build_number(sub)
			seq.append(item)
		return seq

ld = Loader()
res = ld.parse_format("4, 5, -6.5", Factory())
print(res)