class Lib: # представления библиотеки
	def __init__(self):
		self.book_list = [] # список книг в библиотеке

	def __add__(self, book): # добавления книги в библиотеку
		self.book_list.append(book)
		return self

	def __iadd__(self, other):
		self.book_list.append(other)
		return self

	def __sub__(self, other): # удаление книги из библиотеки
		if isinstance(other, int):
			del self.book_list[other]
		elif isinstance(other, Book):
			self.book_list.remove(other)
		return self

	def __isub__(self, other):
		if isinstance(other, int):
			del self.book_list[other]
		elif isinstance(other, Book):
			self.book_list.remove(other)
		return self

	def __len__(self):
		return len(self.book_list)

class Book: # для описания отдельной книги
	def __init__(self, title, author, year):
		self.title = title # заголовок книги
		self.author = author # автор книги
		self.year = year # год издания

