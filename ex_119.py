class IterColumn:
	def __init__(self, data, column):
		self.data = data
		self.index = column

	def __iter__(self):
		for row in self.data:
			yield row[self.index]

lst = [
    ['x00', 'x01', 'x02', 'x03', 'x04'],
    ['x10', 'x11', 'x12', 'x13', 'x14'],
    ['x20', 'x21', 'x22', 'x23', 'x24'],
    ['x30', 'x31', 'x32', 'x33', 'x34'],
]
it = IterColumn(lst, 1)
for x in it:  # последовательный перебор всех элементов столбца списка: x12, x22, ..., xM2
	print(x)

it_iter = iter(it)
x = next(it_iter)