class Player:
	def __init__(self, name, old, score):
		self.name = name # имя игрока
		self.old = int(old) if old.isdigit() and int(old) > 0 else 0 # возраст игрока
		self.score = int(score) if score.isdigit() and int(score) > 0 else 0 # количество очков игрока

	def __bool__(self):
		return True if self.score > 0 else False

lst_in = ['Балакирев; 34; 2048',
		  'Mediel; 27; 0',
		  'Влад; 18; 9012',
		  'Nina P; 33; 0']
players = [Player(*i) for i in list(i.split("; ") for i in lst_in)]
players_filtered = list(filter(lambda x: bool(x), players))

print(list(i.__dict__ for i in players_filtered))