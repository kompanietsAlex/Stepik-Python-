class Book:
	def __init__(self, author, title, price):
		self.__author = author # строка с именем автора
		self.__title = title # строка с названием книги
		self.__price = int(price) # целое число с	ценой книги


	def set_title(self, title): # запись в __title значения title
		self.__title = title

	def set_author(self, author): # запись в __author значения author
		self.__author = author

	def set_price(self, price): # запись в __price значения price;
		self.__price = price

	def get_title(self): # получение значения __title класса Book
		return self.__title

	def get_author(self): # получение значения __author класса Book
		return self.__author

	def get_price(self): # получение значения __price класса Book
		return self.__price