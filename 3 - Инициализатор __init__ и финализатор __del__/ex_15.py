class Point:
	def __init__(self, x, y, color=None):
		self.x = x
		self.y = y
		self.color = color


points = [Point(i * 2 + 1, i * 2 + 1) for i in range(1000)]
points[1] = Point(x=3, y=3, color="yelloq")
