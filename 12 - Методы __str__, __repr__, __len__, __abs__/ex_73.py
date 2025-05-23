class WordString:
	def __init__(self, args=""):
		self.__words = ''
		self.string = args

	def __len__(self):
		return len(self.string.split())

	def __call__(self, indx, *args, **kwargs):
		return self.words(indx)

	def words(self, indx):
		if 0 <= indx <= self.__len__():
			return self.string.split()[indx]

	@property
	def string(self):
		return self.__words

	@string.setter
	def string(self, value=""):
		self.__words = value

words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")