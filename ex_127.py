class Singleton:
	_instance = None

	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = super().__new__(cls)
		return cls._instance

class Game(Singleton):
	def __init__(self, name):
		if not hasattr(self, 'name'):
			self.name = name

game1 = Game("Game 1")
game1 = Game("Game 2")
print(game1.name)
print(game1.name)