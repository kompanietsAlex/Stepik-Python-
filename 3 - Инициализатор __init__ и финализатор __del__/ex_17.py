class TriangleChecker:
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c

	def is_triangle(self):
		lst = [self.a, self.b, self.c]
		if not all(map(lambda x: type(x) in (int, float) and x >= 0, lst)):
			return 1
		elif lst[0] ** 2 + lst[1] ** 2 <= lst[2] ** 2:
			return 3
		else:
			return 2


a, b, c = map(int, input().split())
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
