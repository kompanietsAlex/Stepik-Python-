class StackObj: # описания объектов односвязного списка
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
		if type(obj) == StackObj or obj == None:
			self.__next = obj

class Stack: # описание стека с использованием односвязного списка
	def __init__(self):
		self.top = None
		self.last = None

	def push(self, obj): # добавление StackObj в конец односвязного списка
		if self.last:
			self.last.next = obj
		self.last = obj
		if self.top is None:
			self.top = obj


	def pop(self): # извлечение последнего объекта с удалением из односвязного	списка
		h = self.top
		if h is None:
			return None
		while h and h.next != self.last:
			h = h.next

		if h:
			h.next = None

		last = self.last
		self.last = h

		if self.last is None:
			self.top = None
		return last

	def get_data(self): # получение списка из объектов односвязного списка
		s = []
		h = self.top
		while h:
			s.append(h.data)
			h = h.next
		return s

head_obj = StackObj()
obj = head_obj
