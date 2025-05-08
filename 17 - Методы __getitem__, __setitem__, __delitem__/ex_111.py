class StackObj:
	# описания объектов односвязного списка
	def __init__(self, data):
		self.data = data
		self.next = None

class Stack:
	def __init__(self):
		self.head = None
		self.__count_objs = 0

	def push(self, obj):
		last = self[self.__count_objs - 1] if self.__count_objs > 0 else None

		if last:
			last.next = obj

		if self.head is None:
			self.head = obj

		self.__count_objs += 1

	def pop(self):
		if self.__count_objs == 0:
			return None

		last = self[self.__count_objs - 1]

		if self.__count_objs == 1:
			self.head = None
		else:
			self[self.__count_objs - 2].next = None

		self.__count_objs -= 1
		return last

	def __check_index(self, indx):
		if type(indx) != int or not (0 <= indx < self.__count_objs):
			raise IndexError('неверный индекс')


	def __getitem__(self, indx):
		self.__check_index(indx)

		if self.__count_objs == 0:
			return None
		count = 0
		h = self.head
		while h and count < indx:
			h = h.next
			count += 1
		return h

	def __setitem__(self, key, value):
		self.__check_index(key)

		obj = self[key]
		prev = self[key - 1] if key > 0 else None
		value.next = obj.next
		if prev:
			prev.next = value

st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st[1] = StackObj("new obj2")
print(st[2].data) # obj3
print(st[1].data) # new obj2
res = st[3] # исключение IndexError