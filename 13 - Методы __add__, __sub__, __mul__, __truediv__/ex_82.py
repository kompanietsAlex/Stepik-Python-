class StackObj:
	def __init__(self, data=None):
		self.__data = data
		self.__next = None

	@property
	def data(self):
		return self.__data

	@data.setter
	def data(self, value):
		self.__data = value

	@property
	def next(self):
		return self.__next

	@next.setter
	def next(self, obj):
		self.__next = obj


class Stack: # описание стека с использованием односвязного списка
	def __init__(self):
		self.top = None
		self.last = None

	def push_back(self, obj): # добавление StackObj в конец односвязного списка
		if self.last:
			self.last.next = obj
		self.last = obj
		if self.top is None:
			self.top = obj


	def pop_back(self): # извлечение последнего объекта с удалением из односвязного	списка
		h = self.top
		if h is None:
			return None

		while h.next and h.next != self.last:
			h = h.next

		if self.top == self.last:
			self.top = 	self.last = None
		else:
			self.last = h
			h.next = None

	def __add__(self, other):
		self.push_back(other)
		return self

	def __iadd__(self, other):
		return self.__add__(other)

	def __mul__(self, other):
		for x in other:
			self.push_back(StackObj(x))
		return self

	def __imul__(self, other):
		return self.__mul__(other)

h = StackObj('5')
print(h,__dict__) # 5
st = Stack()
st.push_back(StackObj('1'))
st.push_back(StackObj('2'))
st.push_back(StackObj('3'))
st = st + StackObj('4')
st += StackObj('5')
st = st * [str(i) for i in range(6, 9)]
st *= [str(i) for i in range(9, 12)]