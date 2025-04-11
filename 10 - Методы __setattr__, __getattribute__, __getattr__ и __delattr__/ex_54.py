class Book:
	def __init__(self, title='', author='', pages=0, year=0):
		self.title = title  # заголовок книги (строка, по умолчанию пустая строка);
		self.author = author # автор книги (строка, по умолчанию пустая строка);
		self.pages = pages # число страниц (целое число, по умолчанию 0);
		self.year = year # год издания (целое число, по умолчанию 0).

	def __setattr__(self, key, value):
		if key in ("title", "author") and type(value) == str:
			self.__dict__[key] = value
		elif key in ("pages", "year") and type(value) == int:
			self.__dict__[key] = value
		else:
			raise TypeError("Неверный тип присваиваемых данных.")

book = Book("Python ООП", "Сергей Балакирев", 123, 2022)