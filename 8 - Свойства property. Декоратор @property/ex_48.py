class PhoneNumber:
	def __init__(self, number, fio):
		self.number = number # номер телефона(число);
		self.fio = fio # ФИО владельца	номера телефона



class PhoneBook:
	def __init__(self):
		self.phone_numbers = [] # список объектов PhoneNumber


	def add_phone(self, obj): # добавление нового номера телефона
		self.phone_numbers.append(obj)

	def remove_phone(self, indx): # удаление номера телефона по индексу
		del self.phone_numbers[indx]

	def get_phone_list(self): # получение списка из	объектов всех телефонных номеров
		return self.phone_numbers



p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()