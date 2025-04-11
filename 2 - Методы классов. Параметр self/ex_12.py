lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']


class DataBase:
	lst_data = []
	FIELDS = ('id', 'name', 'old', 'salary')

	def insert(self, data):
		for i in data:
			dct = dict(zip(self.FIELDS, i.split()))
			self.lst_data.append(dct)

	def select(self, a, b):
		return self.lst_data[a: b + 1]


db = DataBase()
db.insert(lst_in)
print(db.select(0, 2))
