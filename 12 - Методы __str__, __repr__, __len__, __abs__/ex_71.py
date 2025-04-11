import sys
class Book:
	def __init__(self, title, author, pages):
		self.title = title # название книги (строка)
		self.author = author # автор книги (строка)
		self.pages = pages # число страниц в книге (целое число)


	def __str__(self):
		return f"Книга: {self.title}; {self.author}; {self.pages}"

lst_in = list(map(str.strip, sys.stdin.readlines()))
book = Book(*lst_in)
print(book)