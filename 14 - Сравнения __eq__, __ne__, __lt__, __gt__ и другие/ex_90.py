class Morph:
	def __init__(self, *args):
		self._words = list(map(lambda x: x.strip(" .,!?;:").lower(), args))

	def add_word(self, word):
		w = word.lower()
		if w not in self._words:
			self._words.append(w)

	def get_words(self):
		return tuple(self._words)

	def __eq__(self, other):
		return other.lower() in self._words

dict_words = [Morph("связь", "связи", "связью", "связей", "связям", "связями", "связях"),
			  Morph("формула", "формулы", "формуле", "формулу", "формулой", "формул", "формулам", "формулами", "формулах"),
			  Morph("вектор", "вектора", "вектору", "вектором", "векторе", "векторы", "векторов", "векторам", "векторами", "векторах"),
			  Morph("эффект", "эффекта", "эффекту", "эффектом", "эффекте", "эффекты", "эффектов", "эффектам", "эффектами", "эффектах"),
			  Morph("день", "дня", "дню", "днем", "дне", "дни", "дням", "днями", "днях")]

text = input()
words = map(lambda x: x.strip(".,!?;:").lower(), text.split())
res = sum(word == morph for word in words for morph in dict_words)
