class TriangleListIterator:
	def __init__(self, lst):
		self._lst = lst

	def __iter__(self):
		for i in range(len(self._lst)):
			for j in range(i + 1):
				yield self._lst[i][j]

lst = [[1, 11, 111, 1111, 11111, 111111],
       [2, 22, 222, 2222, 22222, 222222],
       [3, 33, 333, 3333, 33333, 333333],
       [4, 44, 444, 4444, 44444, 444444]]

it = TriangleListIterator(lst)
for x in it:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
	print(x)

it_iter = iter(it)
x = next(it_iter)
print(x)