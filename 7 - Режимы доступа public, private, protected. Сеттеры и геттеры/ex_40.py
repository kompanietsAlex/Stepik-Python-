class ObjList:
	def __init__(self, data):
		self.__data = data
		self.__next = self.__prev = None

	def set_next(self, obj): # изменение __next на значение	obj
		self.__next = obj

	def set_prev(self, obj): # изменение __prev	на значение obj
		self.__prev = obj

	def get_next(self): # получение	приватного __next
		return self.__next

	def get_prev(self): # получение	приватного __prev
		return self.__prev

	def set_data(self, data): # изменение __data на	значение data
		self.__data = data

	def get_data(self): # получение	приватного __data
		return self.__data


class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def add_obj(self, obj): # добавление obj в конец связного списка
		if self.tail:
			self.tail.set_next(obj)
		obj.set_prev(self.tail)
		self.tail = obj
		if not self.head:
			self.head = obj

	def remove_obj(self): # удаление последнего	объекта	из связного	списка
		if self.tail is None:
			return
		prev = self.tail.get_prev()
		if prev:
			prev.set_next(None)
		self.tail = prev
		if self.tail is None:
			self.head = None

	def get_data(self): # получение списка из строк	__data всех объектов списка
		s = []
		h = self.head
		while h:
			s.append(h.get_data())
			h = h.get_next()
		return s