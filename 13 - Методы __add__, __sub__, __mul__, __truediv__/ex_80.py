class NewList:
	def __init__(self, value=None):
		self.value = value[:] if value and type(value) == list else []

	@staticmethod
	def list_sub_list(a, b):
		b = [(x, type(x)) for x in b]
		return [x for x in a if (x, type(x)) not in b or b.remove((x, type(x)))]

	def __sub__(self, other):
		slf_val = self.copy() if isinstance(self, list) else self.value.copy()
		oth_val = other.copy() if isinstance(other, list) else other.value.copy()
		res = [[slf, type(slf)] for slf in slf_val]
		for slf in slf_val:
			for oth in oth_val:
				if (oth, type(oth)) == (slf, type(slf)):
					res.remove([slf, type(slf)])
					oth_val.remove(oth)
		return NewList([r[0] for r in res])

	def __rsub__(self, other):
		slf_val = self if isinstance(self, list) else self.value
		oth_val = other if isinstance(other, list) else other.value
		return NewList(self.list_sub_list(oth_val, slf_val))

	def get_list(self):
		return self.value

lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]