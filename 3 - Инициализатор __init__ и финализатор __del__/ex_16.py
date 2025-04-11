from random import choice, randint
class Line:
	def __init__(self, a=None, b=None, c=None, d=None):
		self.sp = (a, b)
		self.ep = (c, d)

class Rect:
	def __init__(self, a=None, b=None, c=None, d=None):
		self.sp = (a, b)
		self.ep = (c, d)

class Ellipse:
	def __init__(self, a=None, b=None, c=None, d=None):
		self.sp = (a, b)
		self.ep = (c, d)

lst = [randint(0, 100) for _ in range(4)]
elements = [choice([Line(*lst), Rect(*lst), Ellipse(*lst)]) for _ in range(217)]
for i, key in enumerate(elements):
	if type(key) == Line:
		elements[i] = Line(0, 0, 0, 0)