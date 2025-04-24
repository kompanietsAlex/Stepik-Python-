class Track:
	def __init__(self, start_x, start_y):
		self.start_x = start_x
		self.start_y = start_y
		self.coords = []

	def add_point(self, x, y, speed):
		self.coords.append([x, y, speed])

	def __setitem__(self, key, value):
		self.coords[key][2] = value

	def __getitem__(self, key):
		if key >= len(self.coords):
			raise IndexError('некорректный индекс')
		return (tuple(self.coords[key][:2]), self.coords[key][-1])




tr = Track(10, -5.4)
tr.add_point(20, 0, 100) # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80) # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34) # третий линейный сегмент: indx = 2

print(tr.coords)
tr[2] = 60
print(tr[2])
c, s = tr[2]
print(c, s)

res = tr[3] # IndexError