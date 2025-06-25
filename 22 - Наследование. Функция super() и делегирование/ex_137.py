class Book:
    def __init__(self, title, author, pages, year):
        self.title = title # название книги
        self.author = author # автор книги
        self.pages = pages # количество страниц
        self.year = year # год издания

class DigitBook(Book):
    def __init__(self, title, author, pages, year, size, frm):
        super().__init__(title, author, pages, year)
        self.size = size # размер файла
        self.frm = frm # формат файла
