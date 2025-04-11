class BookStudy:
	def __init__(self, name, author, year):
		self.name = name
		self.author = author
		self.year = year

	def __eq__(self, other):
		return hash(self) == hash(other)

	def __hash__(self):
		return hash((self.name, self.author))

# считывание списка из входного потока
lst_in = [
    'Python; Балакирев С.М.; 2020',
    'Python ООП; Балакирев С.М.; 2021',
    'Python ООП; Балакирев С.М.; 2022',
    'Python; Балакирев С.М.; 2021']

lst_bs = list(map(lambda x: BookStudy(*x.split('; ')), lst_in))
unique_books = len(set(lst_bs))