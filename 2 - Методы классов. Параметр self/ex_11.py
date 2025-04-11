class StreamData:
	def create(self, fields, lst_values):
		if len(fields) != len(lst_values):
			return False

		for i, key in enumerate(fields):
			setattr(self, key, lst_values[i])

		return True


class StreamReader:
	FIELDS = ('id', 'title', 'pages')

	def readlines(self):
		lst_in = ["10", "Питон - основы мастерства", "512"]  # считывание списка строк из входного потока
		sd = StreamData()
		res = sd.create(self.FIELDS, lst_in)
		return sd, res


sr = StreamReader()
data, result = sr.readlines()